from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    jornada = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes')
    pension = models.DecimalField(max_digits=8, decimal_places=2)
    activo = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre
