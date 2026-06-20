# Evidencias - Integrante 5

## Subfase 5.1

### Prompt usado

```text
Desarrolla la subfase 5.1 del proyecto.

Necesito crear el modelo Asistencia para el sistema web de Control Academico en Django.

Requisitos:
- Trabajar en la app asistencia.
- Usar el modelo Matricula de la app academico.
- Crear el modelo Asistencia.
- Campos:
  - matricula
  - fecha
  - estado
  - observacion
  - fecha_registro
- El estado debe permitir:
  - presente
  - tardanza
  - falta
  - justificado
- Evitar que se registre asistencia duplicada para la misma matricula y fecha.
- Registrar el modelo en admin.py.
- En el admin mostrar estudiante, materia, periodo, fecha y estado.
- Permitir busqueda por estudiante y materia.
- Crear y ejecutar migraciones.
- No crear todavia vistas ni formularios.

Quiero que me indiques:
1. Archivos que se deben modificar.
2. Codigo completo del modelo Asistencia.
3. Codigo completo o actualizado de admin.py.
4. Como se evita la asistencia duplicada.
5. Comandos para crear y ejecutar migraciones.
6. Comando para probar que no hay errores.
7. Mensaje de commit recomendado.
8. Breve explicacion para defensa.

Tambien crea o actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.1
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `Asistencia` dentro de la app `asistencia`, relacionado con `Matricula` de la app `academico`. El modelo permite registrar la asistencia de un estudiante matriculado en una materia y periodo para una fecha especifica, manejar los estados presente, tardanza, falta y justificado, guardar observaciones y registrar automaticamente la fecha de creacion.

### Cambios realizados

- Se creo el modelo `Asistencia` en `asistencia/models.py`.
- Se relaciono `Asistencia` con `Matricula` mediante una llave foranea protegida.
- Se agregaron los campos `fecha`, `estado`, `observacion` y `fecha_registro`.
- Se configuro `estado` con las opciones `presente`, `tardanza`, `falta` y `justificado`.
- Se agrego una restriccion unica para evitar asistencias duplicadas por matricula y fecha.
- Se registro `Asistencia` en `asistencia/admin.py`.
- Se configuro el admin para mostrar estudiante, materia, periodo, fecha y estado.
- Se habilito busqueda por codigo, nombres y apellidos del estudiante, ademas de codigo y nombre de la materia.
- Se genero y aplico la migracion inicial de la app `asistencia`.
- No se crearon vistas ni formularios en esta subfase.

## Subfase 5.2

### Prompt usado

```text
Desarrolla la subfase 5.2 del proyecto.

Necesito crear formularios para el modulo de asistencia.

Requisitos:
- Trabajar en la app asistencia.
- Crear archivo forms.py si no existe.
- Crear AsistenciaForm usando ModelForm.
- Campos:
  - matricula
  - fecha
  - estado
  - observacion
- Validar que la matricula sea obligatoria.
- Validar que la fecha sea obligatoria.
- Validar que el estado sea obligatorio.
- Validar que no exista asistencia duplicada para la misma matricula y fecha.
- Mostrar mensajes de error claros.
- No tocar reportes generales.

Quiero que me indiques:
1. Codigo completo de forms.py.
2. Validaciones incluidas.
3. Como funciona el formulario.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.2
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo `AsistenciaForm` dentro de `asistencia/forms.py` usando `ModelForm`. El formulario permite capturar matricula, fecha, estado y observacion, con mensajes claros para campos obligatorios y una validacion para evitar duplicar asistencia en la misma matricula y fecha.

### Cambios realizados

- Se creo el archivo `asistencia/forms.py`.
- Se creo `AsistenciaForm` basado en el modelo `Asistencia`.
- Se limitaron los campos del formulario a `matricula`, `fecha`, `estado` y `observacion`.
- Se agregaron etiquetas y mensajes de error claros para el usuario.
- Se valido que `matricula`, `fecha` y `estado` sean obligatorios.
- Se agrego validacion de duplicidad por `matricula` y `fecha`.
- Se configuro el campo `fecha` con widget de tipo fecha.
- Se configuro `observacion` como area de texto de tres filas.
- No se tocaron reportes generales.

