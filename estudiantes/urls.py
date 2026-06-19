from django.urls import path

from . import views

app_name = 'estudiantes'

urlpatterns = [
    path('', views.listar_estudiantes, name='listar_estudiantes'),
    path('', views.listar_estudiantes, name='index'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path(
        '<int:estudiante_id>/',
        views.detalle_estudiante,
        name='detalle_estudiante',
    ),
    path(
        '<int:estudiante_id>/editar/',
        views.editar_estudiante,
        name='editar_estudiante',
    ),
    path(
        '<int:estudiante_id>/desactivar/',
        views.desactivar_estudiante,
        name='desactivar_estudiante',
    ),
]
