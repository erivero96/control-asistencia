# Pruebas de integracion - Modulo de reportes

## Caso 1: Acceso al panel de reportes

- **Caso probado**: Entrar a `/reportes/` con sesion iniciada.
- **Datos ingresados / condicion probada**: Usuario autenticado.
- **Resultado esperado**: Se muestra el panel con las cinco tarjetas (reporte por estudiante, materia, periodo, resumen de notas, resumen de asistencia).
- **Resultado obtenido**: El panel carga correctamente con las 5 tarjetas y enlaces funcionales.
- **Estado**: correcto

## Caso 2: Reporte por estudiante con datos

- **Caso probado**: Acceder a `/reportes/estudiante/<id>/` de un estudiante con matriculas, notas y asistencias registradas.
- **Datos ingresados / condicion probada**: Estudiante con al menos una matricula con notas y asistencias.
- **Resultado esperado**: Se muestran datos del estudiante (codigo, nombres, DNI, correo), materias matriculadas con periodo, notas por evaluacion, promedio, estado academico y resumen de asistencia.
- **Resultado obtenido**: Todos los datos se muestran correctamente, incluyendo promedios y porcentajes de asistencia.
- **Estado**: correcto

## Caso 3: Reporte por estudiante sin matriculas

- **Caso probado**: Acceder al reporte de un estudiante que no tiene matriculas registradas.
- **Datos ingresados / condicion probada**: Estudiante sin registro en el modelo Matricula.
- **Resultado esperado**: Se muestran los datos del estudiante y el mensaje "El estudiante no tiene matriculas registradas."
- **Resultado obtenido**: Se muestra el mensaje esperado correctamente.
- **Estado**: correcto

## Caso 4: Reporte por estudiante sin notas

- **Caso probado**: Acceder al reporte de un estudiante con matricula pero sin notas registradas.
- **Datos ingresados / condicion probada**: Estudiante con al menos una matricula sin notas asociadas.
- **Resultado esperado**: Para cada materia se muestra "No hay notas registradas para esta materia." y el promedio aparece como "Pendiente".
- **Resultado obtenido**: Mensajes y estado "Pendiente" mostrados correctamente.
- **Estado**: correcto

## Caso 5: Reporte por estudiante sin asistencias

- **Caso probado**: Acceder al reporte de un estudiante con matricula pero sin asistencias.
- **Datos ingresados / condicion probada**: Estudiante con al menos una matricula sin registros de asistencia.
- **Resultado esperado**: Se muestra "No hay asistencias registradas para esta materia."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 6: Reporte por estudiante inexistente

- **Caso probado**: Acceder a `/reportes/estudiante/99999/` con un ID que no existe.
- **Datos ingresados / condicion probada**: ID de estudiante inexistente.
- **Resultado esperado**: Django devuelve error 404 (Page not found).
- **Resultado obtenido**: Error 404 mostrado correctamente mediante `get_object_or_404`.
- **Estado**: correcto

## Caso 7: Reporte por materia con datos

- **Caso probado**: Acceder a `/reportes/materia/<materia_id>/periodo/<periodo_id>/` con materia y periodo que tienen matriculas, notas y asistencias.
- **Datos ingresados / condicion probada**: Materia y periodo con al menos una matricula activa, notas y asistencias.
- **Resultado esperado**: Se muestran datos de la materia y periodo, resumen academico con aprobados/desaprobados/pendientes, resumen de asistencia, y tabla de estudiantes matriculados con notas, promedio y estado.
- **Resultado obtenido**: Todos los datos mostrados correctamente en la tabla y secciones de resumen.
- **Estado**: correcto

## Caso 8: Reporte por materia sin matriculas

- **Caso probado**: Acceder al reporte de una materia y periodo que no tienen estudiantes matriculados.
- **Datos ingresados / condicion probada**: Materia y periodo validos pero sin matriculas.
- **Resultado esperado**: Se muestran datos de materia y periodo, y el mensaje "No hay estudiantes matriculados en esta materia y periodo."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 9: Reporte por materia sin asistencias

- **Caso probado**: Acceder al reporte de una materia y periodo con matriculas pero sin asistencias.
- **Datos ingresados / condicion probada**: Materia y periodo con matriculas pero sin registros de asistencia.
- **Resultado esperado**: Se muestra "No hay asistencias registradas para esta materia y periodo."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 10: Reporte por materia con parametros inexistentes

- **Caso probado**: Acceder a `/reportes/materia/99999/periodo/99999/` con IDs inexistentes.
- **Datos ingresados / condicion probada**: IDs de materia o periodo inexistentes.
- **Resultado esperado**: Django devuelve error 404.
- **Resultado obtenido**: Error 404 mostrado correctamente.
- **Estado**: correcto

## Caso 11: Reporte por periodo con datos

- **Caso probado**: Acceder a `/reportes/periodo/<periodo_id>/` de un periodo con matriculas, notas y asistencias.
- **Datos ingresados / condicion probada**: Periodo con al menos una matricula.
- **Resultado esperado**: Se muestran datos del periodo, indicadores de matricula (total estudiantes, materias activas, total matriculas), resumen de notas (total y promedio general) y resumen de asistencias (desglose por estado).
- **Resultado obtenido**: Todos los indicadores cargan correctamente.
- **Estado**: correcto

## Caso 12: Reporte por periodo sin matriculas

- **Caso probado**: Acceder al reporte de un periodo sin matriculas registradas.
- **Datos ingresados / condicion probada**: Periodo valido pero sin matriculas.
- **Resultado esperado**: Se muestran datos del periodo y el mensaje "Este periodo no tiene matriculas registradas."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 13: Reporte por periodo sin notas

