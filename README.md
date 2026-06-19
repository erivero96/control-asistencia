# Sistema de Control Academico

Aplicacion web base desarrollada con Python y Django para un sistema de Control Academico.

Esta etapa contiene la configuracion tecnica inicial del proyecto. Aun no se han desarrollado los modelos internos ni la logica de negocio de estudiantes, materias, notas, asistencia o reportes.

## Tecnologias

- Python 3
- Django 6.0.6
- MySQL 8
- Docker Compose
- PyMySQL
- python-dotenv

## Requisitos Previos

- Python 3 instalado
- Docker y Docker Compose instalados
- Git instalado

## Instalacion Desde Cero

Clonar el repositorio:

```bash
git clone https://github.com/erivero96/control-asistencia.git
cd control-asistencia
```

Crear entorno virtual:

```bash
python3 -m venv .venv
```

Activar entorno virtual en Linux o macOS:

```bash
source .venv/bin/activate
```

Activar entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Copiar variables de entorno:

```bash
cp .env.example .env
```

Levantar MySQL con Docker:

```bash
docker compose up -d mysql
```

Ejecutar migraciones iniciales:

```bash
python manage.py migrate
```

Correr el servidor Django:

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Verificacion Rapida

Verificar configuracion general de Django:

```bash
python manage.py check
```

Verificar que MySQL este corriendo:

```bash
docker compose ps
```

Verificar que Django usa MySQL:

```bash
python manage.py shell -c "from django.db import connection; print(connection.vendor); print(connection.settings_dict['ENGINE'])"
```

## Variables de Entorno

El archivo `.env` no debe subirse al repositorio. Se debe crear desde `.env.example`.

Variables principales:

```env
SECRET_KEY=django-insecure-dev-only-change-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=control_academico_db
DB_USER=django_user
DB_PASSWORD=django_password
DB_HOST=127.0.0.1
DB_PORT=3307
```

## Estructura del Proyecto

```text
config/        Configuracion principal de Django.
core/          App base con la pagina de inicio.
estudiantes/   App creada para el futuro modulo de estudiantes.
academico/     App creada para el futuro modulo academico.
notas/         App creada para el futuro modulo de notas.
asistencia/    App creada para el futuro modulo de asistencia.
reportes/      App creada para el futuro modulo de reportes.
templates/     Plantillas HTML del proyecto.
static/        Archivos estaticos base.
evidencias/    Registro de prompts y uso de IA.
docker-compose.yml  Servicio MySQL dockerizado.
requirements.txt    Dependencias Python.
```

## Trabajo Realizado por el Integrante 1

- Creacion del proyecto Django `config`.
- Creacion de la app base `core`.
- Configuracion de idioma espanol y zona horaria `America/Lima`.
- Creacion de carpetas base `templates` y `static`.
- Dockerizacion de MySQL 8.
- Conexion de Django con MySQL usando variables de entorno.
- Creacion de las apps principales del sistema.
- Configuracion de rutas basicas y vistas temporales.
- Documentacion tecnica inicial.
- Registro de evidencias de uso de IA.

## Alcance Actual

El proyecto contiene solo la base tecnica. Las apps `estudiantes`, `academico`, `notas`, `asistencia` y `reportes` existen como estructura inicial, pero aun no tienen modelos internos ni funcionalidades finales.
