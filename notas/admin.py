from django.contrib import admin

from .models import Evaluacion


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = (
        'materia',
        'periodo',
        'nombre',
        'peso',
        'estado',
    )
    search_fields = (
        'nombre',
        'materia__codigo',
        'materia__nombre',
    )
    list_filter = ('estado', 'periodo', 'materia')
    ordering = ('materia', 'periodo', 'nombre')
    readonly_fields = ('fecha_registro',)
    list_per_page = 20
