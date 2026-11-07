from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('cursos', views.CursoViewSet, basename='curso')
router.register('estudiantes', views.EstudianteViewSet, basename='estudiante')

urlpatterns = [
    path('', views.inicio, name='matricula_inicio'),
    path('api/estudiantes/', views.listado_estudiantes, name='api_estudiantes'),
    path('cursos/actuales/', views.CursoActualAPIView.as_view(), name='cursos_actuales'),
    path('', include(router.urls)),
]
