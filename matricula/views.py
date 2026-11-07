from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from .models import Curso, Estudiante
from .serializers import CursoSerializer, EstudianteSerializer


def inicio(request):
    return HttpResponse("Bienvenido al sistema Matricula")


@api_view(['GET'])
def listado_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    datos = [
        {
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "curso": estudiante.curso.nom_curso,
        }
        for estudiante in estudiantes
    ]
    return Response(datos)


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('nom_curso')
    serializer_class = CursoSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all().order_by('nombre')
    serializer_class = EstudianteSerializer


class CursoActualAPIView(APIView):

    def get(self, request):
        cursos = Curso.objects.filter(annio=2026)
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
