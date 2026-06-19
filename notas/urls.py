from django.urls import path

from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.listar_notas, name='index'),
    path('', views.listar_notas, name='listar_notas'),
    path('registrar/', views.registrar_nota, name='registrar_nota'),
    path('<int:nota_id>/', views.detalle_nota, name='detalle_nota'),
    path('<int:nota_id>/editar/', views.editar_nota, name='editar_nota'),
    path(
        'estudiante/<int:estudiante_id>/',
        views.notas_por_estudiante,
        name='notas_por_estudiante',
    ),
    path(
        'materia/<int:materia_id>/',
        views.notas_por_materia,
        name='notas_por_materia',
    ),
    path(
        'evaluaciones/',
        views.listar_evaluaciones,
        name='listar_evaluaciones',
    ),
    path(
        'evaluaciones/crear/',
        views.crear_evaluacion,
        name='crear_evaluacion',
    ),
    path(
        'evaluaciones/<int:evaluacion_id>/editar/',
        views.editar_evaluacion,
        name='editar_evaluacion',
    ),
    path(
        'evaluaciones/<int:evaluacion_id>/desactivar/',
        views.desactivar_evaluacion,
        name='desactivar_evaluacion',
    ),
    path(
        'promedios/matricula/<int:matricula_id>/',
        views.promedio_matricula,
        name='promedio_matricula',
    ),
    path(
        'promedios/materia/<int:materia_id>/',
        views.promedios_por_materia,
        name='promedios_por_materia',
    ),
]
