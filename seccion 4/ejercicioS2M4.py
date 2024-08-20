class Animal:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    
    def descripcion(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años, Peso: {self.peso} kg"
    
#def clase

class Caballo(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, edad, raza, peso)

class Leon(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, edad, raza, peso)
        
#main

caballo = Caballo("Zeus", 5, "Pura Sangre", 450)
leon = Leon("Boulder", 10, "Atlas", 130)

print(caballo.descripcion())
print(leon.descripcion())

