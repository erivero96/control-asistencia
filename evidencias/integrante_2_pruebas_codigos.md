# Evidencias de pruebas de codigos automaticos - Integrante 2

## Alcance

Se validaron los codigos automaticos de `Estudiante` y `Materia`. De acuerdo con la auditoria de la subfase 2.12, los modelos `PeriodoAcademico`, `Matricula`, `Evaluacion`, `Nota` y `Asistencia` no tienen un campo de codigo, por lo que no requieren generacion automatica.

## Casos de prueba

### Caso 1: Creacion automatica de codigo de estudiante

- **Caso probado:** Generacion del codigo al guardar un estudiante nuevo sin codigo.
- **Accion realizada:** Se creo un `Estudiante` sin asignar el campo `codigo` y se ejecuto `save()`.
- **Resultado esperado:** Se asigna un codigo con formato `EST-0001`.
- **Resultado obtenido:** Se genero `EST-0001` usando `generar_codigo` con el prefijo `EST` y cuatro digitos.
- **Estado:** Correcto.

### Caso 2: Creacion consecutiva de estudiantes

- **Caso probado:** Correlatividad de codigos para dos estudiantes nuevos.
- **Accion realizada:** Se crearon dos estudiantes con DNI y correos distintos dentro de una prueba de integracion.
- **Resultado esperado:** Los codigos asignados son `EST-0001` y `EST-0002`.
- **Resultado obtenido:** El primer estudiante recibio `EST-0001` y el segundo `EST-0002`.
- **Estado:** Correcto.

### Caso 3: Formulario de estudiante sin codigo manual

- **Caso probado:** Exclusión de `codigo` en `EstudianteForm`.
- **Accion realizada:** Se verifico `EstudianteForm().fields` y la propiedad `editable` del campo del modelo.
- **Resultado esperado:** El formulario no contiene `codigo` y el campo no es editable.
- **Resultado obtenido:** `codigo` no aparece en los campos del formulario y `Estudiante.codigo.editable` es `False`.
- **Estado:** Correcto.

### Caso 4: Visualizacion del codigo de estudiante

- **Caso probado:** Presencia del codigo en las pantallas de consulta de estudiantes.
- **Accion realizada:** Se revisaron `templates/estudiantes/lista.html` y `templates/estudiantes/detalle.html`.
- **Resultado esperado:** La lista y el detalle muestran el codigo del estudiante.
- **Resultado obtenido:** Ambos templates contienen `{{ estudiante.codigo }}`; el formulario no lo solicita porque itera solo los campos de `EstudianteForm`.
- **Estado:** Correcto.

### Caso 5: Creacion automatica de codigo de materia

- **Caso probado:** Generacion del codigo al guardar una materia nueva sin codigo.
- **Accion realizada:** Se creo una `Materia` sin asignar el campo `codigo` y se ejecuto `save()`.
- **Resultado esperado:** Se asigna un codigo con formato `MAT-0001`.
- **Resultado obtenido:** Se genero `MAT-0001` usando `generar_codigo` con el prefijo `MAT` y cuatro digitos.
- **Estado:** Correcto.

### Caso 6: Creacion consecutiva de materias

- **Caso probado:** Correlatividad de codigos para dos materias nuevas.
- **Accion realizada:** Se crearon dos materias con nombres distintos dentro de una prueba de integracion.
- **Resultado esperado:** Los codigos asignados son `MAT-0001` y `MAT-0002`.
- **Resultado obtenido:** La primera materia recibio `MAT-0001` y la segunda `MAT-0002`.
- **Estado:** Correcto.

### Caso 7: Formulario de materia sin codigo manual

- **Caso probado:** Exclusión de `codigo` en `MateriaForm`.
- **Accion realizada:** Se verifico `MateriaForm().fields` y la propiedad `editable` del campo del modelo.
- **Resultado esperado:** El formulario no contiene `codigo` y el campo no es editable.
- **Resultado obtenido:** `codigo` no aparece en los campos del formulario y `Materia.codigo.editable` es `False`.
- **Estado:** Correcto.

### Caso 8: Visualizacion del codigo de materia

- **Caso probado:** Presencia del codigo en el listado de materias.
- **Accion realizada:** Se reviso `templates/academico/materias_lista.html`.
- **Resultado esperado:** El listado muestra el codigo de cada materia.
- **Resultado obtenido:** El template contiene `{{ materia.codigo }}` en la columna Codigo.
- **Estado:** Correcto.

### Caso 9: Prevencion de codigos duplicados

- **Caso probado:** Unicidad de los codigos generados para estudiantes y materias.
- **Accion realizada:** Se crearon dos registros consecutivos de cada modelo y se verifico la definicion `unique=True` de ambos campos `codigo`.
- **Resultado esperado:** Cada registro recibe un codigo distinto y la base de datos impide valores duplicados.
- **Resultado obtenido:** Se obtuvieron `EST-0001`/`EST-0002` y `MAT-0001`/`MAT-0002`; ambos campos mantienen la restriccion `unique=True`.
- **Estado:** Correcto.

### Caso 10: Modelos sin necesidad de codigo automatico

- **Caso probado:** Auditoria de los modelos restantes.
- **Accion realizada:** Se revisaron `PeriodoAcademico`, `Matricula`, `Evaluacion`, `Nota`, `Asistencia` y `reportes.models` buscando campos `codigo`, `cod`, `numero` o `identificador`.
- **Resultado esperado:** No se agregan codigos artificiales a modelos que no los requieren.
- **Resultado obtenido:** Ninguno de los modelos revisados tiene esos campos; `reportes.models` no define modelos de negocio. No se realizaron cambios de esquema ni migraciones nuevas.
- **Estado:** Correcto.

## Comandos de validacion ejecutados

```bash
python manage.py test estudiantes.tests academico.tests core.test_codigos --keepdb
python manage.py check
python manage.py makemigrations --check --dry-run
```

## Resultado general

Las 14 pruebas automatizadas ejecutadas finalizaron correctamente. Django no reporto errores de configuracion y no se detectaron cambios de modelo pendientes de migracion.
