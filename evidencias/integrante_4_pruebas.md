# Evidencias de pruebas - Integrante 4

## Subfase 4.9

### Resumen

Se probaron las funciones principales del modulo de notas: evaluaciones, registro de notas, validaciones, consultas y calculo de promedios. Las pruebas se realizaron con el servidor de Django y con formularios/vistas de Django usando datos temporales con prefijo `T49-`. Los datos temporales se ejecutaron dentro de una transaccion revertida para no dejar registros de prueba en la base de datos.

### Comandos usados

```bash
.venv/bin/python manage.py check
.venv/bin/python manage.py runserver 127.0.0.1:8020 --noreload
curl -I http://127.0.0.1:8020/notas/
curl -I http://127.0.0.1:8020/notas/evaluaciones/
```

Resultado del servidor:

```text
System check identified no issues (0 silenced).
Starting development server at http://127.0.0.1:8020/
HTTP/1.1 200 OK
```

Tambien se ejecuto una prueba automatizada con `manage.py shell` para validar formularios, vistas, duplicados y promedios.

### Casos probados

| Caso probado | Datos ingresados | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| Servidor Django corre sin errores | URL: `/notas/` y `/notas/evaluaciones/` en `127.0.0.1:8020` | El servidor inicia y responde sin errores. | `manage.py check` sin errores y respuestas `HTTP/1.1 200 OK`. | Correcto |
| Registro de evaluacion | Materia `T49-MAT`; periodo `T49-Periodo-2026-I`; nombre `T49 Parcial`; peso `50.00`; estado `activo` | La evaluacion se registra correctamente. | `EvaluacionForm` valido y evaluacion creada. | Correcto |
| Error por peso invalido | Peso `0.00` | El formulario rechaza el peso porque debe ser mayor que cero. | Se mostro el error `El peso de la evaluacion debe ser mayor que cero.` | Correcto |
| Registro de nota | Matricula `T49-EST-AP` en `T49-MAT`; evaluacion `T49 Parcial`; calificacion `12.00` | La nota se registra correctamente. | `NotaForm` valido y nota creada con calificacion `12.00`. | Correcto |
| Error por nota menor que 0 | Calificacion `-1.00` | El formulario rechaza la calificacion menor que cero. | Se mostro el error `La calificacion debe estar entre 0 y 20.` | Correcto |
| Error por nota mayor que 20 | Calificacion `21.00` | El formulario rechaza la calificacion mayor que veinte. | Se mostro el error `La calificacion debe estar entre 0 y 20.` | Correcto |
| Error por nota duplicada | Misma matricula `T49-EST-AP` y misma evaluacion `T49 Parcial` | El sistema evita registrar dos notas para la misma matricula y evaluacion. | Se mostro el error `Ya existe una nota registrada para esta matricula y evaluacion.` | Correcto |
| Edicion de nota | Nota `T49 Parcial`; nueva calificacion `13.00`; observacion `Nota editada.` | La nota se actualiza correctamente. | `NotaForm` valido y nota actualizada a `13.00`. | Correcto |
| Consulta de notas por estudiante | Estudiante `T49-EST-AP` | La vista responde y muestra las notas del estudiante. | Respuesta `200`; contenido incluye `T49 Parcial`. | Correcto |
| Consulta de notas por materia | Materia `T49-MAT` | La vista responde y muestra las notas de la materia. | Respuesta `200`; contenido incluye `Materia Prueba 4.9`. | Correcto |
| Calculo de promedio en vista | Matricula de `T49-EST-AP` con notas `13.00` y `15.00`, pesos `50.00` y `50.00` | La vista de promedio responde y muestra estado aprobado. | Respuesta `200`; contenido incluye `Aprobado`. | Correcto |
| Estado aprobado si promedio es mayor o igual a 11 | Promedio ponderado esperado `14.00` | El estado debe ser `aprobado`. | Promedio `14.00`; estado `aprobado`. | Correcto |
| Estado desaprobado si promedio es menor a 11 | Notas `8.00` y `10.00`, pesos `50.00` y `50.00`; promedio esperado `9.00` | El estado debe ser `desaprobado`. | Promedio `9.00`; estado `desaprobado`. | Correcto |
| Promedio pendiente sin notas | Matricula temporal sin notas registradas | El promedio debe quedar pendiente. | Promedio `None`; estado `pendiente`. | Correcto |

### Errores comunes y solucion

| Error comun | Causa probable | Solucion |
| --- | --- | --- |
| El servidor no inicia | MySQL no esta levantado o faltan dependencias. | Ejecutar `docker compose up -d mysql` y luego `pip install -r requirements.txt`. |
| Error de template no encontrado | Falta algun archivo en `templates/notas/`. | Verificar que existan los templates usados por las vistas. |
| La ruta no existe | Falta registrar la URL en `notas/urls.py`. | Confirmar que el nombre de ruta exista y que `config/urls.py` incluya `path('notas/', include('notas.urls'))`. |
| No aparece el mensaje de error del formulario | El template no recorre `form.errors` o `messages`. | Revisar que el template muestre errores por campo y mensajes de Django. |
| Se permite nota duplicada | No se esta usando `NotaForm` o se omitio la validacion. | Registrar y editar notas siempre mediante `NotaForm`. |
| Promedio aparece como error cuando no hay notas | No se controla el caso sin registros. | Usar `determinar_estado_promedio(None)` para mostrar `pendiente`. |

### Resultado general

Todas las pruebas de la subfase 4.9 fueron correctas. No se realizaron correcciones adicionales al codigo funcional del modulo de notas durante esta subfase; solo se creo la evidencia de pruebas.
