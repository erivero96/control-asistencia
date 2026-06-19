from django.contrib import admin

from .models import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'creditos',
        'estado',
    )
    search_fields = ('codigo', 'nombre')
    list_filter = ('estado', 'fecha_registro')
    ordering = ('nombre',)
    readonly_fields = ('fecha_registro',)
    list_per_page = 20
