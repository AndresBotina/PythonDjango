from django.contrib import admin

# Register your models here.
from .models import Curso, Estudiante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'jornada')
    search_fields = ('nombre',)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso', 'pension', 'activo')
    list_filter = ('activo', 'curso')
    search_fields = ('nombre',)