from django.contrib import admin
from .models import Curso, Estudiante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nom_curso', 'annio')
    search_fields = ('nom_curso',)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'curso')
    list_filter = ('curso',)
    search_fields = ('nombre', 'apellido')

