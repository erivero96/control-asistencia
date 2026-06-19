from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EvaluacionForm
from .models import Evaluacion


def index(request):
    return HttpResponse('Modulo de notas')


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
