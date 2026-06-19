from django.contrib import admin

from .models import Estudiante


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombres',
        'apellidos',
        'dni',
        'correo',
        'telefono',
        'estado',
        'fecha_registro',
    )
    search_fields = ('codigo', 'dni', 'nombres', 'apellidos')
    list_filter = ('estado', 'fecha_registro')
    ordering = ('apellidos', 'nombres')
    readonly_fields = ('fecha_registro',)
    list_per_page = 20
