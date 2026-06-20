from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from academico.models import Materia, Matricula, PeriodoAcademico
from estudiantes.models import Estudiante

from .forms import AsistenciaForm, AsistenciaPorMateriaForm
from .models import Asistencia


class AsistenciaFormValidationTests(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            codigo='EST-0001',
            nombres='Ana',
            apellidos='Torres',
            dni='12345678',
            correo='ana@example.com',
            telefono='999999999',
            direccion='Lima',
        )
        self.materia = Materia.objects.create(
            codigo='MAT-0001',
            nombre='Matematica',
            descripcion='Fundamentos de matematica.',
            creditos=4,
        )
        self.materia_secundaria = Materia.objects.create(
            codigo='MAT-0002',
            nombre='Comunicacion',
            descripcion='Comunicacion oral y escrita.',
            creditos=3,
        )
        self.materia_inactiva = Materia.objects.create(
            codigo='MAT-0003',
            nombre='Historia',
            descripcion='Historia universal.',
            creditos=3,
            estado=Materia.ESTADO_INACTIVO,
        )
        self.periodo = PeriodoAcademico.objects.create(
            nombre='2026-I',
            fecha_inicio=date(2026, 3, 1),
            fecha_fin=date(2026, 7, 31),
        )
        self.periodo_secundario = PeriodoAcademico.objects.create(
            nombre='2026-II',
            fecha_inicio=date(2026, 8, 1),
            fecha_fin=date(2026, 12, 20),
        )
        self.periodo_finalizado = PeriodoAcademico.objects.create(
            nombre='2025-II',
            fecha_inicio=date(2025, 8, 1),
            fecha_fin=date(2025, 12, 20),
            estado=PeriodoAcademico.ESTADO_FINALIZADO,
        )
        self.matricula = Matricula.objects.create(
            estudiante=self.estudiante,
            materia=self.materia,
            periodo=self.periodo,
        )
        self.matricula_retirada = Matricula.objects.create(
            estudiante=self.estudiante,
            materia=self.materia_secundaria,
            periodo=self.periodo,
            estado=Matricula.ESTADO_RETIRADO,
        )
        self.matricula_finalizada = Matricula.objects.create(
            estudiante=self.estudiante,
            materia=self.materia,
            periodo=self.periodo_secundario,
            estado=Matricula.ESTADO_FINALIZADO,
        )

    def datos_asistencia(self, **cambios):
        datos = {
            'matricula': self.matricula.id,
            'fecha': '2026-06-20',
            'estado': Asistencia.ESTADO_PRESENTE,
            'observacion': '',
        }
        datos.update(cambios)
        return datos

    def test_inicia_los_formularios_con_la_fecha_actual(self):
        self.assertEqual(
            AsistenciaForm().fields['fecha'].initial,
            timezone.localdate(),
        )
        self.assertEqual(
            AsistenciaPorMateriaForm().fields['fecha'].initial,
            timezone.localdate(),
        )

    def test_asistencia_form_muestra_solo_matriculas_matriculadas(self):
        formulario = AsistenciaForm()

        self.assertIn(self.matricula, formulario.fields['matricula'].queryset)
        self.assertNotIn(
            self.matricula_retirada,
            formulario.fields['matricula'].queryset,
        )
        self.assertNotIn(
            self.matricula_finalizada,
            formulario.fields['matricula'].queryset,
        )

    def test_valida_fecha_dentro_del_periodo(self):
        for fecha in ('2026-02-28', '2026-08-01'):
            with self.subTest(fecha=fecha):
                formulario = AsistenciaForm(self.datos_asistencia(fecha=fecha))

                self.assertFalse(formulario.is_valid())
                self.assertIn('fecha', formulario.errors)

    def test_no_permite_matriculas_retiradas_o_finalizadas(self):
        for matricula in (self.matricula_retirada, self.matricula_finalizada):
            with self.subTest(matricula=matricula.id):
                formulario = AsistenciaForm(
                    self.datos_asistencia(matricula=matricula.id),
                )

                self.assertFalse(formulario.is_valid())
                self.assertIn('matricula', formulario.errors)

    def test_valida_fecha_en_registro_por_materia(self):
        formulario = AsistenciaPorMateriaForm({
            'materia': self.materia.id,
            'periodo': self.periodo.id,
            'fecha': '2026-08-01',
        })

        self.assertFalse(formulario.is_valid())
        self.assertIn('fecha', formulario.errors)

    def test_registro_por_materia_muestra_opciones_activas(self):
        formulario = AsistenciaPorMateriaForm()

        self.assertNotIn(
            self.materia_inactiva,
            formulario.fields['materia'].queryset,
        )
        self.assertNotIn(
            self.periodo_finalizado,
            formulario.fields['periodo'].queryset,
        )

    def test_no_duplica_asistencia_individual(self):
        Asistencia.objects.create(
            matricula=self.matricula,
            fecha='2026-06-20',
            estado=Asistencia.ESTADO_PRESENTE,
        )
        formulario = AsistenciaForm(self.datos_asistencia())

        self.assertFalse(formulario.is_valid())
        self.assertIn('fecha', formulario.errors)

    def test_registro_por_materia_no_duplica_asistencia_del_mismo_dia(self):
        usuario = get_user_model().objects.create_user(
            username='usuario_asistencia',
            password='clave-segura-prueba',
        )
        self.client.force_login(usuario)
        datos = {
            'materia': self.materia.id,
            'periodo': self.periodo.id,
            'fecha': '2026-06-20',
            f'estado_{self.matricula.id}': Asistencia.ESTADO_PRESENTE,
        }

        respuesta = self.client.post(
            reverse('asistencia:registrar_asistencia_por_materia'),
            datos,
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Asistencia.objects.count(), 1)

        datos[f'estado_{self.matricula.id}'] = Asistencia.ESTADO_TARDANZA
        self.client.post(
            reverse('asistencia:registrar_asistencia_por_materia'),
            datos,
        )

        asistencia = Asistencia.objects.get(
            matricula=self.matricula,
            fecha='2026-06-20',
        )
        self.assertEqual(Asistencia.objects.count(), 1)
        self.assertEqual(asistencia.estado, Asistencia.ESTADO_TARDANZA)
