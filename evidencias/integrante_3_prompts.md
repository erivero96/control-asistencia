# Evidencias - Integrante 3

## Subfase 3.1

### Prompt usado

```text
Desarrolla la subfase 3.1 del proyecto.

Necesito crear el modelo Materia para el sistema web de Control Academico en Django.

Requisitos:
- Trabajar en la app academico.
- Crear el modelo Materia.
- Campos:
  - codigo
  - nombre
  - descripcion
  - creditos
  - estado
  - fecha_registro
- El campo codigo debe ser unico.
- El campo estado debe permitir activo e inactivo.
- Registrar el modelo en admin.py.
- Configurar el admin para mostrar codigo, nombre, creditos y estado.
- Permitir busqueda por codigo y nombre.
- Crear y ejecutar migraciones.
- No crear todavia vistas ni formularios.

Quiero que me indiques:
1. Archivos que se deben modificar.
2. Codigo completo del modelo Materia.
3. Codigo completo del admin.py.
4. Comandos para crear y ejecutar migraciones.
5. Comando para probar que no hay errores.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien crea o actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.1
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `Materia` dentro de la app `academico`, con codigo unico, nombre, descripcion, creditos, estado activo/inactivo y fecha automatica de registro. Tambien se registro el modelo en el panel de administracion de Django con las columnas solicitadas y busqueda por codigo y nombre.

### Cambios realizados

- Se creo el modelo `Materia` en `academico/models.py`.
- Se agrego la restriccion `unique=True` para `codigo`.
- Se configuro el campo `estado` con opciones `activo` e `inactivo`.
- Se configuro `fecha_registro` con `auto_now_add=True`.
- Se registro `Materia` en `academico/admin.py`.
- Se configuraron las columnas `codigo`, `nombre`, `creditos` y `estado` en el admin.
- Se habilito busqueda por codigo y nombre.
- Se dejo pendiente el desarrollo de vistas y formularios para subfases posteriores.

## Subfase 3.2

### Prompt usado

```text
Desarrolla la subfase 3.2 del proyecto.

Necesito crear el modelo PeriodoAcademico para el sistema web de Control Academico.

Requisitos:
- Trabajar en la app academico.
- Crear el modelo PeriodoAcademico.
- Campos:
  - nombre
  - fecha_inicio
  - fecha_fin
  - estado
  - fecha_registro
- El campo nombre debe ser unico.
- El estado debe permitir activo, inactivo y finalizado.
- Validar que la fecha de fin no sea menor que la fecha de inicio.
- Registrar el modelo en admin.py.
- Configurar busqueda por nombre.
- Crear y ejecutar migraciones.
- No crear todavia vistas ni formularios.

Quiero que me indiques:
1. Codigo completo del modelo PeriodoAcademico.
2. Codigo actualizado de admin.py.
3. Validacion de fechas.
4. Comandos de migracion.
5. Comando para probar que no hay errores.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.2
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `PeriodoAcademico` dentro de la app `academico`, con nombre unico, fechas de inicio y fin, estado activo/inactivo/finalizado y fecha automatica de registro. Tambien se agrego una validacion para impedir que la fecha de fin sea menor que la fecha de inicio y se registro el modelo en el panel de administracion de Django.

### Cambios realizados

- Se creo el modelo `PeriodoAcademico` en `academico/models.py`.
- Se agrego la restriccion `unique=True` para `nombre`.
- Se configuro el campo `estado` con opciones `activo`, `inactivo` y `finalizado`.
- Se agrego validacion de fechas mediante el metodo `clean()`.
- Se agrego una restriccion de base de datos para reforzar que `fecha_fin` sea mayor o igual que `fecha_inicio`.
- Se registro `PeriodoAcademico` en `academico/admin.py`.
- Se habilito busqueda por nombre en el admin.
- Se dejo pendiente el desarrollo de vistas y formularios para subfases posteriores.

## Subfase 3.3

### Prompt usado

```text
Desarrolla la subfase 3.3 del proyecto.

Necesito crear el modelo Matricula para relacionar estudiantes, materias y periodos academicos.

Requisitos:
- Trabajar en la app academico.
- Usar el modelo Estudiante de la app estudiantes.
- Usar los modelos Materia y PeriodoAcademico de academico.
- Crear el modelo Matricula.
- Campos:
  - estudiante
  - materia
  - periodo
  - fecha_matricula
  - estado
- El estado debe permitir matriculado, retirado y finalizado.
- Evitar que un mismo estudiante se matricule dos veces en la misma materia y periodo.
- Registrar el modelo en admin.py.
- En el admin mostrar estudiante, materia, periodo, estado y fecha_matricula.
- Crear y ejecutar migraciones.

Quiero que me indiques:
1. Codigo completo del modelo Matricula.
2. Codigo actualizado de admin.py.
3. Como se evita la matricula duplicada.
4. Comandos de migracion.
5. Comando para probar que no hay errores.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.3
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `Matricula` dentro de la app `academico` para relacionar un estudiante con una materia en un periodo academico. El modelo incluye estado matriculado/retirado/finalizado, fecha automatica de matricula y una restriccion para evitar matriculas duplicadas del mismo estudiante en la misma materia y periodo.

### Cambios realizados

- Se importo el modelo `Estudiante` desde la app `estudiantes`.
- Se creo el modelo `Matricula` en `academico/models.py`.
- Se relaciono `Matricula` con `Estudiante`, `Materia` y `PeriodoAcademico`.
- Se configuro el campo `estado` con opciones `matriculado`, `retirado` y `finalizado`.
- Se configuro `fecha_matricula` con `auto_now_add=True`.
- Se agrego una restriccion unica para `estudiante`, `materia` y `periodo`.
- Se registro `Matricula` en `academico/admin.py`.
- Se configuro el admin para mostrar estudiante, materia, periodo, estado y fecha_matricula.

## Subfase 3.4

### Prompt usado

```text
Desarrolla la subfase 3.4 del proyecto.

