from unittest.mock import patch

from django.test import SimpleTestCase, TestCase

from estudiantes.models import Estudiante

from .forms import MateriaForm, MatriculaForm, PeriodoAcademicoForm
from .models import Materia, Matricula, PeriodoAcademico


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


class EstadoInicialFormulariosTests(SimpleTestCase):
    def test_oculta_estado_al_crear_y_lo_mantiene_al_editar(self):
        formularios_nuevos = [
            MateriaForm(),
            PeriodoAcademicoForm(),
            MatriculaForm(),
        ]
        formularios_edicion = [
            MateriaForm(instance=Materia(pk=1)),
            PeriodoAcademicoForm(instance=PeriodoAcademico(pk=1)),
            MatriculaForm(instance=Matricula(pk=1)),
        ]

        for formulario in formularios_nuevos:
            self.assertNotIn('estado', formulario.fields)

        for formulario in formularios_edicion:
            self.assertIn('estado', formulario.fields)


class MatriculaFormDisponibilidadTests(TestCase):
    def setUp(self):
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
        self.materia_activa = Materia.objects.create(
            codigo='MAT-0001',
            nombre='Matematica',
            descripcion='Fundamentos de matematica.',
            creditos=4,
        )
        self.materia_inactiva = Materia.objects.create(
            codigo='MAT-0002',
            nombre='Historia',
            descripcion='Historia universal.',
            creditos=3,
            estado=Materia.ESTADO_INACTIVO,
        )
        self.periodo_activo = PeriodoAcademico.objects.create(
            nombre='2026-I',
            fecha_inicio='2026-03-01',
            fecha_fin='2026-07-31',
        )
        self.periodo_finalizado = PeriodoAcademico.objects.create(
            nombre='2025-II',
            fecha_inicio='2025-08-01',
            fecha_fin='2025-12-20',
            estado=PeriodoAcademico.ESTADO_FINALIZADO,
        )

    def datos_matricula(self):
        return {
            'estudiante': self.estudiante_activo.id,
            'materia': self.materia_activa.id,
            'periodo': self.periodo_activo.id,
        }

    def test_muestra_solo_opciones_activas(self):
        formulario = MatriculaForm()

        self.assertEqual(
            list(formulario.fields['estudiante'].queryset),
            [self.estudiante_activo],
        )
        self.assertEqual(
            list(formulario.fields['materia'].queryset),
            [self.materia_activa],
        )
        self.assertEqual(
            list(formulario.fields['periodo'].queryset),
            [self.periodo_activo],
        )

    def test_no_permite_matricular_opciones_inactivas_o_finalizadas(self):
        casos = [
            ('estudiante', self.estudiante_inactivo.id),
            ('materia', self.materia_inactiva.id),
            ('periodo', self.periodo_finalizado.id),
        ]

        for campo, valor in casos:
            with self.subTest(campo=campo):
                datos = self.datos_matricula()
                datos[campo] = valor
                formulario = MatriculaForm(datos)

                self.assertFalse(formulario.is_valid())
                self.assertIn(campo, formulario.errors)

    def test_guarda_matricula_nueva_con_estado_por_defecto(self):
        datos = self.datos_matricula()
        datos['estado'] = Matricula.ESTADO_RETIRADO
        formulario = MatriculaForm(datos)

        self.assertTrue(formulario.is_valid())

        matricula = formulario.save()

        self.assertEqual(matricula.estado, Matricula.ESTADO_MATRICULADO)
