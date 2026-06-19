from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from academico.models import Materia, PeriodoAcademico


class Evaluacion(models.Model):
    ESTADO_ACTIVO = 'activo'
    ESTADO_INACTIVO = 'inactivo'

    ESTADO_CHOICES = [
        (ESTADO_ACTIVO, 'Activo'),
        (ESTADO_INACTIVO, 'Inactivo'),
    ]

    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    periodo = models.ForeignKey(PeriodoAcademico, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        help_text='Porcentaje de la evaluacion.',
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO,
    )

    class Meta:
        ordering = ['materia', 'periodo', 'nombre']
        verbose_name = 'evaluacion'
        verbose_name_plural = 'evaluaciones'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(peso__gt=0),
                name='evaluacion_peso_mayor_que_cero',
            ),
        ]

    def __str__(self):
        return f'{self.nombre} - {self.materia} - {self.periodo}'
