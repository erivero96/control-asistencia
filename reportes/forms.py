from django import forms

from academico.models import Materia, PeriodoAcademico


class ReporteMateriaForm(forms.Form):
    materia = forms.ModelChoiceField(
        queryset=Materia.objects.order_by('nombre'),
        label='Materia',
        empty_label='Seleccione una materia',
        error_messages={
            'required': 'Seleccione una materia.',
            'invalid_choice': 'Seleccione una materia valida.',
        },
    )
    periodo = forms.ModelChoiceField(
        queryset=PeriodoAcademico.objects.order_by('-fecha_inicio', 'nombre'),
        label='Periodo academico',
        empty_label='Seleccione un periodo academico',
        error_messages={
            'required': 'Seleccione un periodo academico.',
            'invalid_choice': 'Seleccione un periodo academico valido.',
        },
    )
