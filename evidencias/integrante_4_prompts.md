# Evidencias - Integrante 4

## Subfase 4.1

### Prompt usado

```text
Desarrolla la subfase 4.1 del proyecto.

Necesito crear el modelo Evaluacion para el sistema web de Control Academico en Django.

Requisitos:
- Trabajar en la app notas.
- Usar los modelos Materia y PeriodoAcademico de la app academico.
- Crear el modelo Evaluacion.
- Campos:
  - materia
  - periodo
  - nombre
  - descripcion
  - peso
  - fecha_registro
  - estado
- El peso debe representar el porcentaje de la evaluacion.
- El peso debe ser mayor que 0.
- El estado debe permitir activo e inactivo.
- Registrar el modelo en admin.py.
- En el admin mostrar materia, periodo, nombre, peso y estado.
- Permitir busqueda por nombre y materia.
- Crear y ejecutar migraciones.
- No crear todavia vistas ni formularios.

Quiero que me indiques:
1. Archivos que se deben modificar.
2. Codigo completo del modelo Evaluacion.
3. Codigo completo o actualizado de admin.py.
4. Comandos para crear y ejecutar migraciones.
5. Comando para probar que no hay errores.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien crea o actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.1
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `Evaluacion` dentro de la app `notas`, relacionado con `Materia` y `PeriodoAcademico` de la app `academico`. El modelo permite registrar evaluaciones por materia y periodo, definir un peso porcentual mayor que cero, manejar estado activo/inactivo y guardar automaticamente la fecha de registro.

### Cambios realizados

- Se creo el modelo `Evaluacion` en `notas/models.py`.
- Se relaciono `Evaluacion` con `Materia` y `PeriodoAcademico` mediante llaves foraneas protegidas.
- Se agregaron los campos `nombre`, `descripcion`, `peso`, `fecha_registro` y `estado`.
- Se configuro `peso` como porcentaje decimal con validacion para valores mayores que cero.
- Se agrego una restriccion de base de datos para impedir pesos menores o iguales a cero.
- Se configuro el estado con opciones `activo` e `inactivo`.
- Se registro `Evaluacion` en `notas/admin.py`.
- Se configuro el admin para mostrar materia, periodo, nombre, peso y estado.
- Se habilito busqueda por nombre, codigo de materia y nombre de materia.
- Se genero la migracion inicial `notas/migrations/0001_initial.py`.
- Se aplico la migracion en la base de datos configurada.
- No se crearon vistas ni formularios en esta subfase.

## Subfase 4.2

### Prompt usado

```text
Desarrolla la subfase 4.2 del proyecto.

Necesito crear el modelo Nota para registrar las calificaciones de los estudiantes.

Requisitos:
- Trabajar en la app notas.
- Usar el modelo Matricula de la app academico.
- Usar el modelo Evaluacion de la app notas.
- Crear el modelo Nota.
- Campos:
  - matricula
  - evaluacion
  - calificacion
  - observacion
  - fecha_registro
- La calificacion debe permitir decimales.
- La calificacion debe estar entre 0 y 20.
- Evitar que se registre dos veces una nota para la misma matricula y evaluacion.
- Registrar el modelo en admin.py.
- En el admin mostrar estudiante, materia, evaluacion, calificacion y fecha_registro.
- Crear y ejecutar migraciones.

Quiero que me indiques:
1. Codigo completo del modelo Nota.
2. Codigo actualizado de admin.py.
3. Como se valida que la nota este entre 0 y 20.
4. Como se evita una nota duplicada.
5. Comandos de migracion.
6. Comando para probar que no hay errores.
7. Mensaje de commit recomendado.
8. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.2
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el modelo `Nota` dentro de la app `notas` para registrar calificaciones de estudiantes a partir de una `Matricula` y una `Evaluacion`. La calificacion permite decimales, se valida para mantenerse entre 0 y 20, y se evita duplicar una nota para la misma matricula y evaluacion.

### Cambios realizados

