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

## Subfase 1.5

### Prompt usado

```text
Desarrolla la subfase 1.5 del proyecto.

Necesito crear la documentacion tecnica inicial del proyecto Django de Control Academico.

Requisitos:
- Crear README.md.
- Crear AGENTS.md.
- Crear carpeta evidencias si no existe.
- Crear archivo evidencias/integrante_1_prompts.md si no existe.
- Explicar como instalar dependencias.
- Explicar como crear y activar entorno virtual.
- Explicar como copiar .env.example a .env.
- Explicar como levantar MySQL con Docker.
- Explicar como ejecutar migraciones.
- Explicar como correr el servidor Django.
- Explicar la estructura de carpetas del proyecto.
- Explicar que parte hizo el Integrante 1.

No inventes modulos que aun no estan desarrollados. Solo documenta la base creada.

Quiero que me indiques:
1. Contenido completo de README.md.
2. Contenido completo de AGENTS.md.
3. Comandos finales para correr el proyecto desde cero.
4. Mensaje de commit recomendado.
5. Breve explicacion para defensa.

Tambien actualiza:
evidencias/integrante_1_prompts.md

Agrega:
- Subfase 1.5
- Prompt usado
- Resumen de lo generado
- Cambios realizados
```

### Resumen de lo generado

Se creo la documentacion tecnica inicial del proyecto. El `README.md` explica como instalar dependencias, configurar el entorno, levantar MySQL, ejecutar migraciones y correr Django. Tambien se creo `AGENTS.md` con reglas de trabajo para mantener la base tecnica ordenada.

### Cambios realizados

- Se actualizo `README.md` con instrucciones de instalacion y ejecucion.
- Se creo `AGENTS.md` con pautas de trabajo para el repositorio.
- Se verifico que la carpeta `evidencias` existe.
- Se actualizo `evidencias/integrante_1_prompts.md` con la subfase 1.5.
- Se documento la estructura de carpetas del proyecto.
- Se documento el alcance del trabajo realizado por el Integrante 1.
- No se documentaron funcionalidades internas que aun no han sido desarrolladas.

## Subfase 1.6

### Prompt usado

```text
Desarrolla la subfase 1.6 del proyecto.

Necesito crear un diseño visual global para todo el sistema Django.

Requisitos:
- Crear o mejorar templates/base.html.
- Crear archivo static/css/styles.css.
- Configurar correctamente la carga de archivos estáticos con {% load static %}.
- Agregar estructura general: header, menú de navegación, contenedor principal, bloque de mensajes y footer simple.
- Agregar enlaces a Inicio, Estudiantes, Académico, Notas, Asistencia y Reportes.
- El diseño debe ser simple, ordenado y usable.
- No modificar la lógica de las vistas.
```

### Resumen de lo generado

Se implementó un diseño visual global y reutilizable para el Sistema de Control Académico. La plantilla base centraliza la estructura común y todas las pantallas de los módulos la heredan para mantener una apariencia consistente.

### Cambios realizados

- Se mejoró `templates/base.html` con encabezado, menú de navegación, contenedor principal, mensajes del sistema y pie de página.
- Se creó `static/css/styles.css` con estilos generales para navegación, formularios, tablas, mensajes, fichas de detalle y diseño adaptable.
- Se configuró la carga del CSS mediante `{% load static %}` y `{% static 'css/styles.css' %}`.
- Se migraron las plantillas de estudiantes, académico, notas, asistencia y reportes para que hereden de `base.html`, sin cambiar sus enlaces, variables ni formularios.
- Se ajustó la configuración de estáticos para que el CSS se cargue desde cualquier ruta local del sistema.
- No se modificaron modelos, vistas, rutas de los módulos, formularios ni lógica de negocio.

## Subfase 1.7

### Prompt usado

```text
Desarrolla la subfase 1.7 del proyecto.

Necesito que todos los templates del sistema usen la plantilla base y el CSS global.

Requisitos:
- Revisar templates de core, estudiantes, academico, notas, asistencia y reportes.
- Hacer que todos extiendan templates/base.html y usen los bloques title y content.
- Aplicar clases CSS comunes a tablas, formularios, botones, tarjetas, mensajes, páginas de detalle y páginas de confirmación.
- No cambiar nombres de rutas, lógica de vistas ni datos mostrados.
```

### Resumen de lo generado

Se consolidó el uso de la plantilla base y del CSS global en todos los módulos. Las pantallas ahora usan clases visuales reutilizables para que tablas, formularios, botones, tarjetas, mensajes, detalles y confirmaciones mantengan el mismo estilo.

