from django import forms

from .models import Asistencia


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

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')

        if not matricula:
            raise forms.ValidationError('Seleccione una matricula.')

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
