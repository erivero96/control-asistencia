from django import forms
from django.utils import timezone

from academico.models import Materia, Matricula, PeriodoAcademico

from .models import Asistencia


class AsistenciaPorMateriaForm(forms.Form):
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
    fecha = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(attrs={'type': 'date'}),
        error_messages={
            'required': 'La fecha de asistencia es obligatoria.',
            'invalid': 'Ingrese una fecha valida.',
        },
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['materia'].queryset = Materia.objects.filter(
            estado=Materia.ESTADO_ACTIVO,
        ).order_by('nombre')
        self.fields['periodo'].queryset = PeriodoAcademico.objects.filter(
            estado=PeriodoAcademico.ESTADO_ACTIVO,
        ).order_by('-fecha_inicio', 'nombre')

        if not self.is_bound:
            self.fields['fecha'].initial = timezone.localdate()

    def clean_materia(self):
        materia = self.cleaned_data.get('materia')

        if not materia:
            raise forms.ValidationError('Seleccione una materia.')

        if materia.estado != Materia.ESTADO_ACTIVO:
            raise forms.ValidationError(
                'Solo se puede registrar asistencia para materias activas.'
            )

        return materia

    def clean_periodo(self):
        periodo = self.cleaned_data.get('periodo')

        if not periodo:
            raise forms.ValidationError('Seleccione un periodo academico.')

        if periodo.estado != PeriodoAcademico.ESTADO_ACTIVO:
            raise forms.ValidationError(
                'Solo se puede registrar asistencia en periodos activos.'
            )

        return periodo

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        if not fecha:
            raise forms.ValidationError(
                'La fecha de asistencia es obligatoria.'
            )

        return fecha

    def clean(self):
        cleaned_data = super().clean()
        periodo = cleaned_data.get('periodo')
        fecha = cleaned_data.get('fecha')

        if (
            periodo
            and fecha
            and (fecha < periodo.fecha_inicio or fecha > periodo.fecha_fin)
        ):
            self.add_error(
                'fecha',
                'La fecha de asistencia debe estar dentro del periodo academico.',
            )

        return cleaned_data


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            'matricula',
            'fecha',
            'estado',
            'observacion',
        ]
        labels = {
            'matricula': 'Matricula',
            'fecha': 'Fecha',
            'estado': 'Estado',
            'observacion': 'Observacion',
        }
        error_messages = {
            'matricula': {
                'required': 'Seleccione una matricula.',
                'invalid_choice': 'Seleccione una matricula valida.',
            },
            'fecha': {
                'required': 'La fecha de asistencia es obligatoria.',
                'invalid': 'Ingrese una fecha valida.',
            },
            'estado': {
                'required': 'Seleccione el estado de asistencia.',
                'invalid_choice': 'Seleccione un estado valido.',
            },
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['matricula'].queryset = Matricula.objects.filter(
            estado=Matricula.ESTADO_MATRICULADO,
        ).select_related(
            'estudiante',
            'materia',
            'periodo',
        ).order_by(
            'estudiante__apellidos',
            'estudiante__nombres',
            'materia__nombre',
        )

        if not self.instance.pk and not self.is_bound:
            self.fields['fecha'].initial = timezone.localdate()

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')

        if not matricula:
            raise forms.ValidationError('Seleccione una matricula.')

        if matricula.estado != Matricula.ESTADO_MATRICULADO:
            raise forms.ValidationError(
                'Solo se puede registrar asistencia para matriculas activas.'
            )

        return matricula

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')

        if not fecha:
            raise forms.ValidationError(
                'La fecha de asistencia es obligatoria.'
            )

        return fecha

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')

        if not estado:
            raise forms.ValidationError('Seleccione el estado de asistencia.')

        return estado

    def clean(self):
        cleaned_data = super().clean()
        matricula = cleaned_data.get('matricula')
        fecha = cleaned_data.get('fecha')

        if matricula and fecha:
            periodo = matricula.periodo

            if fecha < periodo.fecha_inicio or fecha > periodo.fecha_fin:
                self.add_error(
                    'fecha',
                    'La fecha de asistencia debe estar dentro del periodo academico.',
                )

            asistencias = Asistencia.objects.filter(
                matricula=matricula,
                fecha=fecha,
            )

            if self.instance.pk:
                asistencias = asistencias.exclude(pk=self.instance.pk)

            if asistencias.exists():
                self.add_error(
                    'fecha',
                    'Ya existe asistencia registrada para esta matricula y fecha.',
                )

        return cleaned_data
