# Pruebas - Integrante 2

## Subfase 2.6 - Modulo de estudiantes

Datos temporales usados durante la prueba:

- Codigo principal: `T2601`
- DNI principal: `72600101`
- Codigo secundario: `T2602`
- DNI secundario: `72600102`
- Nombre inicial: `Ana Lucia Quispe Rojas`
- Nombre editado: `Ana Lucia Editada Quispe Rojas`

Los registros temporales fueron eliminados al terminar las pruebas.

| Caso probado | Datos ingresados | Resultado esperado | Resultado obtenido | Estado |
| --- | --- | --- | --- | --- |
| Servidor Django sin errores | `python manage.py check` y acceso HTTP a `/estudiantes/` | El sistema no debe reportar errores y la ruta debe responder correctamente. | `manage.py check` no reporto errores y `/estudiantes/` respondio `200 OK`. | correcto |
| Ingreso a `/estudiantes/` | Solicitud GET a `/estudiantes/` | Debe cargar la lista de estudiantes. | La vista `listar_estudiantes` respondio `200 OK`. | correcto |
| Registro de estudiante | `codigo=T2601`, `dni=72600101`, nombres, apellidos, correo, telefono, direccion y estado activo | Debe guardar el estudiante y redirigir a la lista. | Se creo el estudiante y la respuesta fue `302` hacia la lista. | correcto |
| Edicion de estudiante | Se cambio `nombres` a `Ana Lucia Editada` y `telefono` a `912345678` | Debe actualizar el registro existente. | El estudiante quedo actualizado y la respuesta fue `302`. | correcto |
| Detalle de estudiante | Solicitud GET a `/estudiantes/<id>/` | Debe mostrar la informacion completa del estudiante. | La respuesta fue `200 OK` y el contenido incluyo el nombre editado. | correcto |
| Desactivacion de estudiante | Confirmacion POST a `/estudiantes/<id>/desactivar/` | No debe borrar el registro, solo cambiar `estado` a `inactivo`. | El estudiante quedo con estado `inactivo` y la respuesta fue `302`. | correcto |
| Error por DNI duplicado | Nuevo formulario con `dni=72600101` ya registrado y `codigo=T2602` | Debe impedir el registro y mostrar error de DNI duplicado. | El formulario rechazo el registro con `Ya existe un estudiante registrado con este DNI.` | correcto |
| Error por codigo duplicado | Nuevo formulario con `codigo=T2601` ya registrado y `dni=72600102` | Debe impedir el registro y mostrar error de codigo duplicado. | El formulario rechazo el registro con `Ya existe un estudiante registrado con este codigo.` | correcto |
| Error por DNI corto | `dni=1234567` | Debe impedir el registro y mostrar error de longitud del DNI. | El formulario rechazo el registro con `El DNI debe tener exactamente 8 digitos.` | correcto |
| Error por DNI largo | `dni=123456789` | Debe impedir el registro y mostrar error claro de longitud del DNI. | Se corrigio el mensaje `max_length`; ahora muestra `El DNI debe tener exactamente 8 digitos.` | corregido |

## Comandos usados

```bash
.venv/bin/python manage.py check
curl -I http://127.0.0.1:8000/estudiantes/
.venv/bin/python manage.py shell
```

## Observaciones

- La ruta `/estudiantes/` carga correctamente.
- Las operaciones de registro, edicion, detalle y desactivacion funcionan.
- Las validaciones de DNI y codigo unico funcionan.
- La desactivacion conserva el registro y solo cambia el estado a `inactivo`.
- Se ajusto el mensaje para DNI con mas de 8 digitos, porque Django mostraba inicialmente un mensaje generico de `max_length`.
