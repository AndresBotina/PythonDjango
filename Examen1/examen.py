#parte 3 punto 1

productos = [
    ("frijoles", 8000, 10),
    ("arroz", 4000, 3),
    ("leche", 5000, 5),
    ("huevos", 18000, 2),
    ("maduros", 2000, 20)
]
def crear_inventario(productos):
    inventario = {}
    for producto in productos:
        nombre = producto[0]
        precio = producto[1]
        stock = producto[2]
        inventario[nombre] = {"precio": precio, "stock": stock}
    return inventario
inv = crear_inventario(productos)
print(inv)


#PArte 3 punto 2

def valor_total(inventario):
    total = 0
    for nombre in inventario:
        precio = inventario[nombre]["precio"]
        stock = inventario[nombre]["stock"]
        total = total + precio * stock
    return total
print(valor_total(inv))

#Parte 3 punto3


def productos_bajo_stock(inventario, minimo=5):
    bajos = []
    for nombre in inventario:
        stock = inventario[nombre]["stock"]
        if stock < minimo:
            bajos.append(nombre)
    bajos.sort()
    return bajos
print(productos_bajo_stock(inv))


#PArte3 punto 4

def producto_mas_caro(inventario):
    mas_caro = ""
    precio_mayor = 0
    for nombre in inventario:
        precio = inventario[nombre]["precio"]
        if precio > precio_mayor:
            precio_mayor = precio
            mas_caro = nombre
    return (mas_caro, precio_mayor)
print(producto_mas_caro(inv))


#Parte 3 punto 5

def aplicar_descuento(inventario, porcentaje):
    nuevo = {}
    for nombre in inventario:
        precio = inventario[nombre]["precio"]
        stock = inventario[nombre]["stock"]
        precio_nuevo = precio - precio * porcentaje / 100
        nuevo[nombre] = {"precio": precio_nuevo, "stock": stock}
    return nuevo
print(aplicar_descuento(inv, 10)["frijoles"])
print(inv["frijoles"])

