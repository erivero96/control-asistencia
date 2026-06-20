from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MateriaForm, MatriculaForm, PeriodoAcademicoForm
from .models import Materia, Matricula, PeriodoAcademico


@login_required
def index(request):
    return render(request, 'academico/panel_academico.html')


@login_required
def listar_materias(request):
    materias = Materia.objects.all().order_by('nombre')

    return render(
        request,
        'academico/materias_lista.html',
        {'materias': materias},
    )


@login_required
def crear_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)

        if form.is_valid():
            materia = form.save()
            messages.success(
                request,
                f'Materia {materia.nombre} registrada correctamente.',
            )
            return redirect('academico:listar_materias')

        messages.error(
            request,
            'No se pudo registrar la materia. Revise los datos ingresados.',
        )
    else:
        form = MateriaForm()

    return render(
        request,
        'academico/materia_formulario.html',
        {
            'form': form,
            'titulo': 'Registrar materia',
            'texto_boton': 'Guardar materia',
        },
    )


@login_required
def editar_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)

    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)

        if form.is_valid():
            materia = form.save()
            messages.success(
                request,
                f'Materia {materia.nombre} actualizada correctamente.',
            )
            return redirect('academico:listar_materias')

        messages.error(
            request,
            'No se pudo actualizar la materia. Revise los datos ingresados.',
        )
    else:
        form = MateriaForm(instance=materia)

    return render(
        request,
        'academico/materia_formulario.html',
        {
            'form': form,
            'materia': materia,
            'titulo': 'Editar materia',
            'texto_boton': 'Guardar cambios',
        },
    )


@login_required
def desactivar_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)

    if request.method == 'POST':
        if materia.estado == Materia.ESTADO_INACTIVO:
            messages.error(
                request,
                'La materia ya se encuentra inactiva.',
            )
        else:
            materia.estado = Materia.ESTADO_INACTIVO
            materia.save(update_fields=['estado'])
            messages.success(
                request,
                f'Materia {materia.nombre} desactivada correctamente.',
            )

        return redirect('academico:listar_materias')

    return render(
        request,
        'academico/materia_confirmar_desactivar.html',
        {'materia': materia},
    )


@login_required
def listar_periodos(request):
    periodos = PeriodoAcademico.objects.all().order_by('fecha_inicio')

    return render(
        request,
        'academico/periodos_lista.html',
        {'periodos': periodos},
    )


@login_required
def crear_periodo(request):
    if request.method == 'POST':
        form = PeriodoAcademicoForm(request.POST)

        if form.is_valid():
            periodo = form.save()
            messages.success(
                request,
                f'Periodo academico {periodo.nombre} registrado correctamente.',
            )
            return redirect('academico:listar_periodos')

        messages.error(
            request,
            'No se pudo registrar el periodo academico. '
            'Revise los datos ingresados.',
        )
    else:
        form = PeriodoAcademicoForm()

    return render(
        request,
        'academico/periodo_formulario.html',
        {
            'form': form,
            'titulo': 'Registrar periodo academico',
            'texto_boton': 'Guardar periodo',
        },
    )


@login_required
def editar_periodo(request, periodo_id):
    periodo = get_object_or_404(PeriodoAcademico, id=periodo_id)

    if request.method == 'POST':
        form = PeriodoAcademicoForm(request.POST, instance=periodo)

        if form.is_valid():
            periodo = form.save()
            messages.success(
                request,
                f'Periodo academico {periodo.nombre} actualizado correctamente.',
            )
            return redirect('academico:listar_periodos')

        messages.error(
            request,
            'No se pudo actualizar el periodo academico. '
            'Revise los datos ingresados.',
        )
    else:
        form = PeriodoAcademicoForm(instance=periodo)

    return render(
        request,
        'academico/periodo_formulario.html',
        {
            'form': form,
            'periodo': periodo,
            'titulo': 'Editar periodo academico',
            'texto_boton': 'Guardar cambios',
        },
    )


@login_required
def listar_matriculas(request):
    matriculas = (
        Matricula.objects
        .select_related('estudiante', 'materia', 'periodo')
        .order_by(
            'periodo__fecha_inicio',
            'estudiante__apellidos',
            'estudiante__nombres',
        )
    )

    return render(
        request,
        'academico/matriculas_lista.html',
        {'matriculas': matriculas},
    )


@login_required
def crear_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)

        if form.is_valid():
            matricula = form.save()
            messages.success(
                request,
                'Matricula registrada correctamente.',
            )
            return redirect('academico:detalle_matricula', matricula_id=matricula.id)

        messages.error(
            request,
            'No se pudo registrar la matricula. Revise los datos ingresados.',
        )
    else:
        form = MatriculaForm()

    return render(
        request,
        'academico/matricula_formulario.html',
        {
            'form': form,
            'titulo': 'Registrar matricula',
            'texto_boton': 'Guardar matricula',
        },
    )


@login_required
def detalle_matricula(request, matricula_id):
    matricula = get_object_or_404(
        Matricula.objects.select_related('estudiante', 'materia', 'periodo'),
        id=matricula_id,
    )

    return render(
        request,
        'academico/matricula_detalle.html',
        {'matricula': matricula},
    )


@login_required
def retirar_matricula(request, matricula_id):
    matricula = get_object_or_404(
        Matricula.objects.select_related('estudiante', 'materia', 'periodo'),
        id=matricula_id,
    )

    if request.method == 'POST':
        if matricula.estado == Matricula.ESTADO_RETIRADO:
            messages.error(
                request,
                'La matricula ya se encuentra retirada.',
            )
        else:
            matricula.estado = Matricula.ESTADO_RETIRADO
            matricula.save(update_fields=['estado'])
            messages.success(
                request,
                'Matricula retirada correctamente.',
            )

        return redirect('academico:listar_matriculas')

    return render(
        request,
        'academico/matricula_confirmar_retirar.html',
        {'matricula': matricula},
    )
