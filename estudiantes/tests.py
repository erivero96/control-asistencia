from unittest.mock import patch

from django.test import SimpleTestCase, TestCase

from .forms import EstudianteForm
from .models import Estudiante


class CodigoAutomaticoEstudianteTests(SimpleTestCase):
    def crear_estudiante(self, codigo=''):
        return Estudiante(
            codigo=codigo,
            nombres='Ana',
            apellidos='Torres',
            dni='12345678',
            correo='ana@example.com',
            telefono='999999999',
            direccion='Lima',
        )

    def test_codigo_no_es_editable_ni_aparece_en_el_formulario(self):
        self.assertFalse(Estudiante._meta.get_field('codigo').editable)
        self.assertNotIn('codigo', EstudianteForm().fields)

    @patch('django.db.models.Model.save')
    @patch('estudiantes.models.generar_codigo', return_value='EST-0001')
    def test_genera_codigo_al_guardar_un_estudiante_nuevo(
        self,
        generar_codigo_simulado,
        guardar_simulado,
    ):
        estudiante = self.crear_estudiante()

        estudiante.save()

        self.assertEqual(estudiante.codigo, 'EST-0001')
        generar_codigo_simulado.assert_called_once_with(
            modelo=Estudiante,
            nombre_campo='codigo',
            prefijo='EST',
            cantidad_digitos=4,
        )
        guardar_simulado.assert_called_once_with()

    @patch('django.db.models.Model.save')
    @patch('estudiantes.models.generar_codigo')
    def test_conserva_el_codigo_al_editar_un_estudiante(
        self,
        generar_codigo_simulado,
        guardar_simulado,
    ):
        estudiante = self.crear_estudiante(codigo='EST-0007')

        estudiante.save(update_fields=['nombres'])

        self.assertEqual(estudiante.codigo, 'EST-0007')
        generar_codigo_simulado.assert_not_called()
        guardar_simulado.assert_called_once_with(update_fields=['nombres'])


class CodigoAutomaticoEstudianteIntegracionTests(TestCase):
    def crear_estudiante(self, dni, correo):
        return Estudiante.objects.create(
            nombres='Ana',
            apellidos='Torres',
            dni=dni,
            correo=correo,
            telefono='999999999',
            direccion='Lima',
        )

    def test_genera_codigos_correlativos_al_crear_estudiantes(self):
        primer_estudiante = self.crear_estudiante(
            dni='12345678',
            correo='ana@example.com',
        )
        segundo_estudiante = self.crear_estudiante(
            dni='87654321',
            correo='luis@example.com',
        )

        self.assertEqual(primer_estudiante.codigo, 'EST-0001')
        self.assertEqual(segundo_estudiante.codigo, 'EST-0002')
