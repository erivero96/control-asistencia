from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EstudianteForm
from .models import Estudiante


@login_required
def index(request):
    return HttpResponse('Modulo de estudiantes')


@login_required
def listar_estudiantes(request):
    consulta = request.GET.get('q', '').strip()
    estudiantes = Estudiante.objects.all()

    if consulta:
        estudiantes = estudiantes.filter(
            Q(codigo__icontains=consulta)
            | Q(nombres__icontains=consulta)
            | Q(apellidos__icontains=consulta)
            | Q(dni__icontains=consulta)
        )

    estudiantes = estudiantes.order_by('apellidos', 'nombres')

    return render(
        request,
        'estudiantes/lista.html',
        {
            'estudiantes': estudiantes,
            'consulta': consulta,
        },
    )


@login_required
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
            return redirect('estudiantes:listar_estudiantes')

        messages.error(
            request,
            'No se pudo registrar el estudiante. Revise los datos ingresados.',
        )
    else:
        form = EstudianteForm()

    return render(
        request,
        'estudiantes/formulario.html',
        {
            'form': form,
            'titulo': 'Registrar estudiante',
            'texto_boton': 'Guardar estudiante',
        },
    )


@login_required
def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)

    return render(
        request,
        'estudiantes/detalle.html',
        {'estudiante': estudiante},
    )


@login_required
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
            return redirect('estudiantes:listar_estudiantes')

        messages.error(
            request,
            'No se pudo actualizar el estudiante. Revise los datos ingresados.',
        )
    else:
        form = EstudianteForm(instance=estudiante)

    return render(
        request,
        'estudiantes/formulario.html',
        {
            'form': form,
            'estudiante': estudiante,
            'titulo': 'Editar estudiante',
            'texto_boton': 'Guardar cambios',
        },
    )


@login_required
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

        return redirect('estudiantes:listar_estudiantes')

    return render(
        request,
        'estudiantes/confirmar_desactivar.html',
        {'estudiante': estudiante},
    )