### Cambios realizados

- Se verificó que las 36 plantillas de contenido extiendan `base.html`; `base.html` permanece como el único documento HTML principal.
- Se aplicaron las clases `tabla-datos`, `formulario`, `boton`, `tarjeta`, `mensajes`, `detalle`, `pagina-detalle` y `pagina-confirmacion` según el tipo de contenido.
- Se ampliaron los selectores de `static/css/styles.css` para mantener estilos comunes y adaptables con esas clases.
- Se conservaron los bloques `title` y `content`, las rutas, los formularios, las variables de contexto y los datos ya mostrados.
- No se modificó la lógica de las vistas.

## Subfase 1.8

### Prompt usado

```text
Desarrolla la subfase 1.8 del proyecto.

Necesito mejorar visualmente los formularios, tablas y botones del sistema.

Requisitos:
- Mejorar estilos de formularios, tablas, botones y mensajes de éxito y error.
- Estilizar acciones de registrar, editar, volver, desactivar, retirar, guardar y cancelar.
- Agregar diseño responsive básico, colores sobrios y diseño académico.
- No modificar la lógica del sistema.
```

### Resumen de lo generado

Se refinó la interfaz de captura y consulta de datos con formularios más claros, tablas legibles y botones con variantes visuales según su acción. La interfaz conserva una paleta académica sobria y se adapta mejor a pantallas pequeñas.

### Cambios realizados

- Se añadieron variantes de botón para acciones principales, edición, volver o cancelar y acciones de peligro.
- Se aplicaron esas variantes a los enlaces y botones de registrar, editar, ver, guardar, cancelar, desactivar y retirar existentes.
- Se mejoraron los estados de enfoque y desplazamiento de campos de formulario.
- Se reforzaron la legibilidad de tablas, acciones por fila y mensajes de éxito, error, advertencia e información.
- Se ajustaron formularios, botones y tablas para pantallas pequeñas mediante reglas responsive.
- No se modificaron vistas, rutas, formularios de Django ni lógica de negocio.

## Subfase 1.9

### Prompt usado

```text
Desarrolla la subfase 1.9 del proyecto.

Necesito implementar login y logout en el sistema Django usando el sistema de autenticación propio de Django.

Requisitos:
- Usar django.contrib.auth.
- Crear templates registration/login.html y registration/logged_out.html si es necesario.
- Configurar rutas de login y logout, LOGIN_URL, LOGIN_REDIRECT_URL y LOGOUT_REDIRECT_URL.
- Mostrar el usuario autenticado y los controles de iniciar o cerrar sesión en base.html.
- Mantener el CSS global y no crear roles complejos.
```

### Resumen de lo generado

Se incorporó autenticación básica mediante las vistas estándar de `django.contrib.auth`. El sistema muestra el estado de sesión en la cabecera y mantiene la misma interfaz visual en las pantallas de acceso y cierre de sesión.

### Cambios realizados

- Se configuraron las rutas `cuentas/login/` y `cuentas/logout/` con `LoginView` y `LogoutView` de Django.
- Se agregaron `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` en `config/settings.py`.
- Se crearon las plantillas `registration/login.html` y `registration/logged_out.html` usando `base.html` y el CSS global.
- Se añadieron controles de iniciar sesión, nombre de usuario y cierre de sesión por POST en la cabecera.
- Se añadieron estilos de autenticación y diseño adaptable en `static/css/styles.css`.
- No se crearon roles, modelos nuevos ni lógica de autorización compleja.

## Subfase 1.10

### Prompt usado

```text
Desarrolla la subfase 1.10 del proyecto.

Necesito mejorar el diseño visual de la pantalla de login.

Requisitos:
- Usar el CSS global y crear una tarjeta centrada para el formulario.
- Mostrar el título Sistema de Control Académico, campos ordenados, errores claros y botón para ingresar.
- Mantener un diseño simple, limpio y académico.
- No modificar la lógica de autenticación.
```

### Resumen de lo generado

Se refinó la presentación de la pantalla de acceso con una tarjeta centrada, jerarquía visual académica y mensajes de error más visibles. La autenticación continúa usando las mismas vistas y formulario estándar de Django.

### Cambios realizados

- Se mejoró `registration/login.html` con etiquetas específicas de acceso, descripción y alerta accesible de errores.
- Se reforzó la tarjeta de login en `styles.css` con borde superior, sombra sobria, espaciado y campos visualmente ordenados.
- Se ajustó la tarjeta para pantallas pequeñas sin alterar el comportamiento del formulario.
- No se modificaron rutas, vistas, credenciales ni lógica de autenticación.
