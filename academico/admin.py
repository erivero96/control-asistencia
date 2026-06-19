from django.contrib import admin

from .models import Materia, Matricula, PeriodoAcademico


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


@admin.register(PeriodoAcademico)
class PeriodoAcademicoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'fecha_inicio',
        'fecha_fin',
        'estado',
    )
    search_fields = ('nombre',)
    list_filter = ('estado', 'fecha_inicio', 'fecha_fin')
    ordering = ('-fecha_inicio', 'nombre')
    readonly_fields = ('fecha_registro',)
    list_per_page = 20


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante',
        'materia',
        'periodo',
        'estado',
        'fecha_matricula',
    )
    search_fields = (
        'estudiante__codigo',
        'estudiante__nombres',
        'estudiante__apellidos',
        'materia__codigo',
        'materia__nombre',
        'periodo__nombre',
    )
    list_filter = ('estado', 'periodo', 'materia')
    ordering = ('-fecha_matricula',)
    readonly_fields = ('fecha_matricula',)
    list_per_page = 20