## Subfase 5.3

### Prompt usado

```text
Desarrolla la subfase 5.3 del proyecto.

Necesito crear las vistas principales del modulo de asistencia en Django.

Requisitos:
- Trabajar en la app asistencia.
- Crear vistas para:
  - listar_asistencias
  - registrar_asistencia
  - editar_asistencia
  - detalle_asistencia
  - asistencias_por_estudiante
  - asistencias_por_materia
- Usar AsistenciaForm.
- Usar django.contrib.messages.
- Validar que no exista asistencia duplicada.
- Mostrar informacion relacionada:
  - estudiante
  - materia
  - periodo
  - fecha
  - estado
- Ordenar asistencia por fecha descendente.
- No desarrollar reportes generales.

Quiero que me indiques:
1. Codigo completo de views.py.
2. Explicacion de cada vista.
3. Validaciones aplicadas.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.3
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon las vistas principales del modulo `asistencia` para listar, registrar, editar, detallar y consultar asistencias por estudiante o por materia. Las vistas usan `AsistenciaForm`, mensajes de Django y consultas con relaciones hacia estudiante, materia y periodo.

### Cambios realizados

- Se actualizo `asistencia/views.py`.
- Se agrego la vista `listar_asistencias`.
- Se agrego la vista `registrar_asistencia`.
- Se agrego la vista `editar_asistencia`.
- Se agrego la vista `detalle_asistencia`.
- Se agrego la vista `asistencias_por_estudiante`.
- Se agrego la vista `asistencias_por_materia`.
- Se uso `AsistenciaForm` para registrar y editar asistencias.
- Se usaron mensajes de exito y error con `django.contrib.messages`.
- Se reutilizo la validacion de `AsistenciaForm` para evitar asistencias duplicadas por matricula y fecha.
- Se incluyo informacion relacionada de estudiante, materia, periodo, fecha y estado mediante consultas con `select_related`.
- Se ordenaron las asistencias por fecha descendente.
- No se desarrollaron reportes generales.

## Subfase 5.4

### Prompt usado

```text
Desarrolla la subfase 5.4 del proyecto.

Necesito una funcion/vista para registrar asistencia por materia, periodo y fecha.

Requisitos:
- Trabajar en la app asistencia.
- Crear vista registrar_asistencia_por_materia.
- El usuario debe seleccionar:
  - materia
  - periodo
  - fecha
- El sistema debe listar las matriculas activas de esa materia y periodo.
- Para cada estudiante debe permitir marcar:
  - presente
  - tardanza
  - falta
  - justificado
- Al guardar, debe crear o actualizar la asistencia de cada matricula para esa fecha.
- No debe duplicar registros.
- Debe mostrar mensaje de exito.
- Debe manejar el caso donde no haya estudiantes matriculados.

Quiero que me indiques:
1. Codigo completo de la vista.
2. Si se necesita un formulario adicional, mostrarlo completo.
3. Como se evita duplicar asistencia.
4. Como se actualiza una asistencia existente.
5. Comando para probar que no hay errores.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.4
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo la vista `registrar_asistencia_por_materia` para seleccionar materia, periodo y fecha, listar las matriculas activas correspondientes y registrar la asistencia de todos los estudiantes en una sola operacion. Tambien se creo un formulario adicional para capturar los criterios de seleccion.

### Cambios realizados

- Se actualizo `asistencia/forms.py`.
- Se creo `AsistenciaPorMateriaForm` para seleccionar materia, periodo academico y fecha.
- Se actualizo `asistencia/views.py`.
- Se agrego la vista `registrar_asistencia_por_materia`.
- Se agrego una consulta auxiliar para obtener matriculas activas por materia y periodo.
- Se agrego una estructura auxiliar para mostrar cada estudiante con su estado de asistencia actual.
- Se permitio marcar presente, tardanza, falta o justificado por cada matricula.
- Se uso `update_or_create` para crear o actualizar asistencia por matricula y fecha sin duplicar registros.
- Se uso `transaction.atomic()` para guardar la asistencia de todos los estudiantes como una sola operacion.
- Se agrego mensaje de exito al guardar correctamente.
- Se manejo el caso donde no existen estudiantes matriculados en la materia y periodo seleccionados.

