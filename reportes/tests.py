from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from academico.models import Materia, Matricula, PeriodoAcademico
from asistencia.models import Asistencia
from estudiantes.models import Estudiante
from notas.models import Evaluacion, Nota


class IntegracionSistemaTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user(
            username='usuario_integracion',
            password='clave-segura-prueba',
        )
        self.client.force_login(usuario)

    def _datos_estudiante(self, **cambios):
        datos = {
            'nombres': 'Ana',
            'apellidos': 'Prueba',
            'dni': '12345678',
            'correo': 'ana.prueba@example.com',
            'telefono': '999999999',
            'direccion': 'Av. Pruebas 123',
            'estado': Estudiante.ESTADO_ACTIVO,
        }
        datos.update(cambios)
        return datos

    def _registrar_datos_base(self):
        respuesta = self.client.post(
            reverse('estudiantes:crear_estudiante'),
            self._datos_estudiante(),
        )
        self.assertRedirects(
            respuesta,
            reverse('estudiantes:listar_estudiantes'),
        )
        estudiante = Estudiante.objects.get(dni='12345678')
        self.assertTrue(estudiante.codigo.startswith('EST-'))

        respuesta = self.client.post(
            reverse('academico:crear_materia'),
            {
                'nombre': 'Materia de Integracion',
                'descripcion': 'Materia utilizada en pruebas de integracion.',
                'creditos': '4',
            },
        )
        self.assertRedirects(
            respuesta,
            reverse('academico:listar_materias'),
        )
        materia = Materia.objects.get(nombre='Materia de Integracion')
        self.assertTrue(materia.codigo.startswith('MAT-'))

        respuesta = self.client.post(
            reverse('academico:crear_periodo'),
            {
                'nombre': '2026-I Integracion',
                'fecha_inicio': '2026-03-01',
                'fecha_fin': '2026-07-31',
            },
        )
        self.assertRedirects(
            respuesta,
            reverse('academico:listar_periodos'),
        )
        periodo = PeriodoAcademico.objects.get(nombre='2026-I Integracion')

        respuesta = self.client.post(
            reverse('academico:crear_matricula'),
            {
                'estudiante': estudiante.id,
                'materia': materia.id,
                'periodo': periodo.id,
            },
        )
        matricula = Matricula.objects.get(
            estudiante=estudiante,
            materia=materia,
            periodo=periodo,
        )
        self.assertRedirects(
            respuesta,
            reverse(
                'academico:detalle_matricula',
                args=[matricula.id],
            ),
        )

        respuesta = self.client.post(
            reverse('notas:crear_evaluacion'),
            {
                'materia': materia.id,
                'periodo': periodo.id,
                'nombre': 'Evaluacion de Integracion',
                'descripcion': 'Evaluacion utilizada en pruebas de integracion.',
                'peso': '50.00',
                'estado': Evaluacion.ESTADO_ACTIVO,
            },
        )
        self.assertRedirects(
            respuesta,
            reverse('notas:listar_evaluaciones'),
        )
        evaluacion = Evaluacion.objects.get(
            materia=materia,
            periodo=periodo,
        )

        return estudiante, materia, periodo, matricula, evaluacion

    def test_navegacion_principal_responde_correctamente(self):
        rutas = [
            'home',
            'estudiantes:listar_estudiantes',
            'academico:listar_materias',
            'academico:listar_periodos',
            'academico:listar_matriculas',
            'notas:listar_evaluaciones',
            'notas:listar_notas',
            'asistencia:listar_asistencias',
            'reportes:panel_reportes',
        ]

        for nombre_ruta in rutas:
            with self.subTest(ruta=nombre_ruta):
                respuesta = self.client.get(reverse(nombre_ruta))
                self.assertEqual(respuesta.status_code, 200)

    def test_flujo_completo_y_reportes(self):
        estudiante, materia, periodo, matricula, evaluacion = (
            self._registrar_datos_base()
        )

        respuesta = self.client.post(
            reverse('notas:registrar_nota'),
            {
                'matricula': matricula.id,
                'evaluacion': evaluacion.id,
                'calificacion': '16.00',
                'observacion': 'Nota de prueba de integración.',
            },
        )
        nota = Nota.objects.get(matricula=matricula, evaluacion=evaluacion)
        self.assertRedirects(
            respuesta,
            reverse('notas:detalle_nota', args=[nota.id]),
        )

        respuesta = self.client.post(
            reverse('asistencia:registrar_asistencia'),
            {
                'matricula': matricula.id,
                'fecha': '2026-04-15',
                'estado': Asistencia.ESTADO_PRESENTE,
                'observacion': 'Asistencia de prueba de integración.',
            },
        )
        asistencia = Asistencia.objects.get(matricula=matricula)
        self.assertRedirects(
            respuesta,
            reverse('asistencia:detalle_asistencia', args=[asistencia.id]),
        )

        reportes = [
            (
                reverse('reportes:reporte_estudiante', args=[estudiante.id]),
                'Materia de Integracion',
            ),
            (
                reverse(
                    'reportes:reporte_materia',
                    args=[materia.id, periodo.id],
                ),
                'Ana Prueba',
            ),
            (
                reverse('reportes:reporte_periodo', args=[periodo.id]),
                '2026-I Integracion',
            ),
        ]

        for ruta, contenido in reportes:
            with self.subTest(ruta=ruta):
                respuesta = self.client.get(ruta)
                self.assertEqual(respuesta.status_code, 200)
                self.assertContains(respuesta, contenido)

    def test_validaciones_de_datos_duplicados_y_fuera_de_rango(self):
        estudiante, materia, periodo, matricula, evaluacion = (
            self._registrar_datos_base()
        )

        respuesta = self.client.post(
            reverse('estudiantes:crear_estudiante'),
            self._datos_estudiante(
                correo='ana.duplicada@example.com',
            ),
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFormError(
            respuesta.context['form'],
            'dni',
            'Ya existe un estudiante registrado con este DNI.',
        )

        respuesta = self.client.post(
            reverse('notas:crear_evaluacion'),
            {
                'materia': materia.id,
                'periodo': periodo.id,
                'nombre': evaluacion.nombre,
                'descripcion': 'Intento de duplicado.',
                'peso': '50.00',
                'estado': Evaluacion.ESTADO_ACTIVO,
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(respuesta.context['form'].is_valid())

        respuesta = self.client.post(
            reverse('academico:crear_matricula'),
            {
                'estudiante': estudiante.id,
                'materia': materia.id,
                'periodo': periodo.id,
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFormError(
            respuesta.context['form'],
            'periodo',
            'El estudiante ya esta matriculado en esta materia y periodo.',
        )

        respuesta = self.client.post(
            reverse('notas:registrar_nota'),
            {
                'matricula': matricula.id,
                'evaluacion': evaluacion.id,
                'calificacion': '21.00',
                'observacion': '',
            },
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFormError(
            respuesta.context['form'],
            'calificacion',
            'La calificacion debe estar entre 0 y 20.',
        )

        datos_asistencia = {
            'matricula': matricula.id,
            'fecha': '2026-04-15',
            'estado': Asistencia.ESTADO_PRESENTE,
            'observacion': '',
        }
        respuesta = self.client.post(
            reverse('asistencia:registrar_asistencia'),
            datos_asistencia,
        )
        self.assertEqual(respuesta.status_code, 302)

        respuesta = self.client.post(
            reverse('asistencia:registrar_asistencia'),
            datos_asistencia,
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFormError(
            respuesta.context['form'],
            'fecha',
            'Ya existe asistencia registrada para esta matricula y fecha.',
        )

    def test_reportes_sin_datos_responden_correctamente(self):
        estudiante = Estudiante.objects.create(
            nombres='Sin',
            apellidos='Matricula',
            dni='87654321',
            correo='sin.matricula@example.com',
            telefono='988888888',
            direccion='Av. Sin Datos 100',
        )
        materia = Materia.objects.create(
            nombre='Materia sin matrículas',
            descripcion='Materia usada para reportes sin datos.',
            creditos=3,
        )
        periodo = PeriodoAcademico.objects.create(
            nombre='2026-II Sin Datos',
            fecha_inicio='2026-08-01',
            fecha_fin='2026-12-15',
        )

        casos = [
            (
                reverse('reportes:reporte_estudiante', args=[estudiante.id]),
                'El estudiante no tiene matrículas registradas.',
            ),
            (
                reverse(
                    'reportes:reporte_materia',
                    args=[materia.id, periodo.id],
                ),
                'No hay estudiantes matriculados en esta materia y periodo.',
            ),
            (
                reverse('reportes:reporte_periodo', args=[periodo.id]),
                'Este periodo no tiene matrículas registradas.',
            ),
        ]

        for ruta, mensaje in casos:
            with self.subTest(ruta=ruta):
                respuesta = self.client.get(ruta)
                self.assertEqual(respuesta.status_code, 200)
                self.assertContains(respuesta, mensaje)

    def test_selector_de_reporte_por_materia_redirige_al_reporte(self):
        estudiante, materia, periodo, matricula, evaluacion = (
            self._registrar_datos_base()
        )

        respuesta = self.client.post(
            reverse('reportes:panel_reportes'),
            {
                'materia': materia.id,
                'periodo': periodo.id,
            },
        )

        self.assertRedirects(
            respuesta,
            reverse(
                'reportes:reporte_materia',
                args=[materia.id, periodo.id],
            ),
        )
