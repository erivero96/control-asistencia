# Guía breve para la defensa final

## 1. Explicación general del sistema

El proyecto es un Sistema de Control Académico desarrollado con Python y Django. Permite registrar estudiantes, materias, periodos académicos y matrículas. También administra evaluaciones, notas y asistencias, y reúne la información en reportes académicos.

La aplicación usa MySQL como base de datos, ejecutada con Docker Compose. Django se ejecuta fuera de Docker y se conecta a la base mediante variables de entorno.

## 2. Explicación breve por integrante

| Integrante | Explicación para exponer |
| --- | --- |
| Integrante 1 | Preparó la base técnica: estructura de Django, configuración, conexión a MySQL mediante Docker Compose y aplicaciones iniciales. |
| Integrante 2 | Desarrolló el módulo de estudiantes: registro, edición, detalle, desactivación y validaciones de DNI y código únicos. |
| Integrante 3 | Desarrolló el módulo académico: materias, periodos académicos y matrículas, incluyendo las validaciones de fechas y matrícula única. |
| Integrante 4 | Desarrolló evaluaciones y notas. Implementó los promedios simple y ponderado, además de los estados aprobado, desaprobado y pendiente. |
| Integrante 5 | Desarrolló el módulo de asistencia: registro individual y por materia, consultas y cálculo de porcentajes de asistencia. |
| Integrante 6 | Desarrolló los reportes, integró la navegación principal, realizó las pruebas de integración y consolidó las evidencias finales. |

## 3. Sección especial: Integrante 6

### Reportes desarrollados

- Reporte por estudiante: muestra sus datos, materias matriculadas, periodo, notas, promedio, estado académico y resumen de asistencia.
- Reporte por materia y periodo: muestra estudiantes matriculados, notas, promedio por estudiante, cantidad de aprobados, desaprobados y asistencia global.
- Reporte por periodo académico: muestra estudiantes únicos, materias activas con matrícula, total de matrículas, notas y asistencias del periodo.

### Integración de navegación

Se creó `templates/base.html` con enlaces a Inicio, Estudiantes, Materias, Periodos, Matrículas, Evaluaciones, Notas, Asistencia y Reportes. La página de Inicio se convirtió en un panel principal con accesos directos a esos módulos.

### Pruebas realizadas

Se verificó el inicio de Django, la navegación entre los nueve enlaces principales, el flujo completo de registro y los tres reportes. También se probaron DNI, materia, matrícula y asistencia duplicados, una nota fuera de rango y reportes sin datos. La suite de integración registró cuatro pruebas correctas.

### Documentación de evidencias

Se registraron prompts, resultados de integración, matriz de roles, resumen de prompts y declaración de uso de IA en la carpeta `evidencias/`.

## 4. Flujo recomendado para la demostración en vivo

1. Levantar MySQL con `docker compose up -d mysql` y ejecutar `python manage.py runserver`.
2. Abrir `http://127.0.0.1:8000/` y mostrar el panel principal y su barra de navegación.
3. En Estudiantes, registrar un estudiante con un DNI válido.
4. En Materias, registrar una materia activa.
5. En Periodos, registrar un periodo con fecha de fin posterior a la fecha de inicio.
6. En Matrículas, asociar el estudiante, la materia y el periodo.
7. En Evaluaciones, crear una evaluación para esa materia y periodo.
8. En Notas, registrar una calificación válida, por ejemplo `16.00`.
9. En Asistencia, registrar una asistencia para la matrícula creada.
10. Mostrar los reportes usando los identificadores generados:
    - `/reportes/estudiante/<estudiante_id>/`
    - `/reportes/materia/<materia_id>/periodo/<periodo_id>/`
    - `/reportes/periodo/<periodo_id>/`
11. Finalmente, intentar registrar una nota mayor a 20 o una matrícula repetida para mostrar que las validaciones funcionan.

## 5. Preguntas posibles y respuestas sugeridas

### Integrante 1