## Subfase 5.5

### Prompt usado

```text
Desarrolla la subfase 5.5 del proyecto.

Necesito agregar el calculo de porcentaje de asistencia.

Requisitos:
- Trabajar en la app asistencia.
- Crear funciones auxiliares para:
  - total de clases registradas por matricula
  - total de presentes
  - total de tardanzas
  - total de faltas
  - total de justificados
  - porcentaje de asistencia
- Considerar presente, tardanza y justificado como asistencia valida.
- Considerar falta como inasistencia.
- Si no hay registros, mostrar porcentaje pendiente o 0%.
- Crear vista porcentaje_asistencia_matricula.
- Crear vista porcentajes_por_materia.
- Mostrar:
  - estudiante
  - materia
  - periodo
  - total de clases
  - presentes
  - tardanzas
  - faltas
  - justificados
  - porcentaje

Quiero que me indiques:
1. Codigo completo de las funciones auxiliares.
2. Codigo actualizado de views.py.
3. Explicacion del calculo usado.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.5
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se agregaron funciones auxiliares para calcular totales de asistencia por matricula y el porcentaje de asistencia. Tambien se crearon vistas para consultar el porcentaje de una matricula especifica y los porcentajes de todas las matriculas de una materia.

### Cambios realizados

- Se creo `asistencia/utils.py`.
- Se agrego el calculo de total de clases registradas por matricula.
- Se agregaron funciones para contar presentes, tardanzas, faltas y justificados.
- Se agrego el calculo de porcentaje considerando presente, tardanza y justificado como asistencia valida.
- Se configuro el resultado como `pendiente` cuando una matricula no tiene registros de asistencia.
- Se agrego una funcion de resumen para entregar estudiante, materia, periodo, totales y porcentaje.
- Se actualizo `asistencia/views.py`.
- Se agrego la vista `porcentaje_asistencia_matricula`.
- Se agrego la vista `porcentajes_por_materia`.
- No se desarrollaron reportes generales.

## Subfase 5.6

### Prompt usado

```text
Desarrolla la subfase 5.6 del proyecto.

Necesito configurar las rutas del modulo asistencia.

Requisitos:
- Trabajar en asistencia/urls.py.
- Crear rutas para:
  - /asistencia/
  - /asistencia/registrar/
  - /asistencia/<id>/
  - /asistencia/<id>/editar/
  - /asistencia/estudiante/<id>/
  - /asistencia/materia/<id>/
  - /asistencia/registrar-por-materia/
  - /asistencia/porcentaje/matricula/<id>/
  - /asistencia/porcentajes/materia/<id>/
- Verificar que config/urls.py incluya las rutas de asistencia.
- Usar nombres de rutas claros.

Quiero que me indiques:
1. Codigo completo de asistencia/urls.py.
2. Si se modifica config/urls.py, mostrar el codigo necesario.
3. Explicacion de cada ruta.
4. Comando para probar.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.6
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se configuraron las rutas del modulo `asistencia` para listar, registrar, editar, detallar, consultar por estudiante, consultar por materia, registrar por materia y consultar porcentajes de asistencia. Tambien se verifico que `config/urls.py` ya incluye las rutas de la app mediante `path('asistencia/', include('asistencia.urls'))`.

### Cambios realizados

