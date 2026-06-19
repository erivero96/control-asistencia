from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from academico.models import Materia, Matricula
from estudiantes.models import Estudiante

from .forms import AsistenciaForm, AsistenciaPorMateriaForm
from .models import Asistencia
from .utils import resumen_asistencia_matricula


def index(request):
    return HttpResponse('Modulo de asistencia')


def _asistencias_con_relaciones():
    return Asistencia.objects.select_related(
        'matricula__estudiante',
        'matricula__materia',
        'matricula__periodo',
    )


def _matriculas_activas_por_materia_periodo(materia, periodo):
    return (
        Matricula.objects
        .select_related('estudiante', 'materia', 'periodo')
        .filter(
            materia=materia,
            periodo=periodo,
            estado=Matricula.ESTADO_MATRICULADO,
        )
        .order_by('estudiante__apellidos', 'estudiante__nombres')
    )


def _matriculas_con_relaciones():
    return Matricula.objects.select_related('estudiante', 'materia', 'periodo')


def _filas_asistencia_por_matricula(matriculas, fecha):
    matriculas = list(matriculas)
    asistencias = Asistencia.objects.filter(
        matricula__in=matriculas,
        fecha=fecha,
    )
    asistencias_por_matricula = {
        asistencia.matricula_id: asistencia
        for asistencia in asistencias
    }

    return [
        {
            'matricula': matricula,
            'estudiante': matricula.estudiante,
            'materia': matricula.materia,
            'periodo': matricula.periodo,
            'asistencia': asistencias_por_matricula.get(matricula.id),
            'estado_actual': (
                asistencias_por_matricula[matricula.id].estado
                if matricula.id in asistencias_por_matricula
                else Asistencia.ESTADO_PRESENTE
            ),
        }
        for matricula in matriculas
    ]


def listar_asistencias(request):
    asistencias = _asistencias_con_relaciones().order_by(
        '-fecha',
        'matricula__estudiante__apellidos',
        'matricula__estudiante__nombres',
        'matricula__materia__nombre',
    )

    return render(
        request,
        'asistencia/asistencias_lista.html',
        {'asistencias': asistencias},
    )


def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)

        if form.is_valid():
            asistencia = form.save()
            messages.success(
                request,
                'Asistencia registrada correctamente.',
            )
            return redirect(
                'asistencia:detalle_asistencia',
                asistencia_id=asistencia.id,
            )

        messages.error(
            request,
            'No se pudo registrar la asistencia. Revise los datos ingresados.',
        )
    else:
        form = AsistenciaForm()

    return render(
        request,
        'asistencia/asistencia_formulario.html',
        {
            'form': form,
            'titulo': 'Registrar asistencia',
            'texto_boton': 'Guardar asistencia',
        },
    )


def registrar_asistencia_por_materia(request):
    form_data = request.POST if request.method == 'POST' else request.GET or None
    form = AsistenciaPorMateriaForm(form_data)
    filas_asistencia = []
    estados_asistencia = Asistencia.ESTADO_CHOICES
    materia = None
    periodo = None
    fecha = None

    if form.is_bound and form.is_valid():
        materia = form.cleaned_data['materia']
        periodo = form.cleaned_data['periodo']
        fecha = form.cleaned_data['fecha']
        matriculas = list(
            _matriculas_activas_por_materia_periodo(materia, periodo)
        )

        if not matriculas:
            messages.warning(
                request,
                'No hay estudiantes matriculados en la materia y periodo seleccionados.',
            )
        elif request.method == 'POST':
            estados_validos = {
                estado
                for estado, etiqueta in Asistencia.ESTADO_CHOICES
            }
            estados_por_matricula = {}

            for matricula in matriculas:
                estado = request.POST.get(f'estado_{matricula.id}')

                if estado not in estados_validos:
                    form.add_error(
                        None,
                        f'Seleccione un estado valido para {matricula.estudiante}.',
                    )
                else:
                    estados_por_matricula[matricula.id] = estado

            if form.errors:
                messages.error(
                    request,
                    'No se pudo guardar la asistencia. Revise los estados marcados.',
                )
            else:
                with transaction.atomic():
                    for matricula in matriculas:
                        Asistencia.objects.update_or_create(
                            matricula=matricula,
                            fecha=fecha,
                            defaults={
                                'estado': estados_por_matricula[matricula.id],
                            },
                        )

                messages.success(
                    request,
                    'Asistencia registrada correctamente para la materia seleccionada.',
                )

        filas_asistencia = _filas_asistencia_por_matricula(matriculas, fecha)
    elif form.is_bound:
        messages.error(
            request,
            'Seleccione una materia, un periodo academico y una fecha validos.',
        )

    return render(
        request,
        'asistencia/asistencia_por_materia_formulario.html',
        {
            'form': form,
            'filas_asistencia': filas_asistencia,
            'estados_asistencia': estados_asistencia,
            'materia': materia,
            'periodo': periodo,
            'fecha': fecha,
        },
    )


def editar_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(
        _asistencias_con_relaciones(),
        id=asistencia_id,
    )

    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)

        if form.is_valid():
            asistencia = form.save()
            messages.success(
                request,
                'Asistencia actualizada correctamente.',
            )
            return redirect(
                'asistencia:detalle_asistencia',
                asistencia_id=asistencia.id,
            )

        messages.error(
            request,
            'No se pudo actualizar la asistencia. Revise los datos ingresados.',
        )
    else:
        form = AsistenciaForm(instance=asistencia)

    return render(
        request,
        'asistencia/asistencia_formulario.html',
        {
            'form': form,
            'asistencia': asistencia,
            'titulo': 'Editar asistencia',
            'texto_boton': 'Guardar cambios',
        },
    )


def detalle_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(
        _asistencias_con_relaciones(),
        id=asistencia_id,
    )

    return render(
        request,
        'asistencia/asistencia_detalle.html',
        {'asistencia': asistencia},
    )


def porcentaje_asistencia_matricula(request, matricula_id):
    matricula = get_object_or_404(
        _matriculas_con_relaciones(),
        id=matricula_id,
    )
    resumen = resumen_asistencia_matricula(matricula)

    return render(
        request,
        'asistencia/porcentaje_asistencia_matricula.html',
        resumen,
    )


def porcentajes_por_materia(request, materia_id):
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
    porcentajes = [
        resumen_asistencia_matricula(matricula)
        for matricula in matriculas
    ]

    return render(
        request,
        'asistencia/porcentajes_por_materia.html',
        {
            'materia': materia,
            'porcentajes': porcentajes,
        },
    )


def asistencias_por_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    asistencias = (
        _asistencias_con_relaciones()
        .filter(matricula__estudiante=estudiante)
        .order_by(
            '-fecha',
            'matricula__materia__nombre',
            'matricula__periodo__fecha_inicio',
        )
    )

    return render(
        request,
        'asistencia/asistencias_por_estudiante.html',
        {
            'estudiante': estudiante,
            'asistencias': asistencias,
        },
    )


def asistencias_por_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)
    asistencias = (
        _asistencias_con_relaciones()
        .filter(matricula__materia=materia)
        .order_by(
            '-fecha',
            'matricula__estudiante__apellidos',
            'matricula__estudiante__nombres',
            'matricula__periodo__fecha_inicio',
        )
    )

    return render(
        request,
        'asistencia/asistencias_por_materia.html',
        {
            'materia': materia,
            'asistencias': asistencias,
        },
    )
