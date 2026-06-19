from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EstudianteForm
from .models import Estudiante


def index(request):
    return HttpResponse('Modulo de estudiantes')


def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all().order_by('apellidos', 'nombres')

    return render(
        request,
        'estudiantes/listar_estudiantes.html',
        {'estudiantes': estudiantes},
    )


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)

        if form.is_valid():
            estudiante = form.save()
            messages.success(
                request,
                f'Estudiante {estudiante.nombres} {estudiante.apellidos} '
                'registrado correctamente.',
            )
            return redirect('estudiantes:index')

        messages.error(
            request,
            'No se pudo registrar el estudiante. Revise los datos ingresados.',
        )
    else:
        form = EstudianteForm()

    return render(
        request,
        'estudiantes/crear_estudiante.html',
        {'form': form},
    )


def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)

    return render(
        request,
        'estudiantes/detalle_estudiante.html',
        {'estudiante': estudiante},
    )


def editar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)

    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)

        if form.is_valid():
            estudiante = form.save()
            messages.success(
                request,
                f'Estudiante {estudiante.nombres} {estudiante.apellidos} '
                'actualizado correctamente.',
            )
            return redirect('estudiantes:index')

        messages.error(
            request,
            'No se pudo actualizar el estudiante. Revise los datos ingresados.',
        )
    else:
        form = EstudianteForm(instance=estudiante)

    return render(
        request,
        'estudiantes/editar_estudiante.html',
        {
            'form': form,
            'estudiante': estudiante,
        },
    )


def desactivar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)

    if request.method == 'POST':
        if estudiante.estado == Estudiante.ESTADO_INACTIVO:
            messages.error(
                request,
                'El estudiante ya se encuentra inactivo.',
            )
        else:
            estudiante.estado = Estudiante.ESTADO_INACTIVO
            estudiante.save(update_fields=['estado'])
            messages.success(
                request,
                f'Estudiante {estudiante.nombres} {estudiante.apellidos} '
                'desactivado correctamente.',
            )

        return redirect('estudiantes:index')

    return render(
        request,
        'estudiantes/desactivar_estudiante.html',
        {'estudiante': estudiante},
    )
