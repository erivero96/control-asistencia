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
