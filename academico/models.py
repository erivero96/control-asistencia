from django.core.exceptions import ValidationError
from django.db import models

from core.utils.codigos import generar_codigo
from estudiantes.models import Estudiante


class Materia(models.Model):
    ESTADO_ACTIVO = 'activo'
    ESTADO_INACTIVO = 'inactivo'

    ESTADO_CHOICES = [
        (ESTADO_ACTIVO, 'Activo'),
        (ESTADO_INACTIVO, 'Inactivo'),
    ]

    codigo = models.CharField(max_length=20, unique=True, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.PositiveSmallIntegerField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO,
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'materia'
        verbose_name_plural = 'materias'

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = generar_codigo(
                modelo=type(self),
                nombre_campo='codigo',
                prefijo='MAT',
                cantidad_digitos=4,
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'


class PeriodoAcademico(models.Model):
    ESTADO_ACTIVO = 'activo'
    ESTADO_INACTIVO = 'inactivo'
    ESTADO_FINALIZADO = 'finalizado'

    ESTADO_CHOICES = [
        (ESTADO_ACTIVO, 'Activo'),
        (ESTADO_INACTIVO, 'Inactivo'),
        (ESTADO_FINALIZADO, 'Finalizado'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO,
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_inicio', 'nombre']
        verbose_name = 'periodo academico'
        verbose_name_plural = 'periodos academicos'
        constraints = [
            models.CheckConstraint(
                condition=models.Q(fecha_fin__gte=models.F('fecha_inicio')),
                name='periodo_fecha_fin_gte_inicio',
            ),
        ]

    def clean(self):
        super().clean()
        if self.fecha_inicio and self.fecha_fin and self.fecha_fin < self.fecha_inicio:
            raise ValidationError({
                'fecha_fin': 'La fecha de fin no puede ser menor que la fecha de inicio.',
            })

    def __str__(self):
        return self.nombre


class Matricula(models.Model):
    ESTADO_MATRICULADO = 'matriculado'
    ESTADO_RETIRADO = 'retirado'
    ESTADO_FINALIZADO = 'finalizado'

    ESTADO_CHOICES = [
        (ESTADO_MATRICULADO, 'Matriculado'),
        (ESTADO_RETIRADO, 'Retirado'),
        (ESTADO_FINALIZADO, 'Finalizado'),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    periodo = models.ForeignKey(PeriodoAcademico, on_delete=models.PROTECT)
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=12,
        choices=ESTADO_CHOICES,
        default=ESTADO_MATRICULADO,
    )

    class Meta:
        ordering = ['-fecha_matricula']
        verbose_name = 'matricula'
        verbose_name_plural = 'matriculas'
        constraints = [
            models.UniqueConstraint(
                fields=['estudiante', 'materia', 'periodo'],
                name='matricula_unica_por_estudiante_materia_periodo',
            ),
        ]

    def __str__(self):
        return f'{self.estudiante} - {self.materia} - {self.periodo}'
