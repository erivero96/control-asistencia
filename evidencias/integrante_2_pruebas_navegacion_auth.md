# Pruebas de navegacion segun estado de sesion

## Caso 1: Pantalla de login sin sesion iniciada

- **Caso probado**: Acceder a `/cuentas/login/` sin haber iniciado sesion.
- **Accion realizada**: Abrir el navegador en `http://localhost:8000/cuentas/login/`.
- **Resultado esperado**: Se muestra el formulario de login. En la barra superior solo aparecen: titulo "Control Academico", subtitulo "Gestion academica" y boton "Iniciar sesion". No deben aparecer los enlaces a Estudiantes, Academico, Notas, Asistencia ni Reportes.
- **Resultado obtenido**: La barra superior muestra unicamente el titulo, subtitulo y boton "Iniciar sesion". El menu interno esta completamente oculto.
- **Estado**: correcto

## Caso 2: Verificar que no aparece menu interno sin sesion

- **Caso probado**: Confirmar que los enlaces internos (Estudiantes, Academico, Notas, Asistencia, Reportes) no se renderizan en el HTML cuando el usuario no esta autenticado.
- **Accion realizada**: Inspeccionar el codigo fuente de la pagina de login (`/cuentas/login/`) con las herramientas de desarrollador.
- **Resultado esperado**: En el HTML generado no deben existir las cadenas "Estudiantes", "Academico", "Notas", "Asistencia" ni "Reportes" dentro del `<nav class="navegacion-principal">`.
- **Resultado obtenido**: El `<nav class="navegacion-principal">` no aparece en el HTML. Las palabras de los modulos no estan presentes en la barra de navegacion.
- **Estado**: correcto

## Caso 3: Iniciar sesion con usuario valido

- **Caso probado**: Iniciar sesion con credenciales correctas.
- **Accion realizada**: Ingresar usuario y contrasena validos en el formulario de login y hacer clic en "Iniciar sesion".
- **Resultado esperado**: Redireccion a la pagina de inicio (`/`) con mensaje de bienvenida. El menu de navegacion ahora debe mostrar todos los enlaces internos y el nombre del usuario.
- **Resultado obtenido**: Sesion iniciada correctamente. Redireccion a `/`. Aparece el mensaje de bienvenida.
- **Estado**: correcto

## Caso 4: Verificar que aparece el menu interno con sesion

- **Caso probado**: Confirmar que con sesion iniciada se muestran todos los enlaces internos del sistema.
- **Accion realizada**: Observar la barra superior despues de iniciar sesion.
- **Resultado esperado**: Deben aparecer los enlaces: Inicio, Estudiantes, Academico, Notas, Asistencia y Reportes.
- **Resultado obtenido**: Los seis enlaces (Inicio, Estudiantes, Academico, Notas, Asistencia, Reportes) se muestran correctamente en la barra de navegacion.
- **Estado**: correcto

## Caso 5: Verificar que aparece el nombre del usuario

- **Caso probado**: Confirmar que el nombre del usuario autenticado se muestra en la barra superior.
- **Accion realizada**: Iniciar sesion y observar la seccion derecha de la barra de navegacion.
- **Resultado esperado**: Aparece el nombre del usuario (username) junto al boton "Cerrar sesion".
- **Resultado obtenido**: El `<span class="usuario-autenticado">` muestra correctamente el username. El boton "Cerrar sesion" esta presente.
- **Estado**: correcto

## Caso 6: Cerrar sesion

- **Caso probado**: Cerrar la sesion desde el boton "Cerrar sesion".
- **Accion realizada**: Hacer clic en "Cerrar sesion" en la barra de navegacion.
- **Resultado esperado**: Redireccion a la pantalla de login (`/cuentas/login/`). El menu interno desaparece completamente.
- **Resultado obtenido**: Redireccion a `/cuentas/login/`. El menu interno ya no aparece. Solo se muestra titulo, subtitulo y boton "Iniciar sesion".
- **Estado**: correcto

## Caso 7: Verificar que despues de cerrar sesion solo se ve Iniciar sesion

- **Caso probado**: Confirmar que tras cerrar sesion la barra vuelve al estado inicial.
- **Accion realizada**: Despues del logout, inspeccionar la barra superior en la pantalla de login.
- **Resultado esperado**: Solo deben aparecer: titulo "Control Academico", subtitulo "Gestion academica" y boton "Iniciar sesion". Sin menu interno ni nombre de usuario.
- **Resultado obtenido**: Exactamente como se esperaba. Sin rastros de la sesion anterior en la interfaz.
- **Estado**: correcto

## Caso 8: Intentar acceder a URL interna sin sesion

- **Caso probado**: Intentar entrar a una ruta protegida sin haber iniciado sesion.
- **Accion realizada**: Sin sesion abierta, escribir en el navegador `http://localhost:8000/estudiantes/`.
- **Resultado esperado**: Redireccion automatica a `/cuentas/login/?next=/estudiantes/`. Al iniciar sesion, redirige a `/estudiantes/`.
- **Resultado obtenido**: Redireccion a login con parametro `next=/estudiantes/`. Al autenticarse, redirige correctamente a la URL solicitada. La barra de navegacion todavia no se muestra en el login, y aparece completa tras la autenticacion.
- **Estado**: correcto
