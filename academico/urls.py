from django.urls import path

from . import views

app_name = 'academico'

urlpatterns = [
    path('', views.index, name='index'),
    path('materias/', views.listar_materias, name='listar_materias'),
    path('materias/crear/', views.crear_materia, name='crear_materia'),
    path(
        'materias/<int:materia_id>/editar/',
        views.editar_materia,
        name='editar_materia',
    ),
    path(
        'materias/<int:materia_id>/desactivar/',
        views.desactivar_materia,
        name='desactivar_materia',
    ),
    path('periodos/', views.listar_periodos, name='listar_periodos'),
    path('periodos/crear/', views.crear_periodo, name='crear_periodo'),
    path(
        'periodos/<int:periodo_id>/editar/',
        views.editar_periodo,
        name='editar_periodo',
    ),
    path('matriculas/', views.listar_matriculas, name='listar_matriculas'),
    path('matriculas/crear/', views.crear_matricula, name='crear_matricula'),
    path(
        'matriculas/<int:matricula_id>/',
        views.detalle_matricula,
        name='detalle_matricula',
    ),
    path(
        'matriculas/<int:matricula_id>/retirar/',
        views.retirar_matricula,
        name='retirar_matricula',
    ),
]
