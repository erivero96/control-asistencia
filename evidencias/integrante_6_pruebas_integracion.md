# Pruebas de Integración - Integrante 6

## Entorno de prueba

- Django 6.0.6.
- MySQL 8 ejecutado mediante Docker Compose.
- Base de datos temporal de MySQL usada únicamente durante la ejecución de las pruebas y eliminada al finalizar.

| Caso probado | Datos ingresados | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| Preparación de base de pruebas | Base temporal `test_control_academico_db`. | El usuario de Django debe poder usar una base aislada para ejecutar pruebas sin alterar los datos reales. | Inicialmente, `django_user` no tenía permiso para crear la base de pruebas. Se creó temporalmente con privilegios solo sobre esa base, se ejecutaron las pruebas y luego se eliminó. | Corregido |
| Inicio del servidor y configuración | `python manage.py check` y `python manage.py runserver 127.0.0.1:8001 --noreload` | Django inicia sin errores de configuración. | `check` no reportó incidencias y el servidor respondió con HTTP 200 en `http://127.0.0.1:8001/`. | Correcto |
| Navegación entre módulos | Enlaces de Inicio, Estudiantes, Materias, Periodos, Matrículas, Evaluaciones, Notas, Asistencia y Reportes. | Cada enlace resuelve una vista con respuesta HTTP 200. | Las nueve rutas respondieron con HTTP 200 mediante el cliente de pruebas de Django. | Correcto |
| Registro de estudiante | Código `EST-INT-001`, DNI `12345678`, Ana Prueba. | Se registra el estudiante y redirige a la lista. | Registro creado correctamente. | Correcto |
| Registro de materia | Código `MAT-INT-001`, 4 créditos, estado activo. | Se registra la materia y redirige a la lista. | Registro creado correctamente. | Correcto |
| Registro de periodo | `2026-I Integracion`, del 01/03/2026 al 31/07/2026. | Se registra el periodo y redirige a la lista. | Registro creado correctamente. | Correcto |
| Creación de matrícula | Estudiante Ana Prueba, materia de integración y periodo 2026-I. | Se crea la matrícula y se muestra su detalle. | Matrícula creada correctamente. | Correcto |
| Creación de evaluación | Evaluación de integración, peso 100 %. | Se crea la evaluación y redirige a la lista. | Evaluación creada correctamente. | Correcto |
| Registro de nota | Calificación `16.00`. | Se registra la nota y se muestra su detalle. | Nota creada correctamente. | Correcto |
| Registro de asistencia | Fecha 15/04/2026, estado presente. | Se registra la asistencia y se muestra su detalle. | Asistencia creada correctamente. | Correcto |
| Reportes con datos | Reportes del estudiante, materia-periodo y periodo creados. | Cada reporte muestra información asociada y responde HTTP 200. | Los tres reportes respondieron HTTP 200 con los datos de la prueba. | Correcto |
| DNI duplicado | Segundo estudiante con DNI `12345678`. | El formulario impide el registro y muestra el error de DNI único. | El formulario mostró el mensaje de DNI duplicado. | Correcto |
| Materia duplicada | Segunda materia con código `MAT-INT-001`. | El formulario impide el registro y muestra el error de código único. | El formulario mostró el mensaje de materia duplicada. | Correcto |
| Matrícula duplicada | Misma combinación estudiante, materia y periodo. | El formulario rechaza la matrícula repetida. | El formulario mostró el mensaje de matrícula duplicada. | Correcto |
| Nota fuera de rango | Calificación `21.00`. | El formulario rechaza valores fuera de 0 a 20. | El formulario mostró el mensaje de rango inválido. | Correcto |
| Asistencia duplicada | Misma matrícula y fecha 15/04/2026. | El formulario impide registrar una asistencia repetida. | El formulario mostró el mensaje de asistencia duplicada. | Correcto |
| Reportes sin datos | Estudiante, materia y periodo sin matrículas. | Los reportes responden y muestran un mensaje informativo. | Los tres reportes respondieron HTTP 200 con su mensaje correspondiente. | Correcto |

## Comando ejecutado

```bash
python manage.py test reportes -v 2 --keepdb
```
