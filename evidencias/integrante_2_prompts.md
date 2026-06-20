# Evidencias - Integrante 2

## Subfase 2.1

### Prompt usado

```text
Desarrolla la subfase 2.1 del proyecto.

Necesito crear el modelo Estudiante para el sistema web de Control Academico en Django.

Requisitos:
- Trabajar en la app estudiantes.
- Crear el modelo Estudiante.
- Campos requeridos:
  - codigo
  - nombres
  - apellidos
  - dni
  - correo
  - telefono
  - direccion
  - estado
  - fecha_registro
- El campo codigo debe ser unico.
- El campo dni debe ser unico.
- El campo estado debe permitir activo e inactivo.
- Registrar el modelo en admin.py.
- Configurar el admin para mostrar columnas importantes.
- Permitir busqueda por codigo, DNI, nombres y apellidos.
- Crear y ejecutar migraciones.
- No crear todavia vistas ni formularios.

Quiero que me indiques:
1. Archivos que se deben modificar.
2. Codigo completo del modelo Estudiante.
3. Codigo completo del admin.py.
4. Comandos para crear y ejecutar migraciones.
5. Comando para probar que no hay errores.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien crea o actualiza:
evidencias/integrante_2_prompts.md

Agrega:
- Subfase 2.1
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `Estudiante` dentro de la app `estudiantes`, con campos para datos personales, codigo unico, DNI unico, estado activo/inactivo y fecha automatica de registro. Tambien se registro el modelo en el panel de administracion de Django con columnas principales, filtros y busqueda.

### Cambios realizados

- Se creo el modelo `Estudiante` en `estudiantes/models.py`.
- Se agregaron restricciones `unique=True` para `codigo` y `dni`.
- Se configuro el campo `estado` con opciones `activo` e `inactivo`.
- Se configuro `fecha_registro` con `auto_now_add=True`.
- Se registro `Estudiante` en `estudiantes/admin.py`.
- Se configuraron columnas importantes en el admin.
- Se habilito busqueda por codigo, DNI, nombres y apellidos.
- Se dejo pendiente el desarrollo de vistas y formularios para subfases posteriores.

## Subfase 2.2

### Prompt usado

```text
Desarrolla la subfase 2.2 del proyecto.

Necesito crear el formulario para registrar y editar estudiantes.

Requisitos:
- Trabajar en la app estudiantes.
- Crear un archivo forms.py si no existe.
- Crear EstudianteForm usando ModelForm.
- Incluir los campos:
  - codigo
  - nombres
  - apellidos
  - dni
  - correo
  - telefono
  - direccion
  - estado
- Validar que el codigo no este vacio.
- Validar que el DNI tenga 8 digitos.
- Validar que nombres y apellidos sean obligatorios.
- Mostrar mensajes de error claros.
- No crear todavia templates completos si no es necesario.
- No tocar otros modulos.

Quiero que me indiques:
1. Codigo completo de forms.py.
2. Validaciones incluidas.
3. Como funciona el formulario.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_2_prompts.md

Agrega:
- Subfase 2.2
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el formulario `EstudianteForm` usando `ModelForm` para registrar y editar estudiantes a partir del modelo `Estudiante`. El formulario incluye los campos solicitados y validaciones personalizadas para codigo, DNI, nombres y apellidos, con mensajes de error claros.

### Cambios realizados

- Se creo el archivo `estudiantes/forms.py`.
- Se creo la clase `EstudianteForm`.
- Se incluyeron los campos `codigo`, `nombres`, `apellidos`, `dni`, `correo`, `telefono`, `direccion` y `estado`.
- Se agrego validacion para evitar codigo vacio.
- Se agrego validacion para exigir DNI de exactamente 8 digitos numericos.
- Se agregaron validaciones para nombres y apellidos obligatorios.
- Se configuraron mensajes de error claros para los campos del formulario.
- No se crearon vistas ni templates en esta subfase.

## Subfase 2.3

### Prompt usado

