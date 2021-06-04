from rest_framework import serializers

from api.models import Estudiante,Curso, Direccion

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