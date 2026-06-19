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

## Subfase 1.3

### Prompt usado

```text
Desarrolla la subfase 1.3 del proyecto.

Necesito conectar Django con la base de datos MySQL que esta corriendo en Docker.

Requisitos:
- Django debe dejar de usar SQLite.
- Configurar la base de datos MySQL en settings.py.
- Leer las credenciales desde un archivo .env.
- Usar python-dotenv.
- Usar PyMySQL o mysqlclient, elige la opcion mas facil de instalar y explicar.
- Actualizar requirements.txt.
- Configurar SECRET_KEY, DEBUG y ALLOWED_HOSTS desde variables de entorno.
- Mantener la zona horaria America/Lima.
- Ejecutar migraciones iniciales correctamente.

Variables esperadas:
DB_NAME=control_academico_db
DB_USER=django_user
DB_PASSWORD=django_password
DB_HOST=127.0.0.1
DB_PORT=3307

Quiero que me indiques:
1. Dependencias necesarias.
2. Cambios en settings.py.
3. Si se usa PyMySQL, indicar donde configurarlo.
4. Comandos para instalar dependencias.
5. Comando para correr migraciones.
6. Como verificar que Django ya esta usando MySQL.
7. Mensaje de commit recomendado.
8. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_1_prompts.md

Agrega:
- Subfase 1.3
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se configuro Django para usar MySQL en lugar de SQLite. La configuracion carga variables desde `.env` mediante `python-dotenv`, usa `PyMySQL` como adaptador compatible con el backend MySQL de Django, y deja `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` y las credenciales de base de datos fuera del codigo fuente.

### Cambios realizados

- Se agregaron las dependencias `PyMySQL` y `python-dotenv` en `requirements.txt`.
- Se configuro la carga del archivo `.env` en `config/settings.py`.
- Se cambio `DATABASES` para usar `django.db.backends.mysql`.
- Se configuraron `SECRET_KEY`, `DEBUG` y `ALLOWED_HOSTS` desde variables de entorno.
- Se mantuvo la zona horaria `America/Lima`.
- Se agrego la configuracion de `PyMySQL` en `config/__init__.py`.
- Se actualizo `.env.example` con variables de Django y MySQL.
- Se creo un archivo `.env` local para desarrollo, ignorado por Git.

## Subfase 1.4

### Prompt usado

```text
Desarrolla la subfase 1.4 del proyecto.

Necesito crear las apps principales del sistema de Control Academico, pero sin desarrollar todavia sus modelos internos.

Apps requeridas:
- estudiantes
- academico
- notas
- asistencia
- reportes

Requisitos:
- Crear las apps con manage.py.
- Registrarlas en INSTALLED_APPS.
- Crear archivo urls.py basico en cada app.
- Conectar las URLs de cada app en config/urls.py.
- Crear una vista simple temporal para cada app.
- Crear enlaces desde la pagina de inicio hacia cada modulo.
- No crear todavia modelos de estudiantes, materias, notas, asistencia ni reportes.

Quiero que me indiques:
1. Comandos para crear cada app.
2. Archivos que se modifican.
3. Codigo completo de urls.py y views.py basicos.
4. Codigo actualizado de config/urls.py.
5. Codigo actualizado de la pagina de inicio con enlaces.
6. Comando para probar.
7. Mensaje de commit recomendado.
8. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_1_prompts.md

Agrega:
- Subfase 1.4
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se crearon las apps principales del sistema de Control Academico: `estudiantes`, `academico`, `notas`, `asistencia` y `reportes`. Cada app quedo registrada en Django, con una ruta basica y una vista temporal para confirmar que el modulo responde.

### Cambios realizados

- Se crearon las apps `estudiantes`, `academico`, `notas`, `asistencia` y `reportes`.
- Se registraron las apps en `INSTALLED_APPS`.
- Se creo un archivo `urls.py` basico en cada app.
- Se agrego una vista temporal `index` en cada app.
- Se conectaron las rutas de cada app en `config/urls.py`.
- Se agregaron enlaces desde la pagina de inicio hacia cada modulo.
- No se crearon modelos de estudiantes, materias, notas, asistencia ni reportes.
