# Ejercicio 3: Encapsulamiento

class Mascota:
    def __init__(self, nombre, dueno, edad, peso):
        self.nombre = nombre    # publico: se usa libre
        self._dueno = dueno     # protegido: por acuerdo, no tocar desde afuera
        self.__edad = edad      # privado: escondido fuera de la clase
        self.__peso = peso      # privado (reto)

    # get: leer la edad
    def get_edad(self):
        return self.__edad

    # set: cambiar la edad, revisando que no sea negativa
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Error: la edad no puede ser negativa")

    # Reto: el peso debe estar entre 0 y 100
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0 and nuevo_peso <= 100:
            self.__peso = nuevo_peso
        else:
            print("Error: el peso debe ser mayor que 0 y maximo 100 kg")


m = Mascota("Firulais", "Ana", 3, 20)

print(m.nombre)
print(m._dueno)
m.set_edad(-5)
m.set_edad(4)
print(m.get_edad())

# Esto da error porque __edad es privado:
# print(m.__edad)

# Reto
m.set_peso(150)
m.set_peso(25)
print(m.get_peso())