Necesito crear formularios para el modulo academico.

Requisitos:
- Trabajar en la app academico.
- Crear archivo forms.py si no existe.
- Crear:
  - MateriaForm
  - PeriodoAcademicoForm
  - MatriculaForm
- MateriaForm debe validar codigo, nombre y creditos.
- PeriodoAcademicoForm debe validar fechas.
- MatriculaForm debe validar estudiante, materia y periodo.
- MatriculaForm debe evitar matricula duplicada.
- Mostrar mensajes de error claros.
- No tocar notas, asistencia ni reportes.

Quiero que me indiques:
1. Codigo completo de forms.py.
2. Validaciones incluidas.
3. Como funciona cada formulario.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.4
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el archivo `academico/forms.py` con los formularios `MateriaForm`, `PeriodoAcademicoForm` y `MatriculaForm`. Cada formulario usa `ModelForm`, define etiquetas y mensajes de error claros, y agrega validaciones especificas para datos obligatorios, creditos, fechas y matriculas duplicadas.

### Cambios realizados

- Se creo `MateriaForm` para registrar y editar materias.
- Se validaron codigo, nombre y creditos de materia.
- Se creo `PeriodoAcademicoForm` para registrar y editar periodos academicos.
- Se valido que la fecha de fin no sea menor que la fecha de inicio.
- Se creo `MatriculaForm` para registrar y editar matriculas.
- Se validaron estudiante, materia y periodo en matriculas.
- Se agrego validacion para evitar matriculas duplicadas del mismo estudiante en la misma materia y periodo.
- No se tocaron las apps de notas, asistencia ni reportes.

## Subfase 3.5

### Prompt usado

```text
Desarrolla la subfase 3.5 del proyecto.

Necesito crear las vistas del modulo academico en Django.

Requisitos:
- Trabajar en la app academico.
- Crear vistas para materias:
  - listar_materias
  - crear_materia
  - editar_materia
  - desactivar_materia
- Crear vistas para periodos:
  - listar_periodos
  - crear_periodo
  - editar_periodo
- Crear vistas para matriculas:
  - listar_matriculas
  - crear_matricula
  - detalle_matricula
  - retirar_matricula
- Usar django.contrib.messages.
- No borrar registros, solo cambiar estado cuando corresponda.
- Ordenar materias por nombre.
- Ordenar periodos por fecha_inicio.
- Ordenar matriculas por periodo y estudiante.

Quiero que me indiques:
1. Codigo completo de views.py.
2. Explicacion de cada vista.
3. Validaciones aplicadas.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.5
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon las vistas del modulo `academico` para listar, registrar, editar y desactivar materias; listar, registrar y editar periodos academicos; y listar, registrar, ver detalle y retirar matriculas. Las vistas usan formularios del modulo, mensajes de Django y cambios de estado para evitar borrar registros.

### Cambios realizados

- Se actualizaron las vistas en `academico/views.py`.
- Se agregaron vistas de materias: `listar_materias`, `crear_materia`, `editar_materia` y `desactivar_materia`.
- Se agregaron vistas de periodos: `listar_periodos`, `crear_periodo` y `editar_periodo`.
- Se agregaron vistas de matriculas: `listar_matriculas`, `crear_matricula`, `detalle_matricula` y `retirar_matricula`.
- Se usaron `MateriaForm`, `PeriodoAcademicoForm` y `MatriculaForm`.
- Se agregaron mensajes de exito y error con `django.contrib.messages`.
- Se configuro la desactivacion de materias para cambiar estado a `inactivo` sin borrar registros.
- Se configuro el retiro de matriculas para cambiar estado a `retirado` sin borrar registros.
- Se ordenaron materias por nombre.
- Se ordenaron periodos por fecha de inicio.
- Se ordenaron matriculas por periodo y estudiante.

## Subfase 3.6

### Prompt usado

```text
Desarrolla la subfase 3.6 del proyecto.

Necesito configurar las rutas del modulo academico.

Requisitos:
- Trabajar en academico/urls.py.
- Crear rutas para materias:
  - /academico/materias/
  - /academico/materias/crear/
  - /academico/materias/<id>/editar/
  - /academico/materias/<id>/desactivar/
