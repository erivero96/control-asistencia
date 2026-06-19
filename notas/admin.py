from django.contrib import admin

from .models import Evaluacion, Nota


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


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante',
        'materia',
        'evaluacion',
        'calificacion',
        'fecha_registro',
    )
    search_fields = (
        'matricula__estudiante__codigo',
        'matricula__estudiante__nombres',
        'matricula__estudiante__apellidos',
        'matricula__materia__codigo',
        'matricula__materia__nombre',
        'evaluacion__nombre',
    )
    list_filter = (
        'matricula__periodo',
        'matricula__materia',
        'evaluacion',
        'fecha_registro',
    )
    ordering = ('-fecha_registro',)
    readonly_fields = ('fecha_registro',)
    list_select_related = (
        'matricula__estudiante',
        'matricula__materia',
        'matricula__periodo',
        'evaluacion',
    )
    list_per_page = 20

    @admin.display(description='Estudiante', ordering='matricula__estudiante__apellidos')
    def estudiante(self, obj):
        return obj.matricula.estudiante

    @admin.display(description='Materia', ordering='matricula__materia__nombre')
    def materia(self, obj):
        return obj.matricula.materia
