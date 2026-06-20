# Evidencias de pruebas de autenticación - Integrante 5

## Subfase 5.11 - Login, logout y protección de sesiones

### Datos de prueba

- Usuario válido: `usuario_prueba`.
- Contraseña válida: `clave-segura-prueba`.
- Contraseña incorrecta: `clave-incorrecta`.
- Rutas protegidas verificadas: `/`, `/estudiantes/`, `/academico/`, `/notas/`, `/asistencia/` y `/reportes/`.

## Casos probados

| Caso probado | Datos usados | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| Acceso sin iniciar sesión | GET a `/` y a los módulos protegidos sin cookie de sesión | Redirección a `/cuentas/login/` con `next` | Las 43 rutas protegidas redirigieron al login y conservaron la ruta solicitada. | Correcto |
| Redirección automática al login | GET a `/asistencia/` sin sesión | Mostrar login con `next=/asistencia/` | Respuesta `302` a `/cuentas/login/?next=/asistencia/`. | Correcto |
| Login correcto | `usuario_prueba` y `clave-segura-prueba` | Crear sesión, redirigir al destino y mostrar bienvenida | Se creó `_auth_user_id`, se accedió al módulo y se mostró el mensaje de bienvenida. | Correcto |
| Login incorrecto | `usuario_prueba` y `clave-incorrecta` | Mantenerse en login, mostrar error y no crear sesión | Respuesta `200`, mensaje de error y ausencia de `_auth_user_id`. | Correcto |
| Acceso a módulos con sesión | Usuario válido autenticado | Cargar Inicio y módulos protegidos | Inicio y Asistencia respondieron `200 OK`; el menú mostró el usuario autenticado. | Correcto |
| Cierre de sesión | POST a `/cuentas/logout/` con usuario autenticado | Eliminar sesión, redirigir al login y mostrar confirmación | Se eliminó `_auth_user_id`, se redirigió al login y se mostró el mensaje de cierre. | Correcto |
| Bloqueo después del logout | GET a `/` tras cerrar sesión | Redirigir otra vez al login | Respuesta `302` a `/cuentas/login/?next=/`. | Correcto |

## Comandos ejecutados

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py test --keepdb --verbosity 2
```

## Resultado de validación

```text
System check identified no issues (0 silenced).
Ran 11 tests
OK
```

## Errores comunes y cómo corregirlos

- Si una ruta protegida responde `200` sin sesión, verificar que conserve `@login_required` y que `LOGIN_URL = 'login'` esté configurado.
- Si el usuario no aparece en el menú, comprobar `AuthenticationMiddleware`, el procesador de contexto `django.contrib.auth.context_processors.auth` y que la solicitud tenga una sesión válida.
- Si el logout no bloquea el acceso posterior, verificar que se envíe por POST y que la vista protegida use `@login_required`.
- Si no aparece un mensaje de login o logout, comprobar `MessageMiddleware`, el procesador `django.contrib.messages.context_processors.messages` y el bloque `{% if messages %}` de `base.html`.
- Si las pruebas no conectan a MySQL, levantar el contenedor con `docker compose up -d mysql`.