- Se actualizo `asistencia/urls.py`.
- Se configuro `/asistencia/` para listar asistencias.
- Se configuro `/asistencia/registrar/` para registrar una asistencia individual.
- Se configuro `/asistencia/<id>/` para ver el detalle de una asistencia.
- Se configuro `/asistencia/<id>/editar/` para editar una asistencia.
- Se configuro `/asistencia/estudiante/<id>/` para consultar asistencias por estudiante.
- Se configuro `/asistencia/materia/<id>/` para consultar asistencias por materia.
- Se configuro `/asistencia/registrar-por-materia/` para registrar asistencia masiva por materia, periodo y fecha.
- Se configuro `/asistencia/porcentaje/matricula/<id>/` para consultar el porcentaje de asistencia de una matricula.
- Se configuro `/asistencia/porcentajes/materia/<id>/` para consultar porcentajes por materia.
- Se verifico que `config/urls.py` ya incluye `asistencia.urls`, por lo que no fue necesario modificarlo.

## Subfase 5.7

### Prompt usado

```text
Desarrolla la subfase 5.7 del proyecto.

Necesito crear los templates HTML del modulo asistencia.

Requisitos:
- Crear carpeta templates/asistencia/ si no existe.
- Crear templates:
  - asistencias_lista.html
  - asistencia_formulario.html
  - asistencia_detalle.html
  - asistencias_por_estudiante.html
  - asistencias_por_materia.html
  - registrar_por_materia.html
  - porcentaje_matricula.html
  - porcentajes_por_materia.html
- Usar estructura simple.
- Si existe base.html, extenderlo.
- Incluir botones de volver, editar y registrar.
- Mostrar mensajes de exito o error.
- En registrar_por_materia.html mostrar lista de estudiantes con selector de estado.
- En porcentajes mostrar tabla clara con total y porcentaje.

Quiero que me indiques:
1. Codigo completo de cada template.
2. Como se conectan con las vistas.
3. Como probar en el navegador.
4. Mensaje de commit recomendado.
5. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.7
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon los templates HTML del modulo `asistencia` para listar, registrar, editar, detallar, consultar por estudiante, consultar por materia, registrar asistencia por materia y mostrar porcentajes. No existe un `base.html` en el proyecto, por lo que se usaron documentos HTML completos y simples, siguiendo el estilo de `academico` y `notas`.

### Cambios realizados

- Se creo la carpeta `templates/asistencia/`.
- Se creo `asistencias_lista.html`.
- Se creo `asistencia_formulario.html`.
- Se creo `asistencia_detalle.html`.
- Se creo `asistencias_por_estudiante.html`.
- Se creo `asistencias_por_materia.html`.
- Se creo `registrar_por_materia.html`.
- Se creo `porcentaje_matricula.html`.
- Se creo `porcentajes_por_materia.html`.
- Se agrego visualizacion de mensajes de Django en los templates.
- Se agregaron enlaces para volver, editar, registrar y consultar porcentajes.
- Se agrego una tabla con selector de estado por estudiante en `registrar_por_materia.html`.
- Se agregaron tablas claras de totales y porcentaje en los templates de porcentaje.
- Se actualizaron las vistas para usar `registrar_por_materia.html` y `porcentaje_matricula.html`.

## Subfase 5.8

### Prompt usado

```text
Desarrolla la subfase 5.8 del proyecto.

Necesito probar el modulo de asistencia y dejar evidencia.

Requisitos:
- Verificar que el servidor Django corre sin errores.
- Probar registro de asistencia individual.
- Probar error por asistencia duplicada.
- Probar edicion de asistencia.
- Probar consulta por estudiante.
- Probar consulta por materia.
- Probar registro de asistencia por materia.
- Probar el caso de materia sin estudiantes matriculados.
- Probar calculo de porcentaje de asistencia.
- Probar que presente, tardanza y justificado cuentan como asistencia valida.
- Probar que falta cuenta como inasistencia.
- Crear o actualizar archivo de pruebas.

Archivo sugerido:
evidencias/integrante_5_pruebas.md

Debe contener:
- Caso probado
- Datos ingresados
- Resultado esperado
- Resultado obtenido
- Estado: correcto o corregido

Quiero que me indiques:
1. Lista de pruebas a realizar.
2. Contenido sugerido para integrante_5_pruebas.md.
3. Errores comunes y como solucionarlos.
4. Comando para correr el servidor.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_5_prompts.md

