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




class Contador:
    total = 0 #de clase

    def __init__(self):
        Contador.total +=1
        self.numero = Contador.total # De instancia

a = Contador()
b = Contador()

print(a.numero, b.numero, Contador.total)

