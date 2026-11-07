from rest_framework import serializers
from .models import Curso, Estudiante


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nom_curso', 'annio']

    def validate_annio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El año debe ser mayor que cero.")
        return value


class EstudianteSerializer(serializers.ModelSerializer):
    curso_nombre = serializers.CharField(source='curso.nom_curso', read_only=True)

    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'apellido', 'curso', 'curso_nombre']

    def validate(self, data):
        # Validación que involucra más de un campo a la vez
        if 'nombre' in data and data['nombre'] == data.get('apellido'):
            raise serializers.ValidationError("El nombre y el apellido no pueden ser iguales.")
        return data