- **Caso probado**: Acceder al reporte de un periodo con matriculas pero sin notas.
- **Datos ingresados / condicion probada**: Periodo con matriculas pero sin registros de notas.
- **Resultado esperado**: En la seccion de notas se muestra "No hay notas registradas en este periodo."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 14: Reporte por periodo sin asistencias

- **Caso probado**: Acceder al reporte de un periodo con matriculas pero sin asistencias.
- **Datos ingresados / condicion probada**: Periodo con matriculas pero sin registros de asistencia.
- **Resultado esperado**: En la seccion de asistencia se muestra "No hay asistencias registradas en este periodo."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 15: Reporte por periodo inexistente

- **Caso probado**: Acceder a `/reportes/periodo/99999/` con un ID inexistente.
- **Datos ingresados / condicion probada**: ID de periodo inexistente.
- **Resultado esperado**: Django devuelve error 404.
- **Resultado obtenido**: Error 404 mostrado correctamente.
- **Estado**: correcto

## Caso 16: Resumen de notas con datos

- **Caso probado**: Acceder a `/reportes/resumen-notas/` con evaluaciones y notas registradas.
- **Datos ingresados / condicion probada**: Al menos una evaluacion y notas registradas en el sistema.
- **Resultado esperado**: Se muestran indicadores (total evaluaciones, total notas, promedio general, aprobados, desaprobados) y tabla de estudiantes con promedio.
- **Resultado obtenido**: Indicadores y tabla cargan correctamente con promedios calculados y estados.
- **Estado**: correcto

## Caso 17: Resumen de notas sin datos

- **Caso probado**: Acceder a `/reportes/resumen-notas/` cuando no existen notas registradas.
- **Datos ingresados / condicion probada**: Sistema sin registros en el modelo Nota.
- **Resultado esperado**: Promedio general muestra "No hay notas registradas." y la tabla muestra "No hay notas registradas para ningun estudiante."
- **Resultado obtenido**: Mensajes mostrados correctamente. Aprobados y desaprobados en 0.
- **Estado**: correcto

## Caso 18: Resumen de asistencia con datos

- **Caso probado**: Acceder a `/reportes/resumen-asistencia/` con registros de asistencia.
- **Datos ingresados / condicion probada**: Al menos un registro de asistencia en el sistema.
- **Resultado esperado**: Se muestran total de registros, presentes, tardanzas, faltas, justificados y porcentaje general calculado como (presentes + tardanzas + justificados) / total * 100.
- **Resultado obtenido**: Indicadores y porcentaje mostrados correctamente.
- **Estado**: correcto

## Caso 19: Resumen de asistencia sin datos

- **Caso probado**: Acceder a `/reportes/resumen-asistencia/` sin registros de asistencia.
- **Datos ingresados / condicion probada**: Sistema sin registros en el modelo Asistencia.
- **Resultado esperado**: Se muestra "No hay registros de asistencia en el sistema."
- **Resultado obtenido**: Mensaje mostrado correctamente.
- **Estado**: correcto

## Caso 20: Verificacion de extension de base.html

- **Caso probado**: Revisar que los 6 templates de reportes extiendan `base.html`.
- **Datos ingresados / condicion probada**: Archivos en `templates/reportes/`.
- **Resultado esperado**: Todos contienen `{% extends 'base.html' %}` en la primera linea.
- **Resultado obtenido**: Los 6 templates (panel_reportes, reporte_estudiante, reporte_materia, reporte_periodo, resumen_notas, resumen_asistencia) extienden base.html correctamente.
- **Estado**: correcto

## Caso 21: Navegacion desde panel de reportes

- **Caso probado**: Verificar que los 5 enlaces del panel de reportes dirijan a destinos validos.
- **Datos ingresados / condicion probada**: Clic en cada tarjeta del panel.
- **Resultado esperado**: Cada enlace redirige a la ruta correcta sin errores.
- **Resultado obtenido**:
  - Reporte por estudiante -> `estudiantes:listar_estudiantes` (correcto)
  - Reporte por materia -> `academico:listar_materias` (correcto)
  - Reporte por periodo -> `academico:listar_periodos` (correcto)
  - Resumen de notas -> `reportes:resumen_notas` (correcto)
  - Resumen de asistencia -> `reportes:resumen_asistencia` (correcto)
- **Estado**: correcto

## Caso 22: Proteccion de vistas con login_required

- **Caso probado**: Intentar acceder a cualquier ruta de reportes sin sesion iniciada.
- **Datos ingresados / condicion probada**: Usuario no autenticado.
- **Resultado esperado**: Redireccion a la pagina de login con parametro `next`.
- **Resultado obtenido**: Todas las vistas redirigen al login correctamente.
- **Estado**: correcto

## Caso 23: Consistencia de titulos de pagina

- **Caso probado**: Revisar que todos los titulos de template usen "Control Academico" con tilde en la segunda "e".
- **Datos ingresados / condicion probada**: Archivos HTML en `templates/reportes/`.
- **Resultado esperado**: Todos los titulos muestran "Control Academico".
- **Resultado obtenido**: Se detecto que `resumen_asistencia.html` tenia "Control Academico" sin tilde. Se corrigio a "Control Academico".
- **Estado**: corregido

## Caso 24: Validacion del proyecto con manage.py check

- **Caso probado**: Ejecutar `python manage.py check`.
- **Datos ingresados / condicion probada**: Proyecto completo con todos los modulos.
- **Resultado esperado**: "System check identified no issues (0 silenced)."
- **Resultado obtenido**: Sin errores detectados.
- **Estado**: correcto
