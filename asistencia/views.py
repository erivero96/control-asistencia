from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from academico.models import Materia
from estudiantes.models import Estudiante

from .forms import AsistenciaForm
from .models import Asistencia


def index(request):
    return HttpResponse('Modulo de asistencia')


def _asistencias_con_relaciones():
    return Asistencia.objects.select_related(
        'matricula__estudiante',
        'matricula__materia',
        'matricula__periodo',
    )


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
