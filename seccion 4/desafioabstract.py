from abc import ABC, abstractmethod

# Definición de la clase abstracta Vehiculo
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    @abstractmethod
    def moverse(self):
        pass
    
    @abstractmethod
    def descripcion(self):
        pass

# Clase hija Coche
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
    
    def moverse(self):
        return f"El coche {self.marca}, {self.modelo} está en movimiento."
    
    def descripcion(self):
        return f"Este coche es de marca {self.marca}, modelo {self.modelo}, fue fabricado en el año {self.año}."
    
    def arrancar(self):
        return f"El {self.marca}, {self.modelo} está arrancando."

# Clase hija Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
    
    def moverse(self):
        return f"La moto {self.marca}, {self.modelo} está en movimiento."
    
    def descripcion(self):
        return f"Esta moto es de marca {self.marca}, modelo {self.modelo}, fue fabricada en el año {self.año}."
    
    def prender(self):
        return f"La {self.marca}, {self.modelo} está prendida."

# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
    
    def moverse(self):
        return f"La bicicleta {self.marca}, {self.modelo} está siendo pedaleada."
    
    def descripcion(self):
        return f"Esta bicicleta es de marca {self.marca}, modelo {self.modelo}, fue fabricada en el año {self.año}."
    
    def ajustarAsiento(self):
        return f"El asiento de la {self.marca}, {self.modelo} está siendo ajustado."

# main

# Creación de instancias
mi_Auto = Auto("Toyota", "Yaris", 2017)
mi_moto = Moto("Honda", "CBR", 2020)
mi_bicicleta = Bicicleta("Trek", "FX 2", 2021)

# Uso de los métodos
print(mi_Auto.descripcion())
print(mi_Auto.moverse())
print(mi_Auto.arrancar())

print(mi_moto.descripcion())
print(mi_moto.moverse())
print(mi_moto.prender())

print(mi_bicicleta.descripcion())
print(mi_bicicleta.moverse())
print(mi_bicicleta.ajustarAsiento())
