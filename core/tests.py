from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class ProteccionDeVistasTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username='usuario_prueba',
            password='clave-segura-prueba',
        )

    def test_las_vistas_de_modulos_redirigen_al_login_sin_sesion(self):
        rutas_protegidas = [
            reverse('home'),
            reverse('estudiantes:listar_estudiantes'),
            reverse('estudiantes:crear_estudiante'),
            reverse('estudiantes:detalle_estudiante', args=[999]),
            reverse('estudiantes:editar_estudiante', args=[999]),
            reverse('estudiantes:desactivar_estudiante', args=[999]),
            reverse('academico:index'),
            reverse('academico:listar_materias'),
            reverse('academico:crear_materia'),
            reverse('academico:editar_materia', args=[999]),
            reverse('academico:desactivar_materia', args=[999]),
            reverse('academico:listar_periodos'),
            reverse('academico:crear_periodo'),
            reverse('academico:editar_periodo', args=[999]),
            reverse('academico:listar_matriculas'),
            reverse('academico:crear_matricula'),
            reverse('academico:detalle_matricula', args=[999]),
            reverse('academico:retirar_matricula', args=[999]),
            reverse('notas:listar_notas'),
            reverse('notas:registrar_nota'),
            reverse('notas:detalle_nota', args=[999]),
            reverse('notas:editar_nota', args=[999]),
            reverse('notas:notas_por_estudiante', args=[999]),
            reverse('notas:notas_por_materia', args=[999]),
            reverse('notas:listar_evaluaciones'),
            reverse('notas:crear_evaluacion'),
            reverse('notas:editar_evaluacion', args=[999]),
            reverse('notas:desactivar_evaluacion', args=[999]),
            reverse('notas:promedio_matricula', args=[999]),
            reverse('notas:promedios_por_materia', args=[999]),
            reverse('asistencia:listar_asistencias'),
            reverse('asistencia:registrar_asistencia'),
            reverse('asistencia:registrar_asistencia_por_materia'),
            reverse('asistencia:asistencias_por_estudiante', args=[999]),
            reverse('asistencia:asistencias_por_materia', args=[999]),
            reverse('asistencia:porcentaje_asistencia_matricula', args=[999]),
            reverse('asistencia:porcentajes_por_materia', args=[999]),
            reverse('asistencia:detalle_asistencia', args=[999]),
            reverse('asistencia:editar_asistencia', args=[999]),
            reverse('reportes:panel_reportes'),
            reverse('reportes:reporte_estudiante', args=[999]),
            reverse('reportes:reporte_materia', args=[999, 999]),
            reverse('reportes:reporte_periodo', args=[999]),
        ]
        url_login = reverse('login')

        for ruta in rutas_protegidas:
            with self.subTest(ruta=ruta):
                respuesta = self.client.get(ruta)

                self.assertRedirects(
                    respuesta,
                    f'{url_login}?next={ruta}',
                    fetch_redirect_response=False,
                )

    def test_post_sin_sesion_no_accede_a_vista_de_escritura(self):
        ruta = reverse('estudiantes:crear_estudiante')

        respuesta = self.client.post(ruta, {})

        self.assertRedirects(
            respuesta,
            f'{reverse("login")}?next={ruta}',
            fetch_redirect_response=False,
        )

    def test_login_crea_sesion_y_permite_acceder_a_un_modulo(self):
        destino = reverse('asistencia:listar_asistencias')

        respuesta = self.client.post(
            reverse('login'),
            {
                'username': self.usuario.username,
                'password': 'clave-segura-prueba',
                'next': destino,
            },
        )

        self.assertRedirects(
            respuesta,
            destino,
            fetch_redirect_response=False,
        )
        self.assertIn('_auth_user_id', self.client.session)
        respuesta_destino = self.client.get(destino)
        self.assertEqual(respuesta_destino.status_code, 200)
        self.assertContains(
            respuesta_destino,
            f'Bienvenido, {self.usuario.username}.',
        )
        self.assertContains(respuesta_destino, self.usuario.username)
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)

    def test_login_incorrecto_no_crea_una_sesion(self):
        respuesta = self.client.post(
            reverse('login'),
            {
                'username': self.usuario.username,
                'password': 'clave-incorrecta',
            },
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'No se pudo iniciar sesión.')
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_elimina_la_sesion_y_vuelve_al_login(self):
        self.client.force_login(self.usuario)

        respuesta = self.client.post(reverse('logout'))

        self.assertRedirects(
            respuesta,
            reverse('login'),
            fetch_redirect_response=False,
        )
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertRedirects(
            self.client.get(reverse('home')),
            f'{reverse("login")}?next={reverse("home")}',
            fetch_redirect_response=False,
        )
        self.assertContains(
            self.client.get(reverse('login')),
            'Sesión cerrada correctamente.',
        )

    def test_login_es_accesible_sin_sesion(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)

    def test_configuracion_de_sesion_esta_activa(self):
        self.assertIn(
            'django.contrib.sessions.middleware.SessionMiddleware',
            settings.MIDDLEWARE,
        )
        self.assertIn(
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            settings.MIDDLEWARE,
        )
        self.assertEqual(settings.SESSION_COOKIE_AGE, 60 * 60 * 8)
        self.assertTrue(settings.SESSION_EXPIRE_AT_BROWSER_CLOSE)

# Create your tests here.
