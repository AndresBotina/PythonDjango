#atributos de clase: son caracteristicas comunes a todos los objetos de una clase.
#Se definen dentro de la clase pero fuera de cualquier metodo
#Se accede a ellos mediante la clase o mediante un objeto de la clase

class Carro:
    modelo= "Deportivo"

    def __init__(self, tipo, marca):
        #Atributos de instancia;propios de cada objeto
        self.tipo=tipo
        self.marca=marca

    #esto es unmetodo de instancia ,que es una funcioon que pertenece
    #a la casa y que puede acceder a los atributos de instancia y de clase
    #siempre se definen con verbos en infinitivo(ar,er,ir)
    def Acelerar(self):
        return f"{self.marca} dice: ¡Runnnnnnnnn!" 

Ferrari=Carro( "Gasolina","Ferrari")
lambo=Carro("Electrico","Lambo")

#acceso a atributos de clase
print(f"Marca de carro {Ferrari.marca}:{Ferrari.tipo}")
print(f"Marca de carro {lambo.marca}:{lambo.tipo}")

#acceso a atributos de instancia

print(f"{Ferrari.marca} es un carro a {Ferrari.tipo}.")
print(f"{lambo.marca} es un carro {lambo.tipo}.")

#llamada a metodos de instancia
print(Ferrari.Acelerar())
print(lambo.Acelerar())
                                                        #NOTA: Los atributos privados, eje: (__nombreAtributo), no se puede acceder directamente
#____________________________________________________________________________________________________
class Contador:
    total = 0 #de clase

    def __init__(self):
        Contador.total +=1
        self.numero = Contador.total # De instancia

a = Contador()
b = Contador()

print(a.numero, b.numero, Contador.total)

#____________________________________________________________________________________________________
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # privado, no se puede acceder ni con decorador

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto     #Variable privada, no se puede acceder ni con decorador   

    def retirar(self, monto):
        if monto > self.__saldo:
            raise ValueError("Fondos insuficientes")
        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.consultar_saldo())  # 1500
# print(cuenta.__saldo)  # AttributeError           #Variable privada, no se puede acceder ni con decorador (@property)

#____________________________________________________________________________________________________
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius  # pasa por el setter

    @property           #Esto es un decorador, con este decorador se puede acceder a datos protegidos.
    def celsius(self):
        return self._celsius   #Con una  raya al piso eldato esta privada

    @celsius.setter     #Esto es un decorador, con este decorador se puede acceder a datos protegidos.
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Por debajo del cero absoluto")
        self._celsius = valor #Variable protegida

    @property           ##Esto es un decorador, con este decorador se puede acceder a datos protegidos.
    def fahrenheit(self):  # propiedad calculada, solo lectura
        return self._celsius * 9 / 5 + 32   #Varible protegida, se puede acceder con el decorador


t = Temperatura(25)
print(t.fahrenheit)  # 77.0
t.celsius = 30  # usa el setter con validación.

#HERENCIAAA
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def descripcion(self):
        return f"{self.nombre} gana ${self.salario:,.0f}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)  # inicializa la parte del padre
        self.equipo = equipo

    def descripcion(self):  # sobrescritura (override)
        base = super().descripcion()
        return f"{base} y dirige a {len(self.equipo)} personas"


g = Gerente("Marta", 8_000_000, ["Luis", "Sara"])
print(g.descripcion())
print(isinstance(g, Empleado))       # True
print(issubclass(Gerente, Empleado)) # True 


#POLIMORFISMO





# ===== 5. Polimorfismo y abstracción =====

# Polimorfismo por herencia
class Figura:
    def area(self):
        raise NotImplementedError


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base, self.altura = base, altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2


figuras = [Rectangulo(3, 4), Circulo(2)]
for f in figuras:
    print(f.area())  # mismo mensaje, resultado distinto


# Duck typing
class Pato:
    def sonar(self):
        return "Cuac"


class Robot:
    def sonar(self):
        return "Bip"


def hacer_sonar(obj):
    print(obj.sonar())  # funciona con cualquier objeto que tenga sonar()


hacer_sonar(Pato())
hacer_sonar(Robot())


# Clases abstractas con abc
from abc import ABC, abstractmethod


class Pago(ABC):
    @abstractmethod
    def procesar(self, monto): ...


class Tarjeta(Pago):
    def procesar(self, monto):
        return f"Cobrando ${monto} a tarjeta"


# Pago()  # TypeError: no se puede instanciar una clase abstracta
print(Tarjeta().procesar(100))