- Se importo `Matricula` desde la app `academico`.
- Se creo el modelo `Nota` en `notas/models.py`.
- Se relaciono `Nota` con `Matricula` y `Evaluacion` mediante llaves foraneas protegidas.
- Se agregaron los campos `calificacion`, `observacion` y `fecha_registro`.
- Se configuro `calificacion` como decimal con validadores de minimo 0 y maximo 20.
- Se agrego una restriccion de base de datos para asegurar que la calificacion este entre 0 y 20.
- Se agrego una restriccion unica para evitar notas duplicadas por matricula y evaluacion.
- Se registro `Nota` en `notas/admin.py`.
- Se configuro el admin para mostrar estudiante, materia, evaluacion, calificacion y fecha de registro.
- Se genero la migracion `notas/migrations/0002_nota.py`.
- Se aplico la migracion en la base de datos configurada.

## Subfase 4.3

### Prompt usado

```text
Desarrolla la subfase 4.3 del proyecto.

Necesito crear formularios para el modulo de notas.

Requisitos:
- Trabajar en la app notas.
- Crear archivo forms.py si no existe.
- Crear:
  - EvaluacionForm
  - NotaForm
- EvaluacionForm debe validar:
  - materia obligatoria
  - periodo obligatorio
  - nombre obligatorio
  - peso mayor que 0
- NotaForm debe validar:
  - matricula obligatoria
  - evaluacion obligatoria
  - calificacion entre 0 y 20
  - que no exista nota duplicada para la misma matricula y evaluacion
- Mostrar mensajes de error claros.
- No tocar asistencia ni reportes generales.

Quiero que me indiques:
1. Codigo completo de forms.py.
2. Validaciones incluidas.
3. Como funciona cada formulario.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.3
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo el archivo `notas/forms.py` con los formularios `EvaluacionForm` y `NotaForm`. Ambos formularios usan `ModelForm`, muestran etiquetas y mensajes de error claros, y agregan validaciones especificas para campos obligatorios, rangos numericos y duplicidad de notas.

### Cambios realizados

- Se creo el archivo `notas/forms.py`.
- Se creo `EvaluacionForm` para registrar y editar evaluaciones.
- Se agregaron validaciones para materia obligatoria, periodo obligatorio, nombre obligatorio y peso mayor que cero.
- Se creo `NotaForm` para registrar y editar calificaciones.
- Se agregaron validaciones para matricula obligatoria, evaluacion obligatoria y calificacion entre 0 y 20.
- Se agrego validacion para evitar duplicar una nota con la misma matricula y evaluacion.
- Se configuraron etiquetas y mensajes de error claros en ambos formularios.
- No se tocaron asistencia ni reportes generales.

## Subfase 4.4

### Prompt usado

```text
Desarrolla la subfase 4.4 del proyecto.

Necesito crear las vistas para gestionar evaluaciones.

Requisitos:
- Trabajar en la app notas.
- Crear vistas para:
  - listar_evaluaciones
  - crear_evaluacion
  - editar_evaluacion
  - desactivar_evaluacion
- Usar EvaluacionForm.
- Usar django.contrib.messages.
- No borrar evaluaciones, solo cambiar estado a inactivo.
- Ordenar evaluaciones por materia, periodo y nombre.
- No crear todavia reportes generales.

Quiero que me indiques:
1. Codigo completo o actualizado de views.py.
2. Explicacion de cada vista.
3. Validaciones aplicadas.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.4
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon las vistas para gestionar evaluaciones dentro de la app `notas`. Las vistas permiten listar, registrar, editar y desactivar evaluaciones usando `EvaluacionForm`, mensajes de Django y desactivacion logica mediante el campo `estado`.

### Cambios realizados

- Se actualizo `notas/views.py`.
- Se agrego la vista `listar_evaluaciones`.
- Se agrego la vista `crear_evaluacion`.
- Se agrego la vista `editar_evaluacion`.
- Se agrego la vista `desactivar_evaluacion`.
- Se uso `EvaluacionForm` para crear y editar evaluaciones.
- Se uso `django.contrib.messages` para mostrar mensajes de exito y error.
- Se ordenaron las evaluaciones por materia, periodo y nombre.
- Se configuro la desactivacion para cambiar el estado a `inactivo` sin borrar registros.
- No se crearon reportes generales.

## Subfase 4.5

### Prompt usado

