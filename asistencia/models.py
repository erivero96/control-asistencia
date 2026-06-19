from django.db import models

from academico.models import Matricula


class Asistencia(models.Model):
    ESTADO_PRESENTE = 'presente'
    ESTADO_TARDANZA = 'tardanza'
    ESTADO_FALTA = 'falta'
    ESTADO_JUSTIFICADO = 'justificado'

    ESTADO_CHOICES = [
        (ESTADO_PRESENTE, 'Presente'),
        (ESTADO_TARDANZA, 'Tardanza'),
        (ESTADO_FALTA, 'Falta'),
        (ESTADO_JUSTIFICADO, 'Justificado'),
    ]

    matricula = models.ForeignKey(Matricula, on_delete=models.PROTECT)
    fecha = models.DateField()
    estado = models.CharField(
        max_length=11,
        choices=ESTADO_CHOICES,
        default=ESTADO_PRESENTE,
    )
    observacion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', 'matricula']
        verbose_name = 'asistencia'
        verbose_name_plural = 'asistencias'
        constraints = [
            models.UniqueConstraint(
                fields=['matricula', 'fecha'],
                name='asistencia_unica_por_matricula_fecha',
            ),
        ]

    def __str__(self):
        return f'{self.matricula} - {self.fecha} - {self.estado}'
