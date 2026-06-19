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

## Subfase 1.2

### Prompt usado

```text
Desarrolla la subfase 1.2 del proyecto.

Necesito dockerizar la base de datos MySQL para el proyecto Django de Control Academico.

Requisitos:
- Crear un archivo docker-compose.yml.
- Usar MySQL 8.
- Crear una base de datos llamada control_academico_db.
- Crear usuario django_user.
- Crear contrasena django_password.
- Usar root password root_password.
- Exponer MySQL en el puerto 3307 de mi maquina.
- Usar volumen persistente para no perder datos.
- Agregar healthcheck basico.
- Crear archivo .env.example con las variables necesarias.
- No incluir credenciales reales sensibles.
- No dockerizar todavia Django, solo la base de datos.

Quiero que me indiques:
1. Contenido completo de docker-compose.yml.
2. Contenido completo de .env.example.
3. Comandos para levantar la base de datos.
4. Comandos para detener la base de datos.
5. Como verificar que MySQL esta corriendo.
6. Mensaje de commit recomendado.
7. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_1_prompts.md

Agrega:
- Subfase 1.2
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se dockerizo un servicio de base de datos MySQL 8 para el proyecto de Control Academico. La base de datos queda preparada con nombre `control_academico_db`, usuario `django_user`, puerto local `3307`, volumen persistente y healthcheck basico.

### Cambios realizados

- Se creo el archivo `docker-compose.yml`.
- Se definio un servicio `mysql` usando la imagen `mysql:8.0`.
- Se configuraron variables para base de datos, usuario y contrasenas de desarrollo.
- Se expuso MySQL en el puerto local `3307`.
- Se agrego el volumen persistente `control_academico_mysql_data`.
- Se agrego un healthcheck con `mysqladmin ping`.
- Se creo `.env.example` con variables de ejemplo.
- No se dockerizo Django en esta subfase.