Agrega:
- Subfase 5.8
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se probaron los flujos principales del modulo `asistencia` y se documento la evidencia en `evidencias/integrante_5_pruebas.md`. Las pruebas cubren servidor, registro individual, duplicados, edicion, consultas, registro por materia, materia sin estudiantes y calculo de porcentaje.

### Cambios realizados

- Se creo `evidencias/integrante_5_pruebas.md`.
- Se documento el caso de servidor Django ejecutandose sin errores.
- Se documento el registro de asistencia individual.
- Se documento la validacion de asistencia duplicada.
- Se documento la edicion de asistencia.
- Se documentaron consultas por estudiante y por materia.
- Se documento el registro de asistencia por materia.
- Se documento el caso de materia sin estudiantes matriculados.
- Se documento el calculo de porcentaje de asistencia.
- Se documento que presente, tardanza y justificado cuentan como asistencia valida.
- Se documento que falta cuenta como inasistencia.
- Se agregaron errores comunes y formas de solucionarlos.

## Tarea extra: resumen de asistencia

### Prompt usado

```text
Estoy trabajando en el sistema Django de Control Academico.

Yo soy el Integrante 5 y desarrolle el modulo de asistencia. Ahora necesito agregar el resumen de asistencia dentro de la app reportes.

Requisitos:
- Trabajar en la app reportes.
- Crear una vista llamada resumen_asistencia.
- Usar los modelos existentes:
  - Asistencia
  - Matricula
  - Estudiante
  - Materia
  - PeriodoAcademico
- El resumen debe mostrar:
  - total de asistencias registradas
  - total de presentes
  - total de tardanzas
  - total de faltas
  - total de justificados
  - porcentaje general de asistencia
- Considerar como asistencia valida:
  - presente
  - tardanza
  - justificado
- Considerar como inasistencia:
  - falta
- Manejar el caso donde no existan registros de asistencia.
- Crear template reportes/resumen_asistencia.html.
- Crear o actualizar ruta.
- Agregar enlace desde el panel de reportes si todavia no existe.
- No modificar la logica interna del modulo asistencia salvo que sea estrictamente necesario.
```

### Resumen de lo generado

Se creo la vista `resumen_asistencia` en `reportes/views.py`, la ruta `resumen-asistencia/` en `reportes/urls.py` y el template `reportes/resumen_asistencia.html`. La vista usa `aggregate` con `Count` y filtros `Q` sobre el modelo `Asistencia` para obtener totales generales de registros, presentes, tardanzas, faltas y justificados. El porcentaje general se calcula como `(presentes + tardanzas + justificados) / total_registros * 100`, siguiendo la misma logica de `asistencia/utils.py` donde presente, tardanza y justificado se consideran asistencia valida y falta como inasistencia. El template muestra los indicadores cuando hay registros y un mensaje informativo cuando no los hay. Se actualizo el enlace del panel de reportes para que la tarjeta "Resumen de asistencia" apunte a la nueva vista.

### Cambios realizados

- Se agrego la vista `resumen_asistencia` en `reportes/views.py`.
- Se agrego la importacion de `Decimal` y `ROUND_HALF_UP` en `reportes/views.py`.
- Se agrego la ruta `resumen-asistencia/` en `reportes/urls.py`.
- Se creo el template `templates/reportes/resumen_asistencia.html`.
- Se actualizo el enlace en `panel_reportes.html` de `asistencia:listar_asistencias` a `reportes:resumen_asistencia`.
- No se modifico la logica interna del modulo asistencia.

## Subfase 5.9 - Protección de vistas y sesiones

### Prompt usado

```text
Desarrolla la subfase 5.9 del proyecto.

Necesito proteger las vistas principales del sistema para que solo usuarios autenticados puedan acceder.

Responsable principal: Integrante 5.

Requisitos:
- Usar @login_required en vistas principales de estudiantes, academico, notas, asistencia y reportes.
- Proteger también la página de inicio si el sistema debe iniciar después del login.
- Si un usuario no autenticado intenta entrar a un módulo, debe redirigirse al login.
- No modificar la lógica de cada vista ni cambiar nombres de rutas.
- Mantener compatibilidad con LOGIN_URL.
```