```text
Desarrolla la subfase 2.3 del proyecto.

Necesito crear las vistas del modulo de estudiantes en Django.

Requisitos:
- Trabajar en la app estudiantes.
- Crear vistas para:
  - listar_estudiantes
  - crear_estudiante
  - detalle_estudiante
  - editar_estudiante
  - desactivar_estudiante
- Usar el modelo Estudiante.
- Usar EstudianteForm.
- En desactivar_estudiante no borrar el registro, solo cambiar estado a inactivo.
- Ordenar estudiantes por apellidos y nombres.
- Mostrar mensajes de exito o error usando django.contrib.messages.
- No desarrollar todavia materias, notas, asistencia ni reportes.

Quiero que me indiques:
1. Codigo completo de views.py.
2. Explicacion de cada vista.
3. Validaciones aplicadas.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_2_prompts.md

Agrega:
- Subfase 2.3
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon las vistas principales del modulo de estudiantes: listado, registro, detalle, edicion y desactivacion. Las vistas usan el modelo `Estudiante`, el formulario `EstudianteForm` y mensajes de Django para informar resultados correctos o errores de validacion.

### Cambios realizados

- Se agrego la vista `listar_estudiantes`.
- Se agrego la vista `crear_estudiante`.
- Se agrego la vista `detalle_estudiante`.
- Se agrego la vista `editar_estudiante`.
- Se agrego la vista `desactivar_estudiante`.
- Se ordeno el listado por apellidos y nombres.
- Se uso `EstudianteForm` para crear y editar estudiantes.
- Se uso `get_object_or_404` para obtener estudiantes existentes.
- Se configuro la desactivacion para cambiar `estado` a `inactivo` sin borrar registros.
- Se agregaron mensajes de exito y error con `django.contrib.messages`.
- No se desarrollaron materias, notas, asistencia ni reportes.

## Subfase 2.4

### Prompt usado

```text
Desarrolla la subfase 2.4 del proyecto.

Necesito configurar las rutas del modulo estudiantes.

Requisitos:
- Trabajar en estudiantes/urls.py.
- Crear rutas para:
  - /estudiantes/
  - /estudiantes/crear/
  - /estudiantes/<id>/
  - /estudiantes/<id>/editar/
  - /estudiantes/<id>/desactivar/
- Usar nombres de rutas claros.
- Verificar que config/urls.py incluya las rutas de estudiantes.
- No modificar rutas de otros modulos salvo que sea necesario para conectar estudiantes.

Quiero que me indiques:
1. Codigo completo de estudiantes/urls.py.
2. Si se modifica config/urls.py, mostrar el codigo necesario.
3. Explicacion de cada ruta.
4. Comando para probar.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_2_prompts.md

Agrega:
- Subfase 2.4
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se configuraron las rutas del modulo `estudiantes` para listar, crear, ver detalle, editar y desactivar estudiantes. Tambien se verifico que `config/urls.py` ya incluye las rutas de la app mediante `path('estudiantes/', include('estudiantes.urls'))`, por lo que no fue necesario modificar la configuracion principal.

### Cambios realizados

- Se actualizo `estudiantes/urls.py`.
- Se agrego la ruta `/estudiantes/` para listar estudiantes.
- Se agrego la ruta `/estudiantes/crear/` para registrar estudiantes.
- Se agrego la ruta `/estudiantes/<id>/` para ver el detalle de un estudiante.
- Se agrego la ruta `/estudiantes/<id>/editar/` para editar un estudiante.
- Se agrego la ruta `/estudiantes/<id>/desactivar/` para desactivar un estudiante.
- Se usaron nombres de ruta claros como `listar_estudiantes`, `crear_estudiante`, `detalle_estudiante`, `editar_estudiante` y `desactivar_estudiante`.
- Se mantuvo `index` como alias temporal de compatibilidad para enlaces existentes hacia el modulo.
- No se modificaron rutas de otros modulos.

## Subfase 2.5

### Prompt usado

```text
Desarrolla la subfase 2.5 del proyecto.

Necesito crear los templates HTML del modulo estudiantes.

Requisitos:
- Crear carpeta templates/estudiantes/ si no existe.
- Crear los templates:
  - lista.html
  - formulario.html
  - detalle.html
  - confirmar_desactivar.html
- La lista debe mostrar:
  - codigo
  - nombres
  - apellidos
  - DNI
  - correo
  - estado
  - acciones
- El formulario debe servir para crear y editar.
- El detalle debe mostrar toda la informacion del estudiante.
- La confirmacion debe preguntar antes de desactivar.
- Usar una estructura simple y entendible.
- Si existe un template base.html, extenderlo.
- Si no existe, indicar como crear uno basico sin afectar otros modulos.

Quiero que me indiques:
1. Codigo completo de cada template.
2. Como se conectan con las vistas.
3. Como probar en el navegador.
4. Mensaje de commit recomendado.
5. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_2_prompts.md

Agrega:
- Subfase 2.5
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon los templates HTML del modulo `estudiantes` para listar, crear/editar, ver detalle y confirmar la desactivacion de estudiantes. No existia un `base.html` global, por lo que se usaron templates independientes con estructura HTML simple.

### Cambios realizados

- Se creo la carpeta `templates/estudiantes/`.
- Se creo `templates/estudiantes/lista.html`.
- Se creo `templates/estudiantes/formulario.html`.
- Se creo `templates/estudiantes/detalle.html`.
- Se creo `templates/estudiantes/confirmar_desactivar.html`.
- Se actualizo `estudiantes/views.py` para usar los nombres de templates solicitados.
- Se reutilizo `formulario.html` para registrar y editar estudiantes.
- Se agregaron enlaces de acciones para ver, editar y desactivar estudiantes.
- Se agrego confirmacion previa antes de desactivar un estudiante.

## Subfase 2.6

### Prompt usado

```text
Desarrolla la subfase 2.6 del proyecto.

