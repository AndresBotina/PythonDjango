from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Autor, Libro
from .serializers import AutorSerializer, LibroSerializer

@api_view(['GET'])
def listado_libros(request):
    libros = Libro.objects.all()
    datos = [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor.nombre,
            "precio": libro.precio,
            "disponible": libro.disponible,
        }
        for libro in libros
    ]
    return Response(datos)

def inicio(request):
    return HttpResponse("Hola, soy tu padre!")

def resumen(request):
    total = Libro.objects.count()
    return HttpResponse(f"Actualmente hay {total} libros registrados en la biblioteca.")

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibroSerializer