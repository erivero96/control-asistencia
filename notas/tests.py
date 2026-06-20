from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

from academico.models import Materia, Matricula, PeriodoAcademico
from estudiantes.models import Estudiante

from .forms import EvaluacionForm, NotaForm
from .models import Evaluacion, Nota


class NotasFormValidationTests(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            codigo='EST-0001',
            nombres='Ana',
            apellidos='Torres',
            dni='12345678',
            correo='ana@example.com',
            telefono='999999999',
            direccion='Lima',
        )
        self.materia = Materia.objects.create(
            codigo='MAT-0001',
            nombre='Matematica',
            descripcion='Fundamentos de matematica.',
            creditos=4,
        )
        self.materia_secundaria = Materia.objects.create(
            codigo='MAT-0002',
            nombre='Comunicacion',
            descripcion='Comunicacion oral y escrita.',
            creditos=3,
        )
        self.materia_inactiva = Materia.objects.create(
            codigo='MAT-0003',
            nombre='Historia',
            descripcion='Historia universal.',
            creditos=3,
            estado=Materia.ESTADO_INACTIVO,
        )
        self.periodo = PeriodoAcademico.objects.create(
            nombre='2026-I',
            fecha_inicio='2026-03-01',
            fecha_fin='2026-07-31',
        )
        self.periodo_secundario = PeriodoAcademico.objects.create(
            nombre='2026-II',
            fecha_inicio='2026-08-01',
            fecha_fin='2026-12-20',
        )
        self.periodo_finalizado = PeriodoAcademico.objects.create(
            nombre='2025-II',
            fecha_inicio='2025-08-01',
            fecha_fin='2025-12-20',
            estado=PeriodoAcademico.ESTADO_FINALIZADO,
        )
        self.matricula = Matricula.objects.create(
            estudiante=self.estudiante,
            materia=self.materia,
            periodo=self.periodo,
        )
        self.matricula_retirada = Matricula.objects.create(
            estudiante=self.estudiante,
            materia=self.materia_secundaria,
            periodo=self.periodo,
            estado=Matricula.ESTADO_RETIRADO,
        )
        self.matricula_finalizada = Matricula.objects.create(
            estudiante=self.estudiante,
            materia=self.materia,
            periodo=self.periodo_secundario,
            estado=Matricula.ESTADO_FINALIZADO,
        )
        self.evaluacion = Evaluacion.objects.create(
            materia=self.materia,
            periodo=self.periodo,
            nombre='Parcial',
            descripcion='Evaluacion parcial.',
            peso=Decimal('40.00'),
        )
        self.evaluacion_otra_materia = Evaluacion.objects.create(
            materia=self.materia_secundaria,
            periodo=self.periodo,
            nombre='Parcial',
            descripcion='Evaluacion de otra materia.',
            peso=Decimal('40.00'),
        )
        self.evaluacion_otro_periodo = Evaluacion.objects.create(
            materia=self.materia,
            periodo=self.periodo_secundario,
            nombre='Parcial',
            descripcion='Evaluacion de otro periodo.',
            peso=Decimal('40.00'),
        )

    def datos_evaluacion(self, **cambios):
        datos = {
            'materia': self.materia.id,
            'periodo': self.periodo.id,
            'nombre': 'Final',
            'descripcion': 'Evaluacion final.',
            'peso': '60.00',
            'estado': Evaluacion.ESTADO_ACTIVO,
        }
        datos.update(cambios)
        return datos

    def datos_nota(self, **cambios):
        datos = {
            'matricula': self.matricula.id,
            'evaluacion': self.evaluacion.id,
            'calificacion': '16.00',
            'observacion': '',
        }
        datos.update(cambios)
        return datos

    def test_evaluacion_form_muestra_solo_materias_y_periodos_activos(self):
        formulario = EvaluacionForm()

        self.assertNotIn(
            self.materia_inactiva,
            formulario.fields['materia'].queryset,
        )
        self.assertNotIn(
            self.periodo_finalizado,
            formulario.fields['periodo'].queryset,
        )

    def test_peso_de_evaluacion_debe_estar_entre_uno_y_cien(self):
        for peso in ('0.99', '100.01'):
            with self.subTest(peso=peso):
                formulario = EvaluacionForm(
                    self.datos_evaluacion(peso=peso),
                )

                self.assertFalse(formulario.is_valid())
                self.assertIn('peso', formulario.errors)

    def test_no_permite_superar_cien_por_materia_y_periodo(self):
        formulario = EvaluacionForm(self.datos_evaluacion(peso='60.01'))

        self.assertFalse(formulario.is_valid())
        self.assertIn('peso', formulario.errors)

    def test_no_permite_evaluaciones_duplicadas(self):
        formulario = EvaluacionForm(
            self.datos_evaluacion(nombre=self.evaluacion.nombre, peso='20.00'),
        )

        self.assertFalse(formulario.is_valid())

    def test_nota_form_muestra_solo_matriculas_matriculadas(self):
        formulario = NotaForm()

        self.assertIn(self.matricula, formulario.fields['matricula'].queryset)
        self.assertNotIn(
            self.matricula_retirada,
            formulario.fields['matricula'].queryset,
        )
        self.assertNotIn(
            self.matricula_finalizada,
            formulario.fields['matricula'].queryset,
        )

    def test_no_permite_nota_con_evaluacion_de_otra_materia_o_periodo(self):
        evaluaciones_incompatibles = [
            self.evaluacion_otra_materia,
            self.evaluacion_otro_periodo,
        ]

        for evaluacion in evaluaciones_incompatibles:
            with self.subTest(evaluacion=evaluacion.id):
                formulario = NotaForm(
                    self.datos_nota(evaluacion=evaluacion.id),
                )

                self.assertFalse(formulario.is_valid())
                self.assertIn('evaluacion', formulario.errors)

    def test_no_permite_nota_para_matricula_retirada_o_finalizada(self):
        casos = [self.matricula_retirada, self.matricula_finalizada]

        for matricula in casos:
            with self.subTest(matricula=matricula.id):
                formulario = NotaForm(
                    self.datos_nota(matricula=matricula.id),
                )

                self.assertFalse(formulario.is_valid())
                self.assertIn('matricula', formulario.errors)

    def test_guarda_nota_valida(self):
        formulario = NotaForm(self.datos_nota())

        self.assertTrue(formulario.is_valid())

        nota = formulario.save()

        self.assertEqual(nota.matricula, self.matricula)
        self.assertEqual(nota.evaluacion, self.evaluacion)

    def test_modelo_nota_valida_relacion_de_materia_y_periodo(self):
        nota = Nota(
            matricula=self.matricula,
            evaluacion=self.evaluacion_otra_materia,
            calificacion=Decimal('16.00'),
        )

        with self.assertRaises(ValidationError):
            nota.full_clean()
