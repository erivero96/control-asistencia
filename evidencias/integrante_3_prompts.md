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
