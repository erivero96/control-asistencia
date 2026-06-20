# Evidencias - Integrante 6

## Subfase 6.1

### Prompt usado

```text
Desarrolla la subfase 6.1 del proyecto.

Necesito crear la base del módulo de reportes para el sistema web de Control Académico en Django.

Requisitos:
- Trabajar en la app reportes.
- Crear una vista principal llamada panel_reportes.
- La vista debe mostrar accesos a:
  - reporte por estudiante
  - reporte por materia
  - reporte por periodo
  - resumen de notas
  - resumen de asistencia
- No calcular todavía todos los datos detallados.
- Crear o actualizar reportes/urls.py.
- Verificar que config/urls.py incluya las rutas de reportes.
- Crear un template simple para el panel principal.

También crea o actualiza evidencias/integrante_6_prompts.md con la subfase, prompt, resumen y cambios realizados.
```

### Resumen de lo generado

Se creó la base visual del módulo `reportes` mediante la vista `panel_reportes`. Esta vista muestra un panel con las cinco opciones de consulta solicitadas, sin realizar todavía cálculos ni consultas detalladas de notas o asistencia.

### Cambios realizados

- Se actualizó `reportes/views.py` para crear la vista `panel_reportes` con `render`.
- Se actualizó `reportes/urls.py` para asociar la ruta principal de reportes con `panel_reportes`.
- Se mantuvo el nombre de ruta `index` como alias de compatibilidad para la navegación ya existente desde la página principal.
- Se creó `templates/reportes/panel_reportes.html` con las opciones de reporte por estudiante, materia, periodo, resumen de notas y resumen de asistencia.
- Se verificó que `config/urls.py` ya incluye la ruta `reportes/`; no fue necesario modificarlo.
- No se crearon modelos ni se modificó la lógica de los módulos de estudiantes, académico, notas o asistencia.

## Subfase 6.2

### Prompt usado

```text
Desarrolla la subfase 6.2 del proyecto.

Necesito crear el reporte académico por estudiante.

Requisitos:
- Trabajar en la app reportes.
- Usar los modelos existentes:
  - Estudiante
  - Matricula
  - Nota
  - Asistencia
- Crear una vista reporte_estudiante.
- El reporte debe mostrar:
  - datos del estudiante
  - materias matriculadas
  - periodo académico
  - notas registradas
  - promedio por materia si existe
  - estado aprobado, desaprobado o pendiente
  - resumen de asistencia si existe
- Debe manejar el caso de estudiante sin matrículas.
- Debe manejar el caso de estudiante sin notas.
- Debe manejar el caso de estudiante sin asistencia.
- Crear template reporte_estudiante.html.

Quiero que me indiques:
1. Código completo o actualizado de views.py.
2. Código del template.
3. Código de la ruta necesaria.
4. Explicación de cómo se obtienen los datos.
5. Comando para probar.
6. Mensaje de commit recomendado.
7. Breve explicación para defensa.

También actualiza:
evidencias/integrante_6_prompts.md

Agrega:
- Subfase 6.2
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creó el reporte académico por estudiante. El reporte reúne las matrículas del estudiante con su materia y periodo, las notas registradas, el promedio ponderado y estado académico, además del resumen de asistencia por cada materia.

### Cambios realizados

- Se agregó la vista `reporte_estudiante` en `reportes/views.py`.
- Se reutilizaron los modelos `Estudiante`, `Matricula`, `Nota` y `Asistencia` sin modificar sus definiciones.
- Se reutilizaron las utilidades existentes para calcular el promedio ponderado, el estado académico y el resumen de asistencia.
- Se agregó la ruta `reportes/estudiante/<int:estudiante_id>/` con el nombre `reporte_estudiante`.
- Se creó `templates/reportes/reporte_estudiante.html`.
- Se muestran mensajes adecuados cuando el estudiante no posee matrículas, cuando una materia no tiene notas o cuando no tiene asistencias registradas.

## Subfase 6.3

### Prompt usado

```text
Desarrolla la subfase 6.3 del proyecto.

Necesito crear el reporte académico por materia.

Requisitos:
- Trabajar en la app reportes.
- Usar los modelos existentes:
  - Materia
  - PeriodoAcademico
  - Matricula
  - Nota
  - Asistencia
- Crear una vista reporte_materia.
- El reporte debe permitir ver:
  - datos de la materia
  - estudiantes matriculados
  - periodo académico
  - notas por estudiante
  - promedio por estudiante
  - cantidad de aprobados
  - cantidad de desaprobados
  - resumen básico de asistencia
