from decimal import Decimal

from django import forms

from .models import Evaluacion, Nota


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = [
            'materia',
            'periodo',
            'nombre',
            'descripcion',
            'peso',
            'estado',
        ]
        labels = {
            'materia': 'Materia',
            'periodo': 'Periodo academico',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'peso': 'Peso (%)',
            'estado': 'Estado',
        }
        error_messages = {
            'materia': {
                'required': 'Seleccione una materia.',
                'invalid_choice': 'Seleccione una materia valida.',
            },
            'periodo': {
                'required': 'Seleccione un periodo academico.',
                'invalid_choice': 'Seleccione un periodo academico valido.',
            },
            'nombre': {
                'required': 'El nombre de la evaluacion es obligatorio.',
            },
            'descripcion': {
                'required': 'La descripcion de la evaluacion es obligatoria.',
            },
            'peso': {
                'required': 'El peso de la evaluacion es obligatorio.',
                'invalid': 'Ingrese un peso valido.',
            },
            'estado': {
                'required': 'Seleccione el estado de la evaluacion.',
                'invalid_choice': 'Seleccione un estado valido.',
            },
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_materia(self):
        materia = self.cleaned_data.get('materia')

        if not materia:
            raise forms.ValidationError('Seleccione una materia.')

        return materia

    def clean_periodo(self):
        periodo = self.cleaned_data.get('periodo')

        if not periodo:
            raise forms.ValidationError('Seleccione un periodo academico.')

        return periodo

    def clean_nombre(self):
        nombre = (self.cleaned_data.get('nombre') or '').strip()

        if not nombre:
            raise forms.ValidationError(
                'El nombre de la evaluacion es obligatorio.'
            )

        return nombre

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')

        if peso is None:
            raise forms.ValidationError(
                'El peso de la evaluacion es obligatorio.'
            )

        if peso <= Decimal('0.00'):
            raise forms.ValidationError(
                'El peso de la evaluacion debe ser mayor que cero.'
            )

        return peso


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = [
            'matricula',
            'evaluacion',
            'calificacion',
            'observacion',
        ]
        labels = {
            'matricula': 'Matricula',
            'evaluacion': 'Evaluacion',
            'calificacion': 'Calificacion',
            'observacion': 'Observacion',
        }
        error_messages = {
            'matricula': {
                'required': 'Seleccione una matricula.',
                'invalid_choice': 'Seleccione una matricula valida.',
            },
            'evaluacion': {
                'required': 'Seleccione una evaluacion.',
                'invalid_choice': 'Seleccione una evaluacion valida.',
            },
            'calificacion': {
                'required': 'La calificacion es obligatoria.',
                'invalid': 'Ingrese una calificacion valida.',
            },
        }
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')

        if not matricula:
            raise forms.ValidationError('Seleccione una matricula.')

        return matricula

    def clean_evaluacion(self):
        evaluacion = self.cleaned_data.get('evaluacion')

        if not evaluacion:
            raise forms.ValidationError('Seleccione una evaluacion.')

        return evaluacion

    def clean_calificacion(self):
        calificacion = self.cleaned_data.get('calificacion')

        if calificacion is None:
            raise forms.ValidationError('La calificacion es obligatoria.')

        if calificacion < Decimal('0.00') or calificacion > Decimal('20.00'):
            raise forms.ValidationError(
                'La calificacion debe estar entre 0 y 20.'
            )

        return calificacion

    def clean(self):
        cleaned_data = super().clean()
        matricula = cleaned_data.get('matricula')
        evaluacion = cleaned_data.get('evaluacion')

        if matricula and evaluacion:
            notas = Nota.objects.filter(
                matricula=matricula,
                evaluacion=evaluacion,
            )

            if self.instance.pk:
                notas = notas.exclude(pk=self.instance.pk)

            if notas.exists():
                self.add_error(
                    'evaluacion',
                    'Ya existe una nota registrada para esta matricula y evaluacion.',
                )

        return cleaned_data
