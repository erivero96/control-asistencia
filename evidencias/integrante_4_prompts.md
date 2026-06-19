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