**Pregunta:** ¿Por qué usaron MySQL en Docker Compose?

**Respuesta sugerida:** Porque Docker facilita tener la misma versión de MySQL en todos los equipos y separa la base de datos de la instalación local de Django.

**Pregunta:** ¿Cómo se configura la conexión a la base de datos?

**Respuesta sugerida:** Se usan variables de entorno cargadas desde `.env`; el archivo `.env.example` sirve como plantilla sin exponer credenciales reales.

### Integrante 2

**Pregunta:** ¿Cómo evitan estudiantes duplicados?

**Respuesta sugerida:** El modelo declara únicos el código y el DNI, y el formulario valida el DNI antes de guardar para mostrar mensajes claros.

**Pregunta:** ¿Por qué desactivar en lugar de eliminar un estudiante?

**Respuesta sugerida:** Así se conserva el historial académico y se evita perder referencias relacionadas con matrículas, notas o asistencia.

### Integrante 3

**Pregunta:** ¿Cómo se evita una matrícula repetida?

**Respuesta sugerida:** Se valida la combinación estudiante, materia y periodo tanto en el formulario como con una restricción única en la base de datos.

**Pregunta:** ¿Cómo se validan las fechas de un periodo?

**Respuesta sugerida:** La fecha de fin debe ser igual o posterior a la fecha de inicio; la validación se realiza en el formulario y en el modelo.

### Integrante 4

**Pregunta:** ¿Cómo se calcula el promedio?

**Respuesta sugerida:** Se calcula el promedio ponderado usando la calificación y el peso de cada evaluación. Si no existen notas, el estado es pendiente.

**Pregunta:** ¿Cuándo un estudiante está aprobado?

**Respuesta sugerida:** El sistema considera aprobado un promedio ponderado igual o mayor a 11; si es menor, queda desaprobado.

### Integrante 5

**Pregunta:** ¿Cómo se evita duplicar asistencia?

**Respuesta sugerida:** Se controla la combinación matrícula y fecha en el formulario y mediante una restricción única en la base de datos.

**Pregunta:** ¿Cómo se calcula el porcentaje de asistencia?

**Respuesta sugerida:** Se consideran válidos presente, tardanza y justificado; falta se contabiliza como inasistencia. El porcentaje se calcula sobre el total de clases registradas.

### Integrante 6

**Pregunta:** ¿Cómo se construyen los reportes sin duplicar información?

**Respuesta sugerida:** Los reportes consultan los modelos existentes de estudiantes, matrículas, notas y asistencias. Para promedios y asistencia reutilizan las utilidades ya creadas en esos módulos.

**Pregunta:** ¿Qué verificaron en las pruebas de integración?

**Respuesta sugerida:** Verificamos navegación, el flujo completo desde estudiante hasta reportes, validaciones de duplicados, notas fuera de rango y la respuesta de reportes sin datos.

## 6. Errores encontrados y cómo se corrigieron

| Situación | Corrección aplicada |
| --- | --- |
| El mensaje para un DNI de más de ocho dígitos era genérico. | Se ajustó la validación para mostrar el mensaje claro: el DNI debe tener exactamente ocho dígitos. |
| El usuario de Django no tenía permiso para crear automáticamente la base temporal de pruebas. | Se creó una base temporal con permisos limitados para la prueba de integración y se eliminó al terminar, sin modificar la base real. |
| Podían ocurrir intentos de datos duplicados durante el registro. | Se aplicaron validaciones en formularios y restricciones únicas para DNI, código de materia, matrícula, nota y asistencia. |
| Un reporte podía no tener matrículas, notas o asistencias. | Se agregaron mensajes informativos para mostrar el estado sin producir errores de pantalla. |

## 7. Cierre sugerido

El sistema integra los módulos académicos principales y mantiene reglas de validación para proteger la información. La división por roles permitió desarrollar cada parte de forma organizada, y las pruebas de integración confirmaron que el flujo completo funciona desde el registro hasta los reportes.
