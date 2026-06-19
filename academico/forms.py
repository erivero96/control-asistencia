from django import forms

from .models import Materia, Matricula, PeriodoAcademico


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = [
            'codigo',
            'nombre',
            'descripcion',
            'creditos',
            'estado',
        ]
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'creditos': 'Creditos',
            'estado': 'Estado',
        }
        error_messages = {
            'codigo': {
                'required': 'El codigo de la materia es obligatorio.',
                'unique': 'Ya existe una materia registrada con este codigo.',
            },
            'nombre': {
                'required': 'El nombre de la materia es obligatorio.',
            },
            'descripcion': {
                'required': 'La descripcion de la materia es obligatoria.',
            },
            'creditos': {
                'required': 'Los creditos de la materia son obligatorios.',
                'invalid': 'Ingrese un numero valido de creditos.',
            },
            'estado': {
                'required': 'Seleccione el estado de la materia.',
                'invalid_choice': 'Seleccione un estado valido.',
            },
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_codigo(self):
        codigo = (self.cleaned_data.get('codigo') or '').strip()

        if not codigo:
            raise forms.ValidationError(
                'El codigo de la materia es obligatorio.'
            )

        return codigo

    def clean_nombre(self):
        nombre = (self.cleaned_data.get('nombre') or '').strip()

        if not nombre:
            raise forms.ValidationError(
                'El nombre de la materia es obligatorio.'
            )

        return nombre

    def clean_creditos(self):
        creditos = self.cleaned_data.get('creditos')

        if creditos is None:
            raise forms.ValidationError(
                'Los creditos de la materia son obligatorios.'
            )

        if creditos <= 0:
            raise forms.ValidationError(
                'Los creditos deben ser mayores que cero.'
            )

        return creditos


class PeriodoAcademicoForm(forms.ModelForm):
    class Meta:
        model = PeriodoAcademico
        fields = [
            'nombre',
            'fecha_inicio',
            'fecha_fin',
            'estado',
        ]
        labels = {
            'nombre': 'Nombre',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_fin': 'Fecha de fin',
            'estado': 'Estado',
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre del periodo academico es obligatorio.',
                'unique': 'Ya existe un periodo academico con este nombre.',
            },
            'fecha_inicio': {
                'required': 'La fecha de inicio es obligatoria.',
                'invalid': 'Ingrese una fecha de inicio valida.',
            },
            'fecha_fin': {
                'required': 'La fecha de fin es obligatoria.',
                'invalid': 'Ingrese una fecha de fin valida.',
            },
            'estado': {
                'required': 'Seleccione el estado del periodo academico.',
                'invalid_choice': 'Seleccione un estado valido.',
            },
        }
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            self.add_error(
                'fecha_fin',
                'La fecha de fin no puede ser menor que la fecha de inicio.',
            )

        return cleaned_data


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = [
            'estudiante',
            'materia',
            'periodo',
            'estado',
        ]
        labels = {
            'estudiante': 'Estudiante',
            'materia': 'Materia',
            'periodo': 'Periodo academico',
            'estado': 'Estado',
        }
        error_messages = {
            'estudiante': {
                'required': 'Seleccione un estudiante.',
                'invalid_choice': 'Seleccione un estudiante valido.',
            },
            'materia': {
                'required': 'Seleccione una materia.',
                'invalid_choice': 'Seleccione una materia valida.',
            },
            'periodo': {
                'required': 'Seleccione un periodo academico.',
                'invalid_choice': 'Seleccione un periodo academico valido.',
            },
            'estado': {
                'required': 'Seleccione el estado de la matricula.',
                'invalid_choice': 'Seleccione un estado valido.',
            },
        }

    def clean_estudiante(self):
        estudiante = self.cleaned_data.get('estudiante')

        if not estudiante:
            raise forms.ValidationError('Seleccione un estudiante.')

        return estudiante

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

    def clean(self):
        cleaned_data = super().clean()
        estudiante = cleaned_data.get('estudiante')
        materia = cleaned_data.get('materia')
        periodo = cleaned_data.get('periodo')

        if estudiante and materia and periodo:
            matriculas = Matricula.objects.filter(
                estudiante=estudiante,
                materia=materia,
                periodo=periodo,
            )

            if self.instance.pk:
                matriculas = matriculas.exclude(pk=self.instance.pk)

            if matriculas.exists():
                self.add_error(
                    'periodo',
                    'El estudiante ya esta matriculado en esta materia y periodo.',
                )

        return cleaned_data
