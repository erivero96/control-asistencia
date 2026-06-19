# Evidencias de pruebas - Integrante 3

## Subfase 3.8

### Resumen

Se probaron las funciones principales del modulo academico: materias, periodos academicos y matriculas. Las pruebas se realizaron con el servidor de Django y con el cliente de pruebas de Django usando datos temporales con prefijo `T38-`. Al finalizar, los datos temporales fueron eliminados.

### Comandos usados

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py runserver 127.0.0.1:8001
```

Tambien se verifico la respuesta HTTP del modulo academico:

```bash
curl -I http://127.0.0.1:8001/academico/materias/
```

Resultado del servidor:

```text
HTTP/1.1 200 OK
```

### Casos probados

| Caso probado | Datos ingresados | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| Servidor Django corre sin errores | URL: `/academico/materias/` en `127.0.0.1:8001` | El servidor inicia y responde sin errores. | Respuesta `HTTP/1.1 200 OK`; `manage.py check` sin errores. | Correcto |
| Registro de materia | Codigo: `T38-MAT`; nombre: `Matematica 3.8`; descripcion: `Materia creada para pruebas de la subfase 3.8.`; creditos: `4`; estado: `activo` | La materia se registra correctamente. | Materia creada con respuesta `200` y registro existente en base de datos. | Correcto |
| Error por codigo de materia duplicado | Se intento registrar otra materia con codigo `T38-MAT`. | El sistema rechaza el registro duplicado. | Se mostro el error `Ya existe una materia registrada con este codigo.` y solo quedo una materia con ese codigo. | Correcto |
| Edicion de materia | Materia `T38-MAT`; nuevo nombre: `Matematica 3.8 Editada`; creditos: `5` | La materia se actualiza correctamente. | La materia quedo con nombre `Matematica 3.8 Editada` y `5` creditos. | Correcto |
| Desactivacion de materia | Materia `T38-MAT` editada | No se borra el registro; solo cambia el estado a `inactivo`. | La materia quedo con estado `inactivo`. | Correcto |
| Registro de periodo academico | Nombre: `T38-Periodo-2026-I`; fecha inicio: `2026-03-01`; fecha fin: `2026-07-31`; estado: `activo` | El periodo academico se registra correctamente. | Periodo creado con respuesta `200` y registro existente en base de datos. | Correcto |
| Error si fecha fin es menor que fecha inicio | Nombre: `T38-Periodo-Invalido`; fecha inicio: `2026-08-01`; fecha fin: `2026-07-01`; estado: `activo` | El sistema rechaza el periodo con fechas invalidas. | Se mostro el error `La fecha de fin no puede ser menor que la fecha de inicio.` y no se creo el periodo. | Correcto |
| Registro de matricula | Estudiante: `T38-EST`; materia: `T38-MAT-MATRICULA`; periodo: `T38-Periodo-2026-I`; estado: `matriculado` | La matricula se registra correctamente. | Matricula creada con respuesta `200` y registro existente en base de datos. | Correcto |
| Error por matricula duplicada | Se intento registrar nuevamente al estudiante `T38-EST` en la materia `T38-MAT-MATRICULA` durante el periodo `T38-Periodo-2026-I`. | El sistema rechaza la matricula duplicada. | Se mostro el error `El estudiante ya esta matriculado en esta materia y periodo.` y solo quedo una matricula para esa combinacion. | Correcto |
| Retiro de matricula | Matricula de `T38-EST` en `T38-MAT-MATRICULA` durante `T38-Periodo-2026-I` | No se borra la matricula; solo cambia el estado a `retirado`. | La matricula quedo con estado `retirado`. | Correcto |

### Resultado general

Todas las pruebas de la subfase 3.8 fueron correctas. No se realizaron correcciones adicionales al codigo del modulo academico durante esta subfase.