- Debe manejar el caso de materia sin matrículas.
- Crear template reporte_materia.html.

Quiero que me indiques:
1. Código completo o actualizado de views.py.
2. Código del template.
3. Código de la ruta necesaria.
4. Explicación del cálculo de aprobados y desaprobados.
5. Comando para probar.
6. Mensaje de commit recomendado.
7. Breve explicación para defensa.

También actualiza:
evidencias/integrante_6_prompts.md

Agrega:
- Subfase 6.3
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creó el reporte académico por materia y periodo académico. El reporte presenta los datos de la materia y del periodo seleccionado, los estudiantes matriculados con sus notas, promedio y estado académico, además de los totales de aprobados, desaprobados y un resumen global de asistencia.

### Cambios realizados

- Se agregó la vista `reporte_materia` en `reportes/views.py`.
- Se utilizaron los modelos existentes `Materia`, `PeriodoAcademico`, `Matricula`, `Nota` y `Asistencia`.
- Se reutilizaron las utilidades de notas para calcular el promedio ponderado y determinar el estado académico de cada estudiante.
- Se agregaron los conteos de aprobados, desaprobados y pendientes.
- Se agregó el resumen global de presentes, tardanzas, faltas y justificados para la materia y periodo consultados.
- Se agregó la ruta `reportes/materia/<int:materia_id>/periodo/<int:periodo_id>/` con el nombre `reporte_materia`.
- Se creó `templates/reportes/reporte_materia.html`.
- Se muestra un mensaje cuando no hay matrículas para la materia y periodo seleccionados.

## Subfase 6.4

### Prompt usado

```text
Desarrolla la subfase 6.4 del proyecto.

Necesito crear el reporte por periodo académico.

Requisitos:
- Trabajar en la app reportes.
- Usar los modelos:
  - PeriodoAcademico
  - Matricula
  - Materia
  - Estudiante
  - Nota
  - Asistencia
- Crear una vista reporte_periodo.
- El reporte debe mostrar:
  - nombre del periodo
  - fechas del periodo
  - total de estudiantes matriculados
  - total de materias activas en ese periodo
  - total de matrículas
  - resumen de notas registradas
  - resumen de asistencias registradas
- Debe manejar el caso de periodo sin matrículas.
- Crear template reporte_periodo.html.

Quiero que me indiques:
1. Código completo o actualizado de views.py.
2. Código del template.
3. Código de la ruta necesaria.
4. Explicación de los indicadores mostrados.
5. Comando para probar.
6. Mensaje de commit recomendado.
7. Breve explicación para defensa.

También actualiza:
evidencias/integrante_6_prompts.md

Agrega:
- Subfase 6.4
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creó el reporte por periodo académico. Este presenta los datos del periodo seleccionado, los indicadores de matrículas, estudiantes y materias activas, además del resumen de notas y asistencias registradas únicamente en ese periodo.

### Cambios realizados

- Se agregó la vista `reporte_periodo` en `reportes/views.py`.
- Se utilizaron los modelos existentes `PeriodoAcademico`, `Matricula`, `Materia`, `Estudiante`, `Nota` y `Asistencia`.
- Se agregaron indicadores de total de estudiantes únicos, materias activas con matrículas y matrículas del periodo.
- Se agregó el total de notas y su promedio general de calificaciones.
- Se agregó el resumen de asistencias por estado: presentes, tardanzas, faltas y justificados.
- Se agregó la ruta `reportes/periodo/<int:periodo_id>/` con el nombre `reporte_periodo`.
- Se creó `templates/reportes/reporte_periodo.html`.
- Se muestra un mensaje específico cuando el periodo no tiene matrículas registradas.

## Subfase 6.5

### Prompt usado

```text
Desarrolla la subfase 6.5 del proyecto.

Necesito integrar la navegación general del sistema web de Control Académico.

Requisitos:
- Revisar si existe base.html.
- Si existe, actualizarlo sin romper los módulos.
- Si no existe, crear templates/base.html.
- Agregar menú o barra de navegación con enlaces a:
  - Inicio
  - Estudiantes
  - Materias
  - Periodos
  - Matrículas
  - Evaluaciones
  - Notas
  - Asistencia
  - Reportes
- Actualizar la página de inicio para que se vea como panel principal.
- No modificar la lógica interna de los módulos.
- Mantener diseño simple y entendible.

Quiero que me indiques:
1. Archivos modificados.
2. Código completo de base.html.
3. Código actualizado de la página de inicio si aplica.
4. Cómo verificar que los enlaces funcionan.
5. Mensaje de commit recomendado.
6. Breve explicación para defensa.

