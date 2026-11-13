# Ejercicio 2: Atributos de clase vs. de instancia

class Mascota:
    # De clase: lo comparten todas las mascotas
    reino = "Animal"
    total_mascotas = 0

    def __init__(self, nombre, especie):
        # De instancia: cada mascota tiene el suyo
        self.nombre = nombre
        self.especie = especie
        # Cada mascota nueva suma 1 al total
        Mascota.total_mascotas += 1

    # Reto
    def mostrar_total(self):
        print(f"Hay {Mascota.total_mascotas} mascotas registradas")


m1 = Mascota("Firulais", "perro")
m2 = Mascota("Michi", "gato")
m3 = Mascota("Piolín", "pájaro")

print("Total de mascotas:", Mascota.total_mascotas)
print(m1.reino, m2.reino)
print(m1.nombre, m2.nombre, m3.nombre)

m1.mostrar_total()

# Reto: si hago "del m1", el total sigue en 3 porque nadie le resta.
# Se soluciona con un metodo que reste 1 antes de borrarla:
#   def eliminar(self):
#       Mascota.total_mascotas -= 1
