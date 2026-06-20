from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Sum

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
        validators=[
            MinValueValidator(Decimal('1.00')),
            MaxValueValidator(Decimal('100.00')),
        ],
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
                condition=(
                    models.Q(peso__gte=1)
                    & models.Q(peso__lte=100)
                ),
                name='evaluacion_peso_entre_1_y_100',
            ),
            models.UniqueConstraint(
                fields=['materia', 'periodo', 'nombre'],
                name='evaluacion_unica_por_materia_periodo_nombre',
            ),
        ]

    def clean(self):
        super().clean()

        if not (
            self.materia_id
            and self.periodo_id
            and self.peso is not None
        ):
            return

        peso_total = (
            Evaluacion.objects
            .filter(materia_id=self.materia_id, periodo_id=self.periodo_id)
            .exclude(pk=self.pk)
            .aggregate(total=Sum('peso'))['total']
            or Decimal('0.00')
        )

        if peso_total + self.peso > Decimal('100.00'):
            raise ValidationError({
                'peso': (
                    'La suma de los pesos para esta materia y periodo '
                    'no puede superar 100.'
                ),
            })

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

    def clean(self):
        super().clean()

        if not self.matricula_id or not self.evaluacion_id:
            return

        errores = {}
        matricula = self.matricula
        evaluacion = self.evaluacion

        if matricula.estado != Matricula.ESTADO_MATRICULADO:
            errores['matricula'] = (
                'Solo se pueden registrar notas para matriculas activas.'
            )

        if (
            evaluacion.materia_id != matricula.materia_id
            or evaluacion.periodo_id != matricula.periodo_id
        ):
            errores['evaluacion'] = (
                'La evaluacion debe pertenecer a la misma materia y periodo '
                'de la matricula.'
            )

        if errores:
            raise ValidationError(errores)

    def __str__(self):
        return f'{self.matricula.estudiante} - {self.evaluacion}: {self.calificacion}'