```text
Desarrolla la subfase 4.5 del proyecto.

Necesito crear las vistas para registrar y consultar notas.

Requisitos:
- Trabajar en la app notas.
- Crear vistas para:
  - listar_notas
  - registrar_nota
  - editar_nota
  - detalle_nota
  - notas_por_estudiante
  - notas_por_materia
- Usar NotaForm.
- Usar django.contrib.messages.
- Validar nota entre 0 y 20.
- Evitar notas duplicadas.
- Mostrar informacion relacionada:
  - estudiante
  - materia
  - periodo
  - evaluacion
  - calificacion
- Ordenar notas por estudiante, materia y evaluacion.

Quiero que me indiques:
1. Codigo completo o actualizado de views.py.
2. Explicacion de cada vista.
3. Validaciones aplicadas.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.5
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon las vistas para registrar, editar, detallar y consultar notas dentro de la app `notas`. Las vistas usan `NotaForm`, mensajes de Django y consultas optimizadas con relaciones hacia estudiante, materia, periodo y evaluacion.

### Cambios realizados

- Se actualizo `notas/views.py`.
- Se agrego la vista `listar_notas`.
- Se agrego la vista `registrar_nota`.
- Se agrego la vista `editar_nota`.
- Se agrego la vista `detalle_nota`.
- Se agrego la vista `notas_por_estudiante`.
- Se agrego la vista `notas_por_materia`.
- Se uso `NotaForm` para registrar y editar notas.
- Se usaron mensajes de exito y error con `django.contrib.messages`.
- Se reutilizaron las validaciones de `NotaForm` para rango de calificacion entre 0 y 20 y notas duplicadas.
- Se incluyo informacion relacionada de estudiante, materia, periodo, evaluacion y calificacion mediante consultas con `select_related`.
- Se ordenaron las notas por estudiante, materia y evaluacion.

## Subfase 4.6

### Prompt usado

```text
Desarrolla la subfase 4.6 del proyecto.

Necesito agregar la logica para calcular promedios academicos.

Requisitos:
- Trabajar en la app notas.
- Crear funciones auxiliares para:
  - calcular promedio simple por matricula
  - calcular promedio ponderado por matricula usando el peso de evaluaciones
  - determinar estado aprobado o desaprobado
- La nota minima aprobatoria sera 11.
- Si no hay notas, el promedio debe mostrarse como pendiente.
- Crear una vista llamada promedio_matricula.
- Crear una vista llamada promedios_por_materia.
- Mostrar:
  - estudiante
  - materia
  - periodo
  - promedio
  - estado: aprobado, desaprobado o pendiente
- Evitar errores si faltan notas o evaluaciones.

Quiero que me indiques:
1. Codigo completo de las funciones de promedio.
2. Codigo actualizado de views.py.
3. Explicacion del calculo usado.
4. Comando para probar que no hay errores.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.6
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se agrego la logica de promedios academicos para el modulo `notas`. Se crearon funciones auxiliares para calcular promedio simple, promedio ponderado y estado academico, ademas de vistas para consultar el promedio de una matricula y los promedios por materia.

### Cambios realizados

- Se creo el archivo `notas/utils.py`.
- Se agrego la constante de nota minima aprobatoria `11.00`.
- Se creo la funcion `calcular_promedio_simple_por_matricula`.
- Se creo la funcion `calcular_promedio_ponderado_por_matricula`.
- Se creo la funcion `determinar_estado_promedio`.
- Se configuro el estado como `aprobado`, `desaprobado` o `pendiente`.
- Se actualizo `notas/views.py`.
- Se agrego la vista `promedio_matricula`.
- Se agrego la vista `promedios_por_materia`.
- Se incluyo estudiante, materia, periodo, promedio y estado en el contexto de las vistas.
- Se manejo el caso sin notas mostrando el promedio como `pendiente`.
- Se evito error por falta de pesos validos usando el promedio simple como respaldo.

## Subfase 4.7

### Prompt usado

