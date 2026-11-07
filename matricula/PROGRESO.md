# Progreso de la app `matricula`

**Vamos en el Paso 11: Generic Views (sesión 09).** Continuar desde aquí.

## Cómo trabajamos
- Una sola acción a la vez, con poco texto.
- Usar solo lo visto en las sesiones o en las apps `biblioteca`, `colegio` e `inventario`.
- Yo escribo el código; Claude lo copia solo si se lo pido.

## Modelos
- `Curso`: `nom_curso`, `annio`
- `Estudiante`: `nombre`, `apellido`, `curso` (ForeignKey a `Curso`)

## Pasos
- [x] 1. Crear la app y registrarla en `INSTALLED_APPS`
- [x] 2. Vista simple y URLs
- [x] 3. Modelos con ForeignKey
- [x] 4. `makemigrations` y `migrate`
- [x] 5. Datos de prueba desde el shell
- [x] 6. Admin personalizado
- [x] 7. Endpoint con `@api_view`: `/matricula/api/estudiantes/`
- [x] 8. Serializers con `source`, `validate_annio` y `validate`
- [x] 9. ViewSets y Router: `/matricula/cursos/` y `/matricula/estudiantes/`
- [x] 10. APIView: `/matricula/cursos/actuales/`
- [ ] 11. Generic Views
- [ ] 12. Prueba final en la Browsable API

## Qué sigue

### Paso 11: Generic Views
Todavía no hay nada de este paso en `matricula/views.py`.

1. Agregar arriba de `matricula/views.py`:

```python
from rest_framework import generics
```

2. Agregar al final de `matricula/views.py`:

```python
class CursoListCreateView(generics.ListCreateAPIView):
    serializer_class = CursoSerializer

    def get_queryset(self):
        return Curso.objects.filter(annio=2026).order_by('nom_curso')


class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
```

3. Conectar las dos vistas en `matricula/urls.py`, antes de la línea del router, usando `.as_view()`.
4. Comparar la Generic View con `CursoActualAPIView` y anotar en un comentario cuántas líneas se ahorraron (ejercicio de la sesión 09).

### Paso 12: prueba final
En `/matricula/estudiantes/` probar, en orden: GET, POST inválido, POST válido, PATCH y DELETE.

## Notas
- En el otro PC hay que pasar los archivos actualizados. Allá ya se agregó `'rest_framework'` a `INSTALLED_APPS`.
- Si `matricula/views.py` está abierto con una versión vieja, cerrarlo sin guardar y volver a abrirlo.
