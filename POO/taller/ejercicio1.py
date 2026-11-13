# Ejercicio 1: Clases y objetos

# La clase es el molde
class Mascota:
    # Se ejecuta al crear la mascota y guarda sus datos
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y soy un {self.especie}")

    # Reto: suma un año
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ahora tiene {self.edad} años")


# Los objetos: mascotas reales hechas con el molde
perro = Mascota("Firulais", "perro", 3)
gato = Mascota("Michi", "gato", 2)

perro.presentarse()
gato.presentarse()

# Reto: cumple años dos veces
perro.cumplir_anios()
perro.cumplir_anios()
