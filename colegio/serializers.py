from rest_framework import serializers
from .models import Curso, Estudiante


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'jornada']


class EstudianteSerializer(serializers.ModelSerializer):
    curso_nombre = serializers.CharField(source='curso.nombre', read_only=True)

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'curso', 'curso_nombre', 'pension', 'activo', 'fecha_nacimiento']
