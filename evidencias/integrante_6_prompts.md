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
