# Ejercicio 5: Polimorfismo y abstraccion

from abc import ABC, abstractmethod


# Clase abstracta: dice que deben hacer los hijos, pero no se pueden crear objetos de ella
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

    # Reto: segundo metodo obligatorio
    @abstractmethod
    def moverse(self):
        pass


# Cada hijo escribe su propia version de los metodos
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} corre")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} salta")


class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Muuu!")

    def moverse(self):
        print(f"{self.nombre} camina despacio")


# Reto: nueva clase
class Pajaro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre}: ¡Pío!")

    def moverse(self):
        print(f"{self.nombre} vuela")


animales = [Perro("Firulais"), Gato("Michi"), Vaca("Lola"), Pajaro("Piolín")]

# Polimorfismo: el mismo metodo, un resultado distinto en cada animal
for a in animales:
    a.hacer_sonido()

for a in animales:
    a.moverse()

# Esto da error porque Animal es abstracta:
# Animal("X")
