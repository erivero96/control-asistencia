from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from academico.models import Materia, Matricula
from estudiantes.models import Estudiante

from .forms import EvaluacionForm, NotaForm
from .models import Evaluacion, Nota
from .utils import (
    calcular_promedio_ponderado_por_matricula,
    calcular_promedio_simple_por_matricula,
    determinar_estado_promedio,
)


@login_required
def index(request):
    return HttpResponse('Modulo de notas')


def _notas_con_relaciones():
    return Nota.objects.select_related(
        'matricula__estudiante',
        'matricula__materia',
        'matricula__periodo',
        'evaluacion',
    )


def _matriculas_con_relaciones():
    return Matricula.objects.select_related('estudiante', 'materia', 'periodo')


def _resumen_promedio_matricula(matricula):
    promedio_simple = calcular_promedio_simple_por_matricula(matricula)
    promedio_ponderado = calcular_promedio_ponderado_por_matricula(matricula)
    promedio = promedio_ponderado
    estado = determinar_estado_promedio(promedio)

    return {
        'matricula': matricula,
        'estudiante': matricula.estudiante,
        'materia': matricula.materia,
        'periodo': matricula.periodo,
        'promedio': promedio,
        'promedio_mostrar': promedio if promedio is not None else 'pendiente',
        'promedio_simple': promedio_simple,
        'promedio_ponderado': promedio_ponderado,
        'estado': estado,
    }


@login_required
def listar_evaluaciones(request):
    evaluaciones = (
        Evaluacion.objects
        .select_related('materia', 'periodo')
        .order_by('materia__nombre', 'periodo__fecha_inicio', 'nombre')
    )

    return render(
        request,
        'notas/evaluaciones_lista.html',
        {'evaluaciones': evaluaciones},
    )


@login_required
def crear_evaluacion(request):
    if request.method == 'POST':
        form = EvaluacionForm(request.POST)

        if form.is_valid():
            evaluacion = form.save()
            messages.success(
                request,
                f'Evaluacion {evaluacion.nombre} registrada correctamente.',
            )
            return redirect('notas:listar_evaluaciones')

        messages.error(
            request,
            'No se pudo registrar la evaluacion. Revise los datos ingresados.',
        )
    else:
        form = EvaluacionForm()

    return render(
        request,
        'notas/evaluacion_formulario.html',
        {
            'form': form,
            'titulo': 'Registrar evaluacion',
            'texto_boton': 'Guardar evaluacion',
        },
    )


@login_required
def editar_evaluacion(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id)

    if request.method == 'POST':
        form = EvaluacionForm(request.POST, instance=evaluacion)

        if form.is_valid():
            evaluacion = form.save()
            messages.success(
                request,
                f'Evaluacion {evaluacion.nombre} actualizada correctamente.',
            )
            return redirect('notas:listar_evaluaciones')

        messages.error(
            request,
            'No se pudo actualizar la evaluacion. Revise los datos ingresados.',
        )
    else:
        form = EvaluacionForm(instance=evaluacion)

    return render(
        request,
        'notas/evaluacion_formulario.html',
        {
            'form': form,
            'evaluacion': evaluacion,
            'titulo': 'Editar evaluacion',
            'texto_boton': 'Guardar cambios',
        },
    )


@login_required
def desactivar_evaluacion(request, evaluacion_id):
    evaluacion = get_object_or_404(Evaluacion, id=evaluacion_id)

    if request.method == 'POST':
        if evaluacion.estado == Evaluacion.ESTADO_INACTIVO:
            messages.error(
                request,
                'La evaluacion ya se encuentra inactiva.',
            )
        else:
            evaluacion.estado = Evaluacion.ESTADO_INACTIVO
            evaluacion.save(update_fields=['estado'])
            messages.success(
                request,
                f'Evaluacion {evaluacion.nombre} desactivada correctamente.',
            )

        return redirect('notas:listar_evaluaciones')

    return render(
        request,
        'notas/evaluacion_confirmar_desactivar.html',
        {'evaluacion': evaluacion},
    )


@login_required
def listar_notas(request):
    notas = _notas_con_relaciones().order_by(
        'matricula__estudiante__apellidos',
        'matricula__estudiante__nombres',
        'matricula__materia__nombre',
        'evaluacion__nombre',
    )

    return render(
        request,
        'notas/notas_lista.html',
        {'notas': notas},
    )


@login_required
def registrar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)

        if form.is_valid():
            nota = form.save()
            messages.success(
                request,
                'Nota registrada correctamente.',
            )
            return redirect('notas:detalle_nota', nota_id=nota.id)

        messages.error(
            request,
            'No se pudo registrar la nota. Revise los datos ingresados.',
        )
    else:
        form = NotaForm()

    return render(
        request,
        'notas/nota_formulario.html',
        {
            'form': form,
            'titulo': 'Registrar nota',
            'texto_boton': 'Guardar nota',
        },
    )


@login_required
def editar_nota(request, nota_id):
    nota = get_object_or_404(_notas_con_relaciones(), id=nota_id)

    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)

        if form.is_valid():
            nota = form.save()
            messages.success(
                request,
                'Nota actualizada correctamente.',
            )
            return redirect('notas:detalle_nota', nota_id=nota.id)

        messages.error(
            request,
            'No se pudo actualizar la nota. Revise los datos ingresados.',
        )
    else:
        form = NotaForm(instance=nota)

    return render(
        request,
        'notas/nota_formulario.html',
        {
            'form': form,
            'nota': nota,
            'titulo': 'Editar nota',
            'texto_boton': 'Guardar cambios',
        },
    )


@login_required
def detalle_nota(request, nota_id):
    nota = get_object_or_404(_notas_con_relaciones(), id=nota_id)

    return render(
        request,
        'notas/nota_detalle.html',
        {'nota': nota},
    )


@login_required
def notas_por_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    notas = (
        _notas_con_relaciones()
        .filter(matricula__estudiante=estudiante)
        .order_by(
            'matricula__materia__nombre',
            'matricula__periodo__fecha_inicio',
            'evaluacion__nombre',
        )
    )

    return render(
        request,
        'notas/notas_por_estudiante.html',
        {
            'estudiante': estudiante,
            'notas': notas,
        },
    )


@login_required
def notas_por_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)
    notas = (
        _notas_con_relaciones()
        .filter(matricula__materia=materia)
        .order_by(
            'matricula__estudiante__apellidos',
            'matricula__estudiante__nombres',
            'evaluacion__nombre',
        )
    )

    return render(
        request,
        'notas/notas_por_materia.html',
        {
            'materia': materia,
            'notas': notas,
        },
    )


@login_required
def promedio_matricula(request, matricula_id):
    matricula = get_object_or_404(_matriculas_con_relaciones(), id=matricula_id)
    resumen = _resumen_promedio_matricula(matricula)

    return render(
        request,
        'notas/promedio_matricula.html',
        resumen,
    )


@login_required
def promedios_por_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)
    matriculas = (
        _matriculas_con_relaciones()
        .filter(materia=materia)
        .order_by(
            'estudiante__apellidos',
            'estudiante__nombres',
            'periodo__fecha_inicio',
        )
    )
    promedios = [
        _resumen_promedio_matricula(matricula)
        for matricula in matriculas
    ]

    return render(
        request,
        'notas/promedios_por_materia.html',
        {
            'materia': materia,
            'promedios': promedios,
        },
    )
