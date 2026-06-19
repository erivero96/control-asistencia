from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from academico.models import Materia, Matricula, PeriodoAcademico


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


class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.PROTECT)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.PROTECT)
    calificacion = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal('0.00')),
            MaxValueValidator(Decimal('20.00')),
        ],
    )
    observacion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'nota'
        verbose_name_plural = 'notas'
        constraints = [
            models.UniqueConstraint(
                fields=['matricula', 'evaluacion'],
                name='nota_unica_por_matricula_evaluacion',
            ),
            models.CheckConstraint(
                condition=(
                    models.Q(calificacion__gte=0)
                    & models.Q(calificacion__lte=20)
                ),
                name='nota_calificacion_entre_0_y_20',
            ),
        ]

    def __str__(self):
        return f'{self.matricula.estudiante} - {self.evaluacion}: {self.calificacion}'