Necesito probar el modulo de estudiantes y dejar evidencia.

Requisitos:
- Verificar que el servidor Django corre sin errores.
- Verificar que se puede entrar a /estudiantes/.
- Probar registro de estudiante.
- Probar edicion de estudiante.
- Probar detalle de estudiante.
- Probar desactivacion de estudiante.
- Probar error por DNI duplicado.
- Probar error por codigo duplicado.
- Probar error por DNI con menos o mas de 8 digitos.
- Crear o actualizar un archivo de casos de prueba.

Archivo sugerido:
evidencias/integrante_2_pruebas.md

Debe contener:
- Caso probado
- Datos ingresados
- Resultado esperado
- Resultado obtenido
- Estado: correcto o corregido

Quiero que me indiques:
1. Lista de pruebas a realizar.
2. Contenido sugerido para integrante_2_pruebas.md.
3. Errores comunes y como solucionarlos.
4. Comando para correr el servidor.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_2_prompts.md

Agrega:
- Subfase 2.6
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se probaron las funciones principales del modulo de estudiantes: acceso al listado, registro, edicion, detalle, desactivacion y validaciones de duplicados y longitud del DNI. Tambien se creo el archivo `evidencias/integrante_2_pruebas.md` con los casos probados y sus resultados.

### Cambios realizados

- Se verifico que Django no reporta errores con `manage.py check`.
- Se verifico que `/estudiantes/` responde correctamente.
- Se probaron registro, edicion, detalle y desactivacion de estudiante con datos temporales.
- Se probaron errores por DNI duplicado y codigo duplicado.
- Se probaron errores por DNI con menos y mas de 8 digitos.
- Se creo `evidencias/integrante_2_pruebas.md`.
- Se corrigio el mensaje de error de `dni` para el caso `max_length`, mostrando un mensaje claro cuando el DNI tiene mas de 8 digitos.

## Tarea extra: reporte por estudiante

### Prompt usado

```text
Estoy trabajando en el sistema Django de Control Academico.

Yo soy el Integrante 2 y desarrolle el modulo de estudiantes. Ahora necesito agregar el reporte por estudiante dentro del modulo reportes.

Requisitos:
- Trabajar en la app reportes.
- Crear una vista llamada reporte_estudiante.
- El reporte debe permitir seleccionar o recibir un estudiante.
- Usar los modelos existentes:
  - Estudiante
  - Matricula
  - Nota
  - Asistencia
- El reporte debe mostrar:
  - codigo del estudiante
  - nombres y apellidos
  - DNI
  - correo
  - materias matriculadas
  - periodo academico
  - notas registradas si existen
  - asistencias registradas si existen
- Manejar casos donde:
  - el estudiante no tiene matriculas
  - el estudiante no tiene notas
  - el estudiante no tiene asistencias
- Crear o actualizar la ruta correspondiente.
- Crear template reportes/reporte_estudiante.html.
- Agregar acceso desde el panel de reportes si todavia no existe.
- No modificar la logica interna de estudiantes, notas ni asistencia.
```

### Resumen de lo generado

Se verifico que la vista `reporte_estudiante` ya existia en `reportes/views.py` (construida previamente por el Integrante 1 en la estructura base de reportes), junto con la URL `estudiante/<int:estudiante_id>/` y el template `reportes/reporte_estudiante.html`. La vista consulta el modelo `Estudiante`, recorre las `Matricula` vinculadas y agrega `Nota` y `Asistencia` por cada matricula usando `calcular_promedio_ponderado_por_matricula` y `resumen_asistencia_matricula`. Se agregaron enlaces de navegacion desde `estudiantes/lista.html` y `estudiantes/detalle.html` hacia `reportes:reporte_estudiante` para permitir que el usuario acceda al reporte desde el modulo de estudiantes.

### Cambios realizados

- Se verifico el funcionamiento de `reportes/views.py` con la funcion `reporte_estudiante`.
- Se verifico la ruta `reporte_estudiante` en `reportes/urls.py`.
- Se verifico el template `reportes/reporte_estudiante.html`.
- Se verifico el acceso desde `panel_reportes.html` hacia el listado de estudiantes.
- Se agrego boton "Reporte" en `estudiantes/lista.html` dentro de la columna de acciones.
- Se agrego boton "Ver reporte" en `estudiantes/detalle.html` en la barra de navegacion.
- Se mantuvo sin cambios la logica interna de `estudiantes/views.py`, `notas` y `asistencia`.
