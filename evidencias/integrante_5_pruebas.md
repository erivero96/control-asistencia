# Evidencias de pruebas - Integrante 5

## Subfase 5.8 - Pruebas del modulo de asistencia

### Datos base usados

- Estudiante: `T5A001 - Prueba Asistencia Uno`
- Materia con estudiantes: `T5-ASIS - Materia Prueba Asistencia`
- Materia sin estudiantes: `T5-VACIA - Materia Sin Estudiantes T5`
- Periodo academico: `Periodo Prueba Asistencia 2026`
- Matricula: estudiante `T5A001` en materia `T5-ASIS` y periodo `Periodo Prueba Asistencia 2026`
- Fechas usadas: `2026-06-10`, `2026-06-11`, `2026-06-12`, `2026-06-13`, `2026-06-14`

## Casos probados

| Caso probado | Datos ingresados | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| Servidor Django sin errores | Comando `.venv/bin/python manage.py runserver 127.0.0.1:8000 --noreload` y visita a `/asistencia/` | El servidor inicia y la ruta responde correctamente | Servidor iniciado sin errores y `/asistencia/` respondio `200 OK` | Correcto |
| Registro de asistencia individual | Matricula `T5A001/T5-ASIS`, fecha `2026-06-10`, estado `presente` | Se crea una asistencia y redirige al detalle | La asistencia se creo y la vista respondio con redireccion `302` | Correcto |
| Error por asistencia duplicada | Misma matricula y fecha `2026-06-10` con otro estado | El formulario debe rechazar el registro duplicado | `AsistenciaForm` fue invalido y mostro error en el campo `fecha` | Correcto |
| Edicion de asistencia | Asistencia del `2026-06-10`, cambio de `presente` a `tardanza` | El registro existente se actualiza sin duplicarse | La asistencia cambio a `tardanza` y la vista redirigio correctamente | Correcto |
| Consulta por estudiante | Ruta `/asistencia/estudiante/<id>/` para estudiante `T5A001` | La vista carga las asistencias del estudiante | La vista respondio `200 OK` | Correcto |
| Consulta por materia | Ruta `/asistencia/materia/<id>/` para materia `T5-ASIS` | La vista carga las asistencias de la materia | La vista respondio `200 OK` | Correcto |
| Registro de asistencia por materia | Materia `T5-ASIS`, periodo de prueba, fecha `2026-06-11`, estado `justificado` | Se crea asistencia para la matricula activa | Se creo asistencia para la matricula del estudiante | Correcto |
| Actualizacion por materia sin duplicar | Misma materia, periodo y fecha `2026-06-11`, cambio a `falta` | Debe actualizar el registro existente sin crear duplicado | El estado se actualizo y quedo un solo registro para matricula y fecha | Correcto |
| Materia sin estudiantes matriculados | Materia `T5-VACIA`, periodo de prueba, fecha `2026-06-12` | La vista debe cargar y mostrar mensaje de que no hay estudiantes | La vista respondio `200 OK` y no encontro matriculas para esa materia | Correcto |
| Calculo de total de clases | Cinco asistencias registradas para la matricula de prueba | Total de clases debe ser `5` | La funcion retorno `5` | Correcto |
| Presente cuenta como asistencia valida | Estado `presente` en una fecha de prueba | Debe sumarse como asistencia valida | El conteo de presentes fue correcto | Correcto |
| Tardanza cuenta como asistencia valida | Estados `tardanza` en fechas de prueba | Deben sumarse como asistencia valida | El conteo de tardanzas fue correcto | Correcto |
| Justificado cuenta como asistencia valida | Estado `justificado` en una fecha de prueba | Debe sumarse como asistencia valida | El conteo de justificados fue correcto | Correcto |
| Falta cuenta como inasistencia | Estado `falta` en una fecha de prueba | Debe contarse como falta y no como asistencia valida | El conteo de faltas fue correcto | Correcto |
| Porcentaje de asistencia | 5 clases: 4 validas y 1 falta | Porcentaje esperado `80.00%` | La funcion retorno `80.00` | Correcto |
| Vista porcentaje por matricula | Ruta `/asistencia/porcentaje/matricula/<id>/` | La vista debe mostrar totales y porcentaje | La vista respondio `200 OK` | Correcto |
| Vista porcentajes por materia | Ruta `/asistencia/porcentajes/materia/<id>/` | La vista debe mostrar tabla de porcentajes por materia | La vista respondio `200 OK` | Correcto |

## Comandos ejecutados

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py runserver 127.0.0.1:8000 --noreload
curl -I http://127.0.0.1:8000/asistencia/
```

## Resultado de validacion automatizada

```text
System check identified no issues (0 silenced).
HTTP/1.1 200 OK
PRUEBAS_ASISTENCIA_COMPLETADAS
```

## Errores comunes y solucion

- Si aparece error de conexion a MySQL, levantar la base de datos con `docker compose up -d mysql`.
- Si Django no importa, activar el entorno virtual o usar `.venv/bin/python`.
- Si aparece error de asistencia duplicada, verificar que no exista un registro con la misma matricula y fecha.
- Si una pagina de detalle devuelve 404, confirmar que el ID exista en la base de datos.
- Si el porcentaje aparece como pendiente, verificar que la matricula tenga asistencias registradas.
- Si el registro por materia no lista estudiantes, confirmar que existan matriculas activas para esa materia y periodo.

## Subfase 5.9 - Sesiones y protección de vistas

| Caso probado | Resultado obtenido | Estado |
| --- | --- | --- |
| Acceso sin sesión a Inicio, Estudiantes, Académico, Notas, Asistencia y Reportes | Las 43 rutas protegidas se redirigieron a `cuentas/login/` con el parámetro `next`. | Correcto |
| POST sin sesión a una vista de creación | La solicitud a crear estudiante fue redirigida al login, sin ejecutar la vista de escritura. | Correcto |
| Inicio de sesión | Las credenciales válidas crearon la sesión y permitieron acceder al módulo de asistencia. | Correcto |
| Cierre de sesión | La sesión se eliminó y la respuesta redirigió a la pantalla de login. | Correcto |
| Integración autenticada | Los cuatro flujos existentes de navegación, registro, validaciones y reportes continuaron funcionando con usuario autenticado. | Correcto |

### Comandos ejecutados

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py test core reportes --keepdb --verbosity 2
```

### Resultado

```text
System check identified no issues (0 silenced).
Ran 9 tests
OK
```

## Subfase 5.10 - Manejo básico de sesiones

| Caso probado | Resultado obtenido | Estado |
| --- | --- | --- |
| Middleware de sesión y autenticación | `SessionMiddleware` y `AuthenticationMiddleware` permanecen activos en la configuración. | Correcto |
| Inicio de sesión | Se crea la sesión, se muestra el mensaje de bienvenida y el nombre del usuario en el menú. | Correcto |
| Cierre de sesión | La sesión se elimina, se muestra el mensaje de cierre y el usuario no puede volver al inicio protegido. | Correcto |
| Duración de sesión | La configuración establece un máximo de ocho horas y caducidad al cerrar el navegador. | Correcto |