- Crear rutas para periodos:
  - /academico/periodos/
  - /academico/periodos/crear/
  - /academico/periodos/<id>/editar/
- Crear rutas para matriculas:
  - /academico/matriculas/
  - /academico/matriculas/crear/
  - /academico/matriculas/<id>/
  - /academico/matriculas/<id>/retirar/
- Verificar que config/urls.py incluya las rutas de academico.
- Usar nombres de rutas claros.

Quiero que me indiques:
1. Codigo completo de academico/urls.py.
2. Si se modifica config/urls.py, mostrar el codigo necesario.
3. Explicacion de cada ruta.
4. Comando para probar.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.6
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se configuraron las rutas del modulo `academico` para materias, periodos academicos y matriculas. Tambien se verifico que `config/urls.py` ya incluye las rutas de la app mediante `path('academico/', include('academico.urls'))`, por lo que no fue necesario modificar la configuracion principal.

### Cambios realizados

- Se actualizo `academico/urls.py`.
- Se agregaron rutas para listar, crear, editar y desactivar materias.
- Se agregaron rutas para listar, crear y editar periodos academicos.
- Se agregaron rutas para listar, crear, ver detalle y retirar matriculas.
- Se mantuvo el namespace `academico`.
- Se verifico que `config/urls.py` ya incluye `academico.urls`.

## Subfase 3.7

### Prompt usado

```text
Desarrolla la subfase 3.7 del proyecto.

Necesito crear los templates HTML del modulo academico.

Requisitos:
- Crear carpeta templates/academico/ si no existe.
- Crear templates para materias:
  - materias_lista.html
  - materia_formulario.html
  - materia_confirmar_desactivar.html
- Crear templates para periodos:
  - periodos_lista.html
  - periodo_formulario.html
- Crear templates para matriculas:
  - matriculas_lista.html
  - matricula_formulario.html
  - matricula_detalle.html
  - matricula_confirmar_retirar.html
- Usar estructura simple.
- Si existe base.html, extenderlo.
- Incluir botones de volver, editar y registrar.
- Mostrar mensajes de exito o error.

Quiero que me indiques:
1. Codigo completo de cada template.
2. Como se conectan con las vistas.
3. Como probar en el navegador.
4. Mensaje de commit recomendado.
5. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.7
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon los templates HTML del modulo `academico` para materias, periodos academicos y matriculas. No existia `base.html`, por lo que se uso una estructura HTML completa y simple, consistente con los templates existentes del modulo `estudiantes`.

### Cambios realizados

- Se creo la carpeta `templates/academico/`.
- Se crearon los templates `materias_lista.html`, `materia_formulario.html` y `materia_confirmar_desactivar.html`.
- Se crearon los templates `periodos_lista.html` y `periodo_formulario.html`.
- Se crearon los templates `matriculas_lista.html`, `matricula_formulario.html`, `matricula_detalle.html` y `matricula_confirmar_retirar.html`.
- Se agregaron enlaces para volver, registrar, editar, desactivar o retirar segun corresponda.
- Se agrego visualizacion de mensajes de exito o error con `messages`.
- Se actualizaron las vistas de `academico/views.py` para usar los nombres de templates solicitados.

## Subfase 3.8

### Prompt usado

```text
Desarrolla la subfase 3.8 del proyecto.

Necesito probar el modulo academico y dejar evidencia.

Requisitos:
- Verificar que el servidor Django corre sin errores.
- Probar registro de materia.
- Probar error por codigo de materia duplicado.
- Probar edicion de materia.
- Probar desactivacion de materia.
- Probar registro de periodo academico.
- Probar error si fecha fin es menor que fecha inicio.
- Probar registro de matricula.
- Probar error por matricula duplicada.
- Probar retiro de matricula.
- Crear o actualizar archivo de pruebas.

Archivo sugerido:
evidencias/integrante_3_pruebas.md

Debe contener:
- Caso probado
- Datos ingresados
- Resultado esperado
- Resultado obtenido
- Estado: correcto o corregido

Quiero que me indiques:
1. Lista de pruebas a realizar.
2. Contenido sugerido para integrante_3_pruebas.md.
3. Errores comunes y como solucionarlos.
4. Comando para correr el servidor.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_3_prompts.md

Agrega:
- Subfase 3.8
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se probaron las funcionalidades principales del modulo academico y se creo el archivo `evidencias/integrante_3_pruebas.md` con los casos ejecutados, datos ingresados, resultados esperados, resultados obtenidos y estado de cada prueba.

### Cambios realizados

- Se verifico que `manage.py check` no reporta errores.
- Se levanto el servidor Django en `127.0.0.1:8001` y se verifico respuesta `200 OK`.
- Se probaron registro, duplicado, edicion y desactivacion de materias.
- Se probaron registro y validacion de fechas en periodos academicos.
- Se probaron registro, duplicado y retiro de matriculas.
- Se creo `evidencias/integrante_3_pruebas.md`.
- No se modifico codigo funcional del modulo academico.
