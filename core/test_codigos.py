from unittest.mock import Mock

from django.core.exceptions import FieldDoesNotExist
from django.test import SimpleTestCase

from core.utils.codigos import generar_codigo


class GenerarCodigoTests(SimpleTestCase):
    def crear_modelo_simulado(self, ultimo_codigo):
        modelo = Mock()
        modelo.__name__ = 'ModeloPrueba'
        modelo._meta.get_field.return_value = Mock()
        modelo._default_manager.order_by.return_value.values_list.return_value.first.return_value = (
            ultimo_codigo
        )
        return modelo

    def test_inicia_en_uno_cuando_no_existen_registros(self):
        modelo = self.crear_modelo_simulado(None)

        codigo = generar_codigo(modelo, 'codigo', 'EST', 4)

        self.assertEqual(codigo, 'EST-0001')

    def test_incrementa_el_ultimo_codigo(self):
        modelo = self.crear_modelo_simulado('MAT-0042')

        codigo = generar_codigo(modelo, 'codigo', 'MAT', 4)

        self.assertEqual(codigo, 'MAT-0043')
        modelo._default_manager.order_by.assert_called_once_with('-codigo')

    def test_rechaza_un_ultimo_codigo_con_formato_invalido(self):
        modelo = self.crear_modelo_simulado('MATERIA-42')

        with self.assertRaisesRegex(ValueError, 'no tiene el formato esperado'):
            generar_codigo(modelo, 'codigo', 'MAT', 4)

    def test_rechaza_un_campo_inexistente(self):
        modelo = self.crear_modelo_simulado(None)
        modelo._meta.get_field.side_effect = FieldDoesNotExist

        with self.assertRaisesRegex(ValueError, 'no existe en el modelo'):
            generar_codigo(modelo, 'codigo_inexistente', 'EST', 4)

    def test_rechaza_el_desbordamiento_de_la_numeracion(self):
        modelo = self.crear_modelo_simulado('EVA-9999')

        with self.assertRaisesRegex(ValueError, 'No se pueden generar mas codigos'):
            generar_codigo(modelo, 'codigo', 'EVA', 4)

    def test_valida_los_parametros_de_configuracion(self):
        modelo = self.crear_modelo_simulado(None)

        casos_invalidos = [
            ('', 'EST', 4),
            ('codigo', '', 4),
            ('codigo', 'EST', 0),
            ('codigo', 'EST', True),
        ]

        for nombre_campo, prefijo, cantidad_digitos in casos_invalidos:
            with self.subTest(
                nombre_campo=nombre_campo,
                prefijo=prefijo,
                cantidad_digitos=cantidad_digitos,
            ):
                with self.assertRaises(ValueError):
                    generar_codigo(
                        modelo,
                        nombre_campo,
                        prefijo,
                        cantidad_digitos,
                    )
