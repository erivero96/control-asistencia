from decimal import Decimal, ROUND_HALF_UP

from .models import Asistencia


ESTADOS_ASISTENCIA_VALIDA = (
    Asistencia.ESTADO_PRESENTE,
    Asistencia.ESTADO_TARDANZA,
    Asistencia.ESTADO_JUSTIFICADO,
)
PORCENTAJE_PENDIENTE = 'pendiente'


def _redondear_porcentaje(porcentaje):
    return porcentaje.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def _asistencias_de_matricula(matricula):
    return Asistencia.objects.filter(matricula=matricula)


def total_clases_registradas_por_matricula(matricula):
    return _asistencias_de_matricula(matricula).count()


def total_presentes_por_matricula(matricula):
    return _asistencias_de_matricula(matricula).filter(
        estado=Asistencia.ESTADO_PRESENTE,
    ).count()


def total_tardanzas_por_matricula(matricula):
    return _asistencias_de_matricula(matricula).filter(
        estado=Asistencia.ESTADO_TARDANZA,
    ).count()


def total_faltas_por_matricula(matricula):
    return _asistencias_de_matricula(matricula).filter(
        estado=Asistencia.ESTADO_FALTA,
    ).count()


def total_justificados_por_matricula(matricula):
    return _asistencias_de_matricula(matricula).filter(
        estado=Asistencia.ESTADO_JUSTIFICADO,
    ).count()


def calcular_porcentaje_asistencia_por_matricula(matricula):
    total_clases = total_clases_registradas_por_matricula(matricula)

    if total_clases == 0:
        return None

    asistencias_validas = _asistencias_de_matricula(matricula).filter(
        estado__in=ESTADOS_ASISTENCIA_VALIDA,
    ).count()
    porcentaje = (
        Decimal(asistencias_validas)
        * Decimal('100.00')
        / Decimal(total_clases)
    )

    return _redondear_porcentaje(porcentaje)


def resumen_asistencia_matricula(matricula):
    total_clases = total_clases_registradas_por_matricula(matricula)
    presentes = total_presentes_por_matricula(matricula)
    tardanzas = total_tardanzas_por_matricula(matricula)
    faltas = total_faltas_por_matricula(matricula)
    justificados = total_justificados_por_matricula(matricula)
    porcentaje = calcular_porcentaje_asistencia_por_matricula(matricula)

    return {
        'matricula': matricula,
        'estudiante': matricula.estudiante,
        'materia': matricula.materia,
        'periodo': matricula.periodo,
        'total_clases': total_clases,
        'presentes': presentes,
        'tardanzas': tardanzas,
        'faltas': faltas,
        'justificados': justificados,
        'porcentaje': porcentaje,
        'porcentaje_mostrar': (
            porcentaje
            if porcentaje is not None
            else PORCENTAJE_PENDIENTE
        ),
    }
