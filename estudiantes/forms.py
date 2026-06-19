from django import forms

from .models import Estudiante


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'codigo',
            'nombres',
            'apellidos',
            'dni',
            'correo',
            'telefono',
            'direccion',
            'estado',
        ]
        labels = {
            'codigo': 'Codigo',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'dni': 'DNI',
            'correo': 'Correo electronico',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'estado': 'Estado',
        }
        error_messages = {
            'codigo': {
                'required': 'El codigo del estudiante es obligatorio.',
                'unique': 'Ya existe un estudiante registrado con este codigo.',
            },
            'nombres': {
                'required': 'Los nombres del estudiante son obligatorios.',
            },
            'apellidos': {
                'required': 'Los apellidos del estudiante son obligatorios.',
            },
            'dni': {
                'required': 'El DNI del estudiante es obligatorio.',
                'unique': 'Ya existe un estudiante registrado con este DNI.',
            },
            'correo': {
                'required': 'El correo electronico es obligatorio.',
                'invalid': 'Ingrese un correo electronico valido.',
            },
            'telefono': {
                'required': 'El telefono es obligatorio.',
            },
            'direccion': {
                'required': 'La direccion es obligatoria.',
            },
            'estado': {
                'required': 'Seleccione el estado del estudiante.',
                'invalid_choice': 'Seleccione un estado valido.',
            },
        }
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_codigo(self):
        codigo = (self.cleaned_data.get('codigo') or '').strip()

        if not codigo:
            raise forms.ValidationError(
                'El codigo del estudiante es obligatorio.'
            )

        return codigo

    def clean_dni(self):
        dni = (self.cleaned_data.get('dni') or '').strip()

        if not dni:
            raise forms.ValidationError('El DNI del estudiante es obligatorio.')

        if not dni.isdigit() or len(dni) != 8:
            raise forms.ValidationError('El DNI debe tener exactamente 8 digitos.')

        return dni

    def clean_nombres(self):
        nombres = (self.cleaned_data.get('nombres') or '').strip()

        if not nombres:
            raise forms.ValidationError(
                'Los nombres del estudiante son obligatorios.'
            )

        return nombres

    def clean_apellidos(self):
        apellidos = (self.cleaned_data.get('apellidos') or '').strip()

        if not apellidos:
            raise forms.ValidationError(
                'Los apellidos del estudiante son obligatorios.'
            )

        return apellidos
