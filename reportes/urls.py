from django.urls import path

from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.panel_reportes, name='panel_reportes'),
    path('', views.panel_reportes, name='index'),
    path(
        'estudiante/<int:estudiante_id>/',
        views.reporte_estudiante,
        name='reporte_estudiante',
    ),
]
