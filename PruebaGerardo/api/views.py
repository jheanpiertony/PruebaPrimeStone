from rest_framework import viewsets
from api.serializers import EstudianteSerializer, CursoSerializer,DireccionSerializer
from api.models import Estudiante,Curso,Direccion
from rest_framework.permissions import IsAuthenticated

""" 
Creditos

Autor = Gerardo Beltran Pulido
version = "1.0.0
correo = "gerbel06@gmail.com
Estado = "Dev
Fecha = "2021-06-04


"""


"""Se crean las views para consumir la api y se le agrega los serializadores y la autenticacion por JWT"""

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('pk')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all().order_by('pk')
    serializer_class = EstudianteSerializer


class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all().order_by('pk')
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticated]