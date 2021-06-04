from django.db import models

"""En este archivo se crean las clases o modelos de la base de datos"""

"""Se crea un modelo de curso con sus respectivos atributos"""
class Curso(models.Model):
    CodigoCurso = models.CharField(max_length=20)
    NombreCurso = models.CharField(max_length=50)
    FechaInicio = models.DateField()
    FechaFin  = models.DateField()

    def __str__(self):
        return '{}-{}'.format(self.pk,self.CodigoCurso, self.NombreCurso)

"""Se crea un modelo de estudiante con sus respectivos atributos y se le asigna una lista de
Cursos para que un estudiante pueda estar en muchos cursos"""

class Estudiante(models.Model):
    OpcionesGenero = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N', 'NoDefinido')
    ]

    Nombres = models.CharField(max_length=80)
    Apellidos  = models.CharField(max_length=80)
    FechaNacimento  = models.DateField()
    Genero  = models.CharField(max_length=1, choices=OpcionesGenero)
    Cursos = models.ManyToManyField(Curso, verbose_name="Cursos")

    def __str__(self):
        return '{} {}'.format(self.pk,self.Nombres, self.Apellidos)

"""Se crea un modelo de dirreccion  con sus respectivos atributos y se le asigna una llave fornea de estudiante"""

class Direccion(models.Model):
    TiposDireccion = [
        ('D', 'Domicilio'), 
        ('L', 'Laboral'),
        ('T', 'Temporal')
    ]

    StringDireccion  = models.CharField(max_length=80)
    TipoDireccion = models.CharField(max_length=1, choices=TiposDireccion)
    Estudiante = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)

    def __str__(self):
        return self.StringDireccion