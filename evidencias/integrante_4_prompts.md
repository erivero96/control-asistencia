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