### Resumen de lo generado

Se protegieron las vistas de Estudiantes, Académico, Notas, Asistencia, Reportes y la página de inicio mediante `login_required`. Como `LOGIN_REDIRECT_URL` apunta a `home`, la portada queda disponible inmediatamente después del login y no es accesible sin sesión. Se mantuvo el login de Django y la lógica interna de los módulos.

### Cambios realizados

- Se agregó `login_required` a las vistas de los cinco módulos principales, sin alterar su lógica interna.
- Se protegió `core.views.home` para que el panel principal requiera una sesión válida.
- Los usuarios sin sesión son redirigidos a `cuentas/login/` conservando la URL solicitada en el parámetro `next`.
- Se configuró `LOGOUT_REDIRECT_URL = 'login'` para que el cierre de sesión termine en la pantalla de acceso.
- Se agregaron pruebas de protección de rutas, creación de sesión, cierre de sesión y acceso por POST sin autenticar en `core/tests.py`.
- Se adaptaron las pruebas de integración existentes para ejecutarse con un usuario autenticado.

## Subfase 5.10 - Manejo básico de sesiones

### Prompt usado

```text
Desarrolla la subfase 5.10 del proyecto.

Necesito agregar manejo básico de sesiones en el sistema.

Responsable principal: Integrante 5.

Requisitos:
- Verificar que Django tenga activado SessionMiddleware.
- Verificar que AuthenticationMiddleware esté activo.
- Mostrar en el menú el usuario autenticado.
- Agregar mensaje de bienvenida al iniciar sesión.
- Agregar mensaje al cerrar sesión si es posible.
- Configurar duración de sesión si corresponde.
- Evitar acceso a páginas internas después de cerrar sesión.
- No implementar roles avanzados todavía.
```

### Resumen de lo generado

Se verificó la configuración de middleware de sesión y autenticación de Django. Se mantuvo la visualización del usuario autenticado en el menú, se añadieron mensajes de bienvenida y cierre de sesión, y se configuró una duración máxima de ocho horas con cierre al terminar el navegador. Las vistas protegidas continúan impidiendo el acceso después de cerrar sesión.

### Cambios realizados

- Se verificó que `SessionMiddleware` y `AuthenticationMiddleware` están activos y en el orden requerido.
- Se configuraron `SESSION_COOKIE_AGE = 60 * 60 * 8` y `SESSION_EXPIRE_AT_BROWSER_CLOSE = True`.
- Se crearon extensiones mínimas de `LoginView` y `LogoutView` para mostrar mensajes de sesión sin cambiar las rutas existentes.
- Se confirmó que `base.html` ya muestra el nombre del usuario autenticado y los mensajes del sistema.
- Se agregaron pruebas para middleware, duración de sesión, bienvenida, cierre de sesión y bloqueo de inicio después del logout.

## Subfase 5.11 - Pruebas de autenticación y sesiones

### Prompt usado

```text
Desarrolla la subfase 5.11 del proyecto.

Necesito probar el login, logout y protección de sesiones del sistema.

Responsable principal: Integrante 5.

Requisitos:
- Crear o actualizar evidencias/integrante_5_pruebas_auth.md.
- Probar acceso sin sesión, redirección al login, login correcto e incorrecto, acceso autenticado, cierre de sesión y bloqueo posterior.
- Registrar caso probado, datos usados, resultado esperado, resultado obtenido y estado.
```

### Resumen de lo generado

Se creó una evidencia específica para autenticación y sesiones. Las pruebas verifican que las rutas internas redirigen al login sin sesión, que las credenciales válidas crean una sesión, que las inválidas no la crean, y que el logout bloquea de nuevo las rutas internas.

### Cambios realizados

- Se creó `evidencias/integrante_5_pruebas_auth.md` con los siete casos de autenticación solicitados.
- Se agregó una prueba automatizada para login incorrecto en `core/tests.py`.
- Se documentaron datos de prueba no reales, comandos ejecutados y errores frecuentes de configuración.
