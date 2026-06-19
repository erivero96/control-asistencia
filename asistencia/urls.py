from django.urls import path

from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.listar_asistencias, name='index'),
    path('', views.listar_asistencias, name='listar_asistencias'),
    path('registrar/', views.registrar_asistencia, name='registrar_asistencia'),
    path(
        'registrar-por-materia/',
        views.registrar_asistencia_por_materia,
        name='registrar_asistencia_por_materia',
    ),
    path(
        'estudiante/<int:estudiante_id>/',
        views.asistencias_por_estudiante,
        name='asistencias_por_estudiante',
    ),
    path(
        'materia/<int:materia_id>/',
        views.asistencias_por_materia,
        name='asistencias_por_materia',
    ),
    path(
        'porcentaje/matricula/<int:matricula_id>/',
        views.porcentaje_asistencia_matricula,
        name='porcentaje_asistencia_matricula',
    ),
    path(
        'porcentajes/materia/<int:materia_id>/',
        views.porcentajes_por_materia,
        name='porcentajes_por_materia',
    ),
    path(
        '<int:asistencia_id>/',
        views.detalle_asistencia,
        name='detalle_asistencia',
    ),
    path(
        '<int:asistencia_id>/editar/',
        views.editar_asistencia,
        name='editar_asistencia',
    ),
]
