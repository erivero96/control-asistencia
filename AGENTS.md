# AGENTS.md

## Alcance

Estas instrucciones aplican a todo el repositorio.

## Contexto del Proyecto

Este repositorio contiene la base tecnica de una aplicacion web de Control Academico desarrollada con Django. La base de datos es MySQL 8 ejecutada con Docker Compose.

## Reglas de Trabajo

- No subir `.env`, `.venv`, `db.sqlite3`, archivos `__pycache__` ni credenciales reales.
- Usar `.env.example` como plantilla para variables de entorno.
- Mantener Django fuera de Docker hasta que una subfase posterior lo indique.
- Mantener MySQL en Docker usando `docker-compose.yml`.
- No crear modelos internos de estudiantes, materias, notas, asistencia o reportes hasta que la subfase correspondiente lo solicite.
- Documentar los cambios importantes en `evidencias/integrante_1_prompts.md` cuando correspondan al trabajo del Integrante 1.
- Preferir cambios pequenos y claros, respetando la estructura existente del proyecto.

## Comandos Utiles

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Levantar MySQL:

```bash
docker compose up -d mysql
```

Ejecutar migraciones:

```bash
python manage.py migrate
```

Validar Django:

```bash
python manage.py check
```

Correr servidor:

```bash
python manage.py runserver
```

## Estructura Base

- `config/`: configuracion principal del proyecto.
- `core/`: pagina de inicio.
- `estudiantes/`: estructura base del modulo de estudiantes.
- `academico/`: estructura base del modulo academico.
- `notas/`: estructura base del modulo de notas.
- `asistencia/`: estructura base del modulo de asistencia.
- `reportes/`: estructura base del modulo de reportes.
- `evidencias/`: registro de prompts y uso de IA.
