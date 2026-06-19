from decimal import Decimal, ROUND_HALF_UP

from .models import Nota


NOTA_MINIMA_APROBATORIA = Decimal('11.00')
ESTADO_APROBADO = 'aprobado'
ESTADO_DESAPROBADO = 'desaprobado'
ESTADO_PENDIENTE = 'pendiente'


def _redondear_promedio(promedio):
    return promedio.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def _notas_de_matricula(matricula):
    return Nota.objects.filter(matricula=matricula).select_related('evaluacion')


def calcular_promedio_simple_por_matricula(matricula):
    notas = list(_notas_de_matricula(matricula))

    if not notas:
        return None

    total = sum((nota.calificacion for nota in notas), Decimal('0.00'))
    promedio = total / Decimal(len(notas))

    return _redondear_promedio(promedio)


def calcular_promedio_ponderado_por_matricula(matricula):
    notas = list(_notas_de_matricula(matricula))

    if not notas:
        return None

    total_ponderado = Decimal('0.00')
    total_pesos = Decimal('0.00')

    for nota in notas:
        peso = nota.evaluacion.peso if nota.evaluacion else Decimal('0.00')

        if peso <= 0:
            continue

        total_ponderado += nota.calificacion * peso
        total_pesos += peso

    if total_pesos <= 0:
        return calcular_promedio_simple_por_matricula(matricula)

    promedio = total_ponderado / total_pesos

    return _redondear_promedio(promedio)


def determinar_estado_promedio(promedio):
    if promedio is None:
        return ESTADO_PENDIENTE

    if promedio >= NOTA_MINIMA_APROBATORIA:
        return ESTADO_APROBADO

    return ESTADO_DESAPROBADO
