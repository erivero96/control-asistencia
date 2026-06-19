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
