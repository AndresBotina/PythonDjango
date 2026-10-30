from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Curso, Estudiante
from .serializers import CursoSerializer, EstudianteSerializer


@api_view(['GET'])
def listado_cursos(request):
    cursos = Curso.objects.all()
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listado_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    serializer = EstudianteSerializer(estudiantes, many=True)
    return Response(serializer.data)