También actualiza:
evidencias/integrante_6_prompts.md

Agrega:
- Subfase 6.5
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creó una plantilla base con una barra de navegación para los módulos principales del sistema. La página de inicio ahora hereda esta plantilla y presenta un panel principal con accesos directos a cada módulo.

### Cambios realizados

- Se verificó que no existía una plantilla `base.html`.
- Se creó `templates/base.html` con enlaces a Inicio, Estudiantes, Materias, Periodos, Matrículas, Evaluaciones, Notas, Asistencia y Reportes.
- Se agregó un diseño simple y adaptable para la barra de navegación y las tarjetas del panel.
- Se actualizó `templates/core/home.html` para heredar de `base.html`.
- Se transformó la página de inicio en un panel principal con accesos a los módulos existentes.
- No se modificó la lógica Python ni las rutas de los módulos.

## Subfase 6.6

### Prompt usado

```text
Desarrolla la subfase 6.6 del proyecto.

Necesito realizar pruebas de integración del sistema completo.

Requisitos:
- Probar que el servidor Django inicia sin errores.
- Probar navegación entre módulos.
- Probar flujo completo:
  1. Registrar estudiante.
  2. Registrar materia.
  3. Registrar periodo.
  4. Crear matrícula.
  5. Crear evaluación.
  6. Registrar nota.
  7. Registrar asistencia.
  8. Ver reporte por estudiante.
  9. Ver reporte por materia.
  10. Ver reporte por periodo.
- Probar casos incorrectos:
  - DNI duplicado
  - materia duplicada
  - matrícula duplicada
  - nota fuera de rango
  - asistencia duplicada
  - reporte sin datos
- Crear archivo evidencias/integrante_6_pruebas_integracion.md.

El archivo debe contener caso probado, datos ingresados, resultado esperado,
resultado obtenido y estado: correcto o corregido.

También actualiza evidencias/integrante_6_prompts.md con la subfase, prompt,
resumen y cambios realizados.
```

### Resumen de lo generado

Se agregaron pruebas automatizadas de integración que verifican la navegación principal, el flujo completo de registros y reportes, las validaciones de datos duplicados o fuera de rango y los reportes sin datos. Se creó el registro documentado de resultados de las pruebas.

### Cambios realizados

- Se reemplazó el archivo base de pruebas de `reportes` por pruebas de integración reproducibles con el cliente de Django.
- Se verificó el flujo completo desde el registro de estudiante hasta los tres reportes.
- Se verificaron los casos de DNI, materia, matrícula y asistencia duplicados, además de una nota fuera del rango permitido.
- Se verificaron los reportes de estudiante, materia y periodo sin matrículas.
- Se creó `evidencias/integrante_6_pruebas_integracion.md` con los datos, resultados esperados, resultados obtenidos y estado de cada caso.
- Se detectó y resolvió temporalmente la falta de permisos del usuario de Django para crear la base de pruebas, sin alterar la base de datos real.

## Subfase 6.7

### Prompt usado

```text
Desarrolla la subfase 6.7 del proyecto.

Necesito documentar las evidencias finales de uso de IA y trabajo por roles.

Requisitos:
- Crear o actualizar:
  - evidencias/matriz_roles.md
  - evidencias/prompts_resumen.md
  - evidencias/declaracion_uso_ia.md
- La matriz de roles debe incluir integrante, módulo trabajado, responsabilidad,
  archivos principales y evidencia generada.
- El resumen de prompts debe indicar integrante, subfase, prompt usado,
  cambios realizados y prueba aplicada.
- La declaración de uso de IA debe indicar que la IA fue usada como apoyo, que el
  código fue revisado, adaptado y probado por el equipo.
- No inventar nombres de integrantes. Usar Integrante 1, Integrante 2, etc.
- Mantener redacción sencilla y defendible.

También actualiza evidencias/integrante_6_prompts.md con la subfase, prompt,
resumen y cambios realizados.
```

### Resumen de lo generado

Se consolidó la documentación final de roles, prompts, cambios y pruebas. También se creó una declaración clara sobre el uso responsable de IA como apoyo al trabajo del equipo.

### Cambios realizados

- Se creó `evidencias/matriz_roles.md` con la distribución de responsabilidades de los seis integrantes.
- Se creó `evidencias/prompts_resumen.md` con el resumen de subfases, prompts, cambios y pruebas por integrante.
- Se creó `evidencias/declaracion_uso_ia.md` con la declaración de uso de IA como herramienta de apoyo revisada por el equipo.
- Se mantuvo la identificación por Integrante 1 a Integrante 6, sin inventar nombres personales.
