from django.db import models


class Curso(models.Model):
    nom_curso = models.CharField(max_length=50)
    annio = models.IntegerField()

    def __str__(self):
        return self.nom_curso


class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return self.nombre
