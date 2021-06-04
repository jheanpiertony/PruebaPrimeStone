
from rest_framework import serializers

from api.models import Estudiante,Curso, Direccion

""" 
Creditos

Autor = Gerardo Beltran Pulido
version = "1.0.0
correo = "gerbel06@gmail.com
Estado = "Dev
Fecha = "2021-06-04


"""


"""Se crean los serializadores para el api de cada modelo para que retorne jsons"""


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('CodigoCurso', 'NombreCurso', 'FechaInicio', 'FechaFin')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('Nombres', 'Apellidos', 'FechaNacimento', 'Genero', 'Cursos')

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = ('StringDireccion', 'TipoDireccion', 'Estudiante')