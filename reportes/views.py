from collections import defaultdict

from django.shortcuts import get_object_or_404, render

from academico.models import Matricula
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
