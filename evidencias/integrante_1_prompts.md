# Evidencias - Integrante 1

## Subfase 1.1

### Prompt usado

```text
Desarrolla la subfase 1.1 del proyecto.

Necesito crear la base de un proyecto Django para un sistema web de Control Academico.

Requisitos:
- Crear proyecto Django llamado config.
- Crear una app inicial llamada core.
- Configurar una vista de inicio simple.
- Configurar una URL principal para mostrar la pagina de inicio.
- Configurar idioma espanol.
- Configurar zona horaria America/Lima.
- Crear carpetas base templates y static.
- Crear un template simple para la pagina de inicio.
- No crear todavia modelos de estudiantes, notas, asistencia ni reportes.

Quiero que me indiques:
1. Comandos exactos para crear el proyecto.
2. Archivos que se deben modificar.
3. Codigo completo de cada archivo modificado.
4. Comando para probar que funciona.
5. Mensaje de commit recomendado.
6. Breve explicacion para poder defender esta parte.

Tambien crea o actualiza un archivo de evidencia en:
evidencias/integrante_1_prompts.md

Ahi debes registrar:
- Subfase 1.1
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo la base inicial de un proyecto Django para el sistema web de Control Academico. El proyecto principal se llama `config`, la app inicial se llama `core`, y se configuro una pagina de inicio simple accesible desde la ruta principal `/`.

### Cambios realizados

- Se creo el proyecto Django `config`.
- Se creo la app inicial `core`.
- Se registro la app `core` en `INSTALLED_APPS`.
- Se configuro el directorio global `templates`.
- Se configuro el directorio base `static`.
- Se configuro el idioma en espanol.
- Se configuro la zona horaria `America/Lima`.
- Se creo la vista `home`.
- Se creo la ruta principal para mostrar la pagina de inicio.
- Se creo el template `templates/core/home.html`.
- No se crearon modelos de estudiantes, notas, asistencia ni reportes.
