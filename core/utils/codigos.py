import re

from django.core.exceptions import FieldDoesNotExist
from django.db.models import Model


def generar_codigo(
    modelo: type[Model],
    nombre_campo: str,
    prefijo: str,
    cantidad_digitos: int,
) -> str:
    """Genera el siguiente codigo correlativo para un modelo de Django.

    El ultimo valor se obtiene ordenando de forma descendente el campo indicado.
    Si no hay codigos registrados, la numeracion comienza en uno. El codigo
    existente debe respetar exactamente el formato ``PREFIJO-0001``.
    """
    if not isinstance(nombre_campo, str) or not nombre_campo:
        raise ValueError('El nombre del campo de codigo no puede estar vacio.')

    if not isinstance(prefijo, str) or not prefijo:
        raise ValueError('El prefijo no puede estar vacio.')

    if (
        not isinstance(cantidad_digitos, int)
        or isinstance(cantidad_digitos, bool)
        or cantidad_digitos <= 0
    ):
        raise ValueError('La cantidad de digitos debe ser un entero mayor que cero.')

    try:
        modelo._meta.get_field(nombre_campo)
    except (AttributeError, FieldDoesNotExist) as error:
        nombre_modelo = getattr(modelo, '__name__', str(modelo))
        raise ValueError(
            f'El campo "{nombre_campo}" no existe en el modelo {nombre_modelo}.'
        ) from error

    ultimo_codigo = (
        modelo._default_manager
        .order_by(f'-{nombre_campo}')
        .values_list(nombre_campo, flat=True)
        .first()
    )

    if ultimo_codigo is None:
        siguiente_numero = 1
    else:
        patron = rf'{re.escape(prefijo)}-(\d{{{cantidad_digitos}}})'
        coincidencia = re.fullmatch(patron, str(ultimo_codigo))

        if coincidencia is None:
            raise ValueError(
                f'El ultimo codigo "{ultimo_codigo}" no tiene el formato esperado: '
                f'{prefijo}- seguido de {cantidad_digitos} digitos.'
            )

        siguiente_numero = int(coincidencia.group(1)) + 1

    if siguiente_numero > (10**cantidad_digitos) - 1:
        raise ValueError(
            f'No se pueden generar mas codigos con {cantidad_digitos} digitos '
            f'para el prefijo "{prefijo}".'
        )

    return f'{prefijo}-{siguiente_numero:0{cantidad_digitos}d}'
