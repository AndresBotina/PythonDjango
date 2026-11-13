# Ejercicio 4: Herencia

# Clase padre
class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo")


# Perro hereda de Mascota
class Perro(Mascota):
    def __init__(self, nombre, raza):
        super().__init__(nombre)   # el padre guarda el nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")


# Gato hereda de Mascota
class Gato(Mascota):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")


# Reto: Cachorro hereda de Perro
class Cachorro(Perro):
    def jugar(self):
        print(f"{self.nombre} está jugando con la pelota")


perro = Perro("Firulais", "Labrador")
gato = Gato("Michi", "negro")

perro.comer()     # heredado
perro.ladrar()    # propio
gato.comer()      # heredado
gato.maullar()    # propio

# Reto
c = Cachorro("Toby", "Pug")
c.comer()
c.ladrar()
c.jugar()

# Un Cachorro hereda de Perro, y por medio de Perro, de Mascota.
