# 5.1. Ejemplos Avanzados de Funciones
# B. Integración de Funciones con Estructuras Combinadas

def procesar_evaluaciones(estudiantes):
    """
    Recibe una lista de diccionarios y retorna una tupla estructurada:
    (promedio_general, mejor_estudiante)
    """
    if not estudiantes:
        return (0.0, None)

    suma_notas = 0.0
    mejor_estudiante = estudiantes[0]

    for est in estudiantes:
        suma_notas += est.get("nota", 0.0)
        if est.get("nota", 0.0) > mejor_estudiante.get("nota", 0.0):
            mejor_estudiante = est

    promedio = suma_notas / len(estudiantes)
    return (round(promedio, 2), mejor_estudiante.get("nombre"))


# Datos de entrada
grupo = [
    {"nombre": "Ana", "nota": 4.5},
    {"nombre": "Carlos", "nota": 3.8},
    {"nombre": "Elena", "nota": 4.9}
]

prom, mejor = procesar_evaluaciones(grupo)  # Resultado: prom = 4.4, mejor = 'Elena'

print("Promedio general:", prom)
print("Mejor estudiante:", mejor)
