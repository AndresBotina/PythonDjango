grupos = [
    ("Grupo A", "Matemáticas", 30),
    ("Grupo B", "Programación", 25),
    ("Grupo C", "Inglés", 18),
]
# Cada tupla: (grupo, materia, estudiantes)


def crear_registro(grupos):
    registro = {}
    for grupo, materia, estudiantes in grupos:
        registro[grupo] = {"materia": materia, "estudiantes": estudiantes}
    return registro


registro = crear_registro(grupos)
# {"Grupo A": {"materia": "Matemáticas", "estudiantes": 30}, "Grupo B": {...}, ...}

print(registro)