```text
Desarrolla la subfase 4.7 del proyecto.

Necesito configurar las rutas del modulo notas.

Requisitos:
- Trabajar en notas/urls.py.
- Crear rutas para evaluaciones:
  - /notas/evaluaciones/
  - /notas/evaluaciones/crear/
  - /notas/evaluaciones/<id>/editar/
  - /notas/evaluaciones/<id>/desactivar/
- Crear rutas para notas:
  - /notas/
  - /notas/registrar/
  - /notas/<id>/
  - /notas/<id>/editar/
  - /notas/estudiante/<id>/
  - /notas/materia/<id>/
- Crear rutas para promedios:
  - /notas/promedios/matricula/<id>/
  - /notas/promedios/materia/<id>/
- Verificar que config/urls.py incluya las rutas de notas.
- Usar nombres de rutas claros.

Quiero que me indiques:
1. Codigo completo de notas/urls.py.
2. Si se modifica config/urls.py, mostrar el codigo necesario.
3. Explicacion de cada ruta.
4. Comando para probar.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.7
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se configuraron las rutas del modulo `notas` para evaluaciones, notas y promedios. Tambien se verifico que `config/urls.py` ya incluye las rutas de la app mediante `path('notas/', include('notas.urls'))`.

### Cambios realizados

- Se actualizo `notas/urls.py`.
- Se configuro `/notas/` para listar notas.
- Se agregaron rutas para registrar, ver, editar y consultar notas por estudiante o materia.
- Se agregaron rutas para listar, crear, editar y desactivar evaluaciones.
- Se agregaron rutas para consultar promedio por matricula y promedios por materia.
- Se usaron nombres de rutas claros y consistentes con las vistas.
- Se verifico que `config/urls.py` ya incluye `notas.urls`, por lo que no fue necesario modificarlo.

## Subfase 4.8

### Prompt usado

```text
Desarrolla la subfase 4.8 del proyecto.

Necesito crear los templates HTML del modulo notas.

Requisitos:
- Crear carpeta templates/notas/ si no existe.
- Crear templates para evaluaciones:
  - evaluaciones_lista.html
  - evaluacion_formulario.html
  - evaluacion_confirmar_desactivar.html
- Crear templates para notas:
  - notas_lista.html
  - nota_formulario.html
  - nota_detalle.html
  - notas_por_estudiante.html
  - notas_por_materia.html
- Crear templates para promedios:
  - promedio_matricula.html
  - promedios_por_materia.html
- Usar estructura simple.
- Si existe base.html, extenderlo.
- Incluir botones de volver, editar y registrar.
- Mostrar mensajes de exito o error.
- Mostrar aprobado/desaprobado de forma clara.

Quiero que me indiques:
1. Codigo completo de cada template.
2. Como se conectan con las vistas.
3. Como probar en el navegador.
4. Mensaje de commit recomendado.
5. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.8
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon los templates HTML del modulo `notas` para evaluaciones, notas y promedios. No existe un `base.html` en el proyecto, por lo que se usaron documentos HTML completos y simples, siguiendo la estructura de los templates existentes de `academico` y `estudiantes`.

### Cambios realizados

- Se creo la carpeta `templates/notas/`.
- Se creo `evaluaciones_lista.html`.
- Se creo `evaluacion_formulario.html`.
- Se creo `evaluacion_confirmar_desactivar.html`.
- Se creo `notas_lista.html`.
- Se creo `nota_formulario.html`.
- Se creo `nota_detalle.html`.
- Se creo `notas_por_estudiante.html`.
- Se creo `notas_por_materia.html`.
- Se creo `promedio_matricula.html`.
- Se creo `promedios_por_materia.html`.
- Se agregaron enlaces de volver, editar, registrar y consultar promedios segun corresponda.
- Se agrego visualizacion de mensajes de Django en los templates.
- Se mostro el estado del promedio como aprobado, desaprobado o pendiente.
- Se mantuvo una ruta `notas:index` apuntando al listado de notas para conservar compatibilidad con el enlace existente en la pagina de inicio.

## Subfase 4.9

### Prompt usado

