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
