from django.contrib import admin

from .models import Asistencia


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante',
        'materia',
        'periodo',
        'fecha',
        'estado',
    )
    search_fields = (
        'matricula__estudiante__codigo',
        'matricula__estudiante__nombres',
        'matricula__estudiante__apellidos',
        'matricula__materia__codigo',
        'matricula__materia__nombre',
    )
    list_filter = (
        'estado',
        'fecha',
        'matricula__periodo',
        'matricula__materia',
    )
    ordering = ('-fecha',)
    readonly_fields = ('fecha_registro',)
    list_select_related = (
        'matricula__estudiante',
        'matricula__materia',
        'matricula__periodo',
    )
    list_per_page = 20

    @admin.display(description='Estudiante', ordering='matricula__estudiante__apellidos')
    def estudiante(self, obj):
        return obj.matricula.estudiante

    @admin.display(description='Materia', ordering='matricula__materia__nombre')
    def materia(self, obj):
        return obj.matricula.materia

    @admin.display(description='Periodo', ordering='matricula__periodo__nombre')
    def periodo(self, obj):
        return obj.matricula.periodo
