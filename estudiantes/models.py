from django.db import models

from core.utils.codigos import generar_codigo


class Estudiante(models.Model):
    ESTADO_ACTIVO = 'activo'
    ESTADO_INACTIVO = 'inactivo'

    ESTADO_CHOICES = [
        (ESTADO_ACTIVO, 'Activo'),
        (ESTADO_INACTIVO, 'Inactivo'),
    ]

    codigo = models.CharField(max_length=20, unique=True, editable=False)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    correo = models.EmailField(max_length=120)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO,
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['apellidos', 'nombres']
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = generar_codigo(
                modelo=type(self),
                nombre_campo='codigo',
                prefijo='EST',
                cantidad_digitos=4,
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.codigo} - {self.nombres} {self.apellidos}'
