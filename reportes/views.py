from collections import defaultdict

from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, render

from academico.models import Materia, Matricula, PeriodoAcademico
from asistencia.models import Asistencia
from asistencia.utils import resumen_asistencia_matricula
from estudiantes.models import Estudiante
from notas.models import Nota
from notas.utils import (
    calcular_promedio_ponderado_por_matricula,
    determinar_estado_promedio,
)


def panel_reportes(request):
    """Muestra las opciones iniciales del módulo de reportes."""
    return render(request, 'reportes/panel_reportes.html')


def reporte_estudiante(request, estudiante_id):
    """Muestra el resumen académico y de asistencia de un estudiante."""
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    matriculas = list(
        Matricula.objects
        .filter(estudiante=estudiante)
        .select_related('materia', 'periodo')
        .order_by('periodo__fecha_inicio', 'materia__nombre')
    )

    notas_por_matricula = defaultdict(list)
    for nota in (
        Nota.objects
        .filter(matricula__in=matriculas)
        .select_related('evaluacion')
        .order_by('matricula_id', 'evaluacion__nombre')
    ):
        notas_por_matricula[nota.matricula_id].append(nota)

    matriculas_con_asistencia = set(
        Asistencia.objects
        .filter(matricula__in=matriculas)
        .values_list('matricula_id', flat=True)
        .distinct()
    )

    reportes_materias = []
    for matricula in matriculas:
        promedio = calcular_promedio_ponderado_por_matricula(matricula)
        resumen_asistencia = resumen_asistencia_matricula(matricula)

        reportes_materias.append({
            'matricula': matricula,
            'notas': notas_por_matricula[matricula.id],
            'tiene_notas': bool(notas_por_matricula[matricula.id]),
            'promedio': promedio,
            'estado': determinar_estado_promedio(promedio),
            'asistencia': resumen_asistencia,
            'tiene_asistencia': matricula.id in matriculas_con_asistencia,
        })

    return render(
        request,
        'reportes/reporte_estudiante.html',
        {
            'estudiante': estudiante,
            'reportes_materias': reportes_materias,
        },
    )


def reporte_materia(request, materia_id, periodo_id):
    """Muestra el rendimiento y asistencia de una materia en un periodo."""
    materia = get_object_or_404(Materia, id=materia_id)
    periodo = get_object_or_404(PeriodoAcademico, id=periodo_id)
    matriculas = list(
        Matricula.objects
        .filter(materia=materia, periodo=periodo)
        .select_related('estudiante')
        .order_by('estudiante__apellidos', 'estudiante__nombres')
    )

    notas_por_matricula = defaultdict(list)
    for nota in (
        Nota.objects
        .filter(matricula__in=matriculas)
        .select_related('evaluacion')
        .order_by('matricula_id', 'evaluacion__nombre')
    ):
        notas_por_matricula[nota.matricula_id].append(nota)

    estudiantes_reporte = []
    aprobados = 0
    desaprobados = 0
    pendientes = 0

    for matricula in matriculas:
        promedio = calcular_promedio_ponderado_por_matricula(matricula)
        estado = determinar_estado_promedio(promedio)

        if estado == 'aprobado':
            aprobados += 1
        elif estado == 'desaprobado':
            desaprobados += 1
        else:
            pendientes += 1

        estudiantes_reporte.append({
            'matricula': matricula,
            'notas': notas_por_matricula[matricula.id],
            'tiene_notas': bool(notas_por_matricula[matricula.id]),
            'promedio': promedio,
            'estado': estado,
        })

    resumen_asistencia = Asistencia.objects.filter(
        matricula__in=matriculas,
    ).aggregate(
        total_registros=Count('id'),
        presentes=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_PRESENTE),
        ),
        tardanzas=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_TARDANZA),
        ),
        faltas=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_FALTA),
        ),
        justificados=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_JUSTIFICADO),
        ),
    )

    return render(
        request,
        'reportes/reporte_materia.html',
        {
            'materia': materia,
            'periodo': periodo,
            'estudiantes_reporte': estudiantes_reporte,
            'aprobados': aprobados,
            'desaprobados': desaprobados,
            'pendientes': pendientes,
            'resumen_asistencia': resumen_asistencia,
        },
    )


def reporte_periodo(request, periodo_id):
    """Muestra los indicadores académicos generales de un periodo."""
    periodo = get_object_or_404(PeriodoAcademico, id=periodo_id)
    matriculas = Matricula.objects.filter(periodo=periodo)
    total_matriculas = matriculas.count()
    total_estudiantes = Estudiante.objects.filter(
        matricula__periodo=periodo,
    ).distinct().count()
    total_materias_activas = Materia.objects.filter(
        matricula__periodo=periodo,
        estado=Materia.ESTADO_ACTIVO,
    ).distinct().count()

    resumen_notas = Nota.objects.filter(
        matricula__periodo=periodo,
    ).aggregate(
        total_registros=Count('id'),
        promedio_general=Avg('calificacion'),
    )

    resumen_asistencia = Asistencia.objects.filter(
        matricula__periodo=periodo,
    ).aggregate(
        total_registros=Count('id'),
        presentes=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_PRESENTE),
        ),
        tardanzas=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_TARDANZA),
        ),
        faltas=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_FALTA),
        ),
        justificados=Count(
            'id',
            filter=Q(estado=Asistencia.ESTADO_JUSTIFICADO),
        ),
    )

    return render(
        request,
        'reportes/reporte_periodo.html',
        {
            'periodo': periodo,
            'total_estudiantes': total_estudiantes,
            'total_materias_activas': total_materias_activas,
            'total_matriculas': total_matriculas,
            'resumen_notas': resumen_notas,
            'resumen_asistencia': resumen_asistencia,
        },
    )
