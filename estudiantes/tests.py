from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

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


class ListaEstudiantesTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user(
            username='usuario_estudiantes',
            password='clave-segura-prueba',
        )
        self.client.force_login(usuario)
        self.estudiante_activo = Estudiante.objects.create(
            codigo='EST-0001',
            nombres='Ana',
            apellidos='Torres',
            dni='12345678',
            correo='ana@example.com',
            telefono='999999999',
            direccion='Lima',
        )
        self.estudiante_inactivo = Estudiante.objects.create(
            codigo='EST-0002',
            nombres='Luis',
            apellidos='Ramos',
            dni='87654321',
            correo='luis@example.com',
            telefono='988888888',
            direccion='Lima',
            estado=Estudiante.ESTADO_INACTIVO,
        )

    def test_busca_por_codigo_nombres_apellidos_y_dni(self):
        for termino in ('EST-0001', 'Ana', 'Torres', '12345678'):
            with self.subTest(termino=termino):
                respuesta = self.client.get(
                    reverse('estudiantes:listar_estudiantes'),
                    {'q': termino},
                )

                self.assertEqual(
                    list(respuesta.context['estudiantes']),
                    [self.estudiante_activo],
                )
                self.assertEqual(respuesta.context['consulta'], termino)

    def test_oculta_desactivar_para_estudiantes_inactivos(self):
        respuesta = self.client.get(reverse('estudiantes:listar_estudiantes'))

        self.assertContains(
            respuesta,
            reverse(
                'estudiantes:desactivar_estudiante',
                args=[self.estudiante_activo.id],
            ),
        )
        self.assertNotContains(
            respuesta,
            reverse(
                'estudiantes:desactivar_estudiante',
                args=[self.estudiante_inactivo.id],
            ),
        )
