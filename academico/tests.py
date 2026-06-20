from unittest.mock import patch

from django.test import SimpleTestCase, TestCase

from .forms import MateriaForm
from .models import Materia


class CodigoAutomaticoMateriaTests(SimpleTestCase):
    def crear_materia(self, codigo=''):
        return Materia(
            codigo=codigo,
            nombre='Matematica',
            descripcion='Fundamentos de matematica.',
            creditos=4,
        )

    def test_codigo_no_es_editable_ni_aparece_en_el_formulario(self):
        self.assertFalse(Materia._meta.get_field('codigo').editable)
        self.assertNotIn('codigo', MateriaForm().fields)

    @patch('django.db.models.Model.save')
    @patch('academico.models.generar_codigo', return_value='MAT-0001')
    def test_genera_codigo_al_guardar_una_materia_nueva(
        self,
        generar_codigo_simulado,
        guardar_simulado,
    ):
        materia = self.crear_materia()

        materia.save()

        self.assertEqual(materia.codigo, 'MAT-0001')
        generar_codigo_simulado.assert_called_once_with(
            modelo=Materia,
            nombre_campo='codigo',
            prefijo='MAT',
            cantidad_digitos=4,
        )
        guardar_simulado.assert_called_once_with()

    @patch('django.db.models.Model.save')
    @patch('academico.models.generar_codigo')
    def test_conserva_el_codigo_al_editar_una_materia(
        self,
        generar_codigo_simulado,
        guardar_simulado,
    ):
        materia = self.crear_materia(codigo='MAT-0007')

        materia.save(update_fields=['nombre'])

        self.assertEqual(materia.codigo, 'MAT-0007')
        generar_codigo_simulado.assert_not_called()
        guardar_simulado.assert_called_once_with(update_fields=['nombre'])


class CodigoAutomaticoMateriaIntegracionTests(TestCase):
    def crear_materia(self, nombre):
        return Materia.objects.create(
            nombre=nombre,
            descripcion=f'Descripcion de {nombre}.',
            creditos=4,
        )

    def test_genera_codigos_correlativos_al_crear_materias(self):
        primera_materia = self.crear_materia('Matematica')
        segunda_materia = self.crear_materia('Comunicacion')

        self.assertEqual(primera_materia.codigo, 'MAT-0001')
        self.assertEqual(segunda_materia.codigo, 'MAT-0002')
