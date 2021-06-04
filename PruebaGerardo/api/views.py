from rest_framework import viewsets
from api.serializers import EstudianteSerializer, CursoSerializer,DireccionSerializer
from api.models import Estudiante,Curso,Direccion
from rest_framework.permissions import IsAuthenticated


def home(request):
    """
    """
    context = admin.site.each_context(request)
    context.update({'title': _('Home'), })

    template = 'home.html'
    return render(request, template, context)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('CodigoCurso')
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all().order_by('Nombres')
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all().order_by('StringDireccion')
    serializer_class = DireccionSerializer
    permission_classes = [IsAuthenticated]