```text
Desarrolla la subfase 4.9 del proyecto.

Necesito probar el modulo de notas y dejar evidencia.

Requisitos:
- Verificar que el servidor Django corre sin errores.
- Probar registro de evaluacion.
- Probar error por peso invalido.
- Probar registro de nota.
- Probar error por nota menor que 0.
- Probar error por nota mayor que 20.
- Probar error por nota duplicada.
- Probar edicion de nota.
- Probar consulta de notas por estudiante.
- Probar consulta de notas por materia.
- Probar calculo de promedio.
- Probar estado aprobado si promedio es mayor o igual a 11.
- Probar estado desaprobado si promedio es menor a 11.
- Crear o actualizar archivo de pruebas.

Archivo sugerido:
evidencias/integrante_4_pruebas.md

Debe contener:
- Caso probado
- Datos ingresados
- Resultado esperado
- Resultado obtenido
- Estado: correcto o corregido

Quiero que me indiques:
1. Lista de pruebas a realizar.
2. Contenido sugerido para integrante_4_pruebas.md.
3. Errores comunes y como solucionarlos.
4. Comando para correr el servidor.
5. Mensaje de commit recomendado.
6. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_4_prompts.md

Agrega:
- Subfase 4.9
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se probaron las funcionalidades principales del modulo `notas`: servidor, evaluaciones, registro y edicion de notas, validaciones, consultas y promedios academicos. Tambien se creo el archivo `evidencias/integrante_4_pruebas.md` con los casos probados, datos ingresados, resultados esperados, resultados obtenidos y estado de cada prueba.

### Cambios realizados

- Se verifico que Django ejecuta `manage.py check` sin errores.
- Se levanto el servidor local en `127.0.0.1:8020`.
- Se verifico respuesta `HTTP/1.1 200 OK` para `/notas/` y `/notas/evaluaciones/`.
- Se probaron formularios de evaluacion y nota con datos temporales.
- Se probaron errores por peso invalido, nota menor que 0, nota mayor que 20 y nota duplicada.
- Se probaron consultas por estudiante y por materia.
- Se probaron calculos de promedio y estados `aprobado`, `desaprobado` y `pendiente`.
- Se creo `evidencias/integrante_4_pruebas.md`.

## Tarea extra: resumen de notas

### Prompt usado

```text
Estoy trabajando en el sistema Django de Control Academico.

Yo soy el Integrante 4 y desarrolle el modulo de notas. Ahora necesito agregar el resumen de notas dentro de la app reportes.

Requisitos:
- Trabajar en la app reportes.
- Crear una vista llamada resumen_notas.
- Usar los modelos existentes:
  - Evaluacion
  - Nota
  - Matricula
  - Materia
  - PeriodoAcademico
  - Estudiante
- El resumen debe mostrar:
  - total de evaluaciones
  - total de notas registradas
  - promedio general
  - cantidad de aprobados
  - cantidad de desaprobados
  - listado de estudiantes con promedio si se puede calcular
- Nota minima aprobatoria: 11.
- Manejar el caso donde no existan notas registradas.
- Crear template reportes/resumen_notas.html.
- Crear o actualizar ruta.
- Agregar enlace desde el panel de reportes si todavia no existe.
- No modificar la logica interna del modulo notas salvo que sea estrictamente necesario.
```

### Resumen de lo generado

Se creo la vista `resumen_notas` en `reportes/views.py`, la ruta `reportes/resumen-notas/` en `reportes/urls.py` y el template `reportes/resumen_notas.html`. La vista consulta el modelo `Evaluacion` para el total de evaluaciones, el modelo `Nota` para el total de notas registradas y el promedio general (`Avg` de calificacion). Para cada estudiante con al menos una nota, se calcula su promedio individual y se clasifica como aprobado (promedio >= 11) o desaprobado (promedio < 11). El template muestra indicadores generales y una tabla con el listado de estudiantes, su promedio y estado academico. Se maneja el caso sin notas con mensajes informativos. Se actualizo el enlace del panel de reportes para que la tarjeta "Resumen de notas" apunte a la nueva vista.

### Cambios realizados

- Se agrego la vista `resumen_notas` en `reportes/views.py`.
- Se importo el modelo `Evaluacion` y la constante `NOTA_MINIMA_APROBATORIA` en `reportes/views.py`.
- Se agrego la ruta `resumen-notas/` en `reportes/urls.py`.
- Se creo el template `templates/reportes/resumen_notas.html`.
- Se actualizo el enlace en `panel_reportes.html` de `notas:listar_notas` a `reportes:resumen_notas`.
- No se modifico la logica interna del modulo notas.
