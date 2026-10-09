# Función de operaciones aritméticas
# Recibe la operación a realizar y los parámetros x, y.
# Operaciones disponibles: "suma", "resta", "multiplicacion", "division"

def operaciones_aritmeticas(operacion, x, y):
    """
    Realiza la operación indicada entre x e y y retorna el resultado.
    """
    if operacion == "suma":
        resultado = x + y
    elif operacion == "resta":
        resultado = x - y
    elif operacion == "multiplicacion":
        resultado = x * y
    elif operacion == "division":
        if y == 0:
            return "Error: no se puede dividir entre cero"
        resultado = x / y
    else:
        return "Error: operación no válida"

    return resultado

# Llamadas a la función con cada operación
print("Suma:", operaciones_aritmeticas("suma", 10, 5))                      
print("Resta:", operaciones_aritmeticas("resta", 10, 5))                    
print("Multiplicación:", operaciones_aritmeticas("multiplicacion", 10, 5))  
print("División:", operaciones_aritmeticas("division", 10, 5))             

print("División entre cero:", operaciones_aritmeticas("division", 10, 0))