class Animal:
    def __init__(self, nombre, edad, raza, peso):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    
    def descripcion(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad} años, Peso: {self.peso} kg"

    def comer(self):
        return f"{self.nombre} está comiendo."
    
    def caminar(self):
        return f"{self.nombre} está caminando."
    
    def dormir(self):
        return f"{self.nombre} está durmiendo."
    
#def clase

class Perro(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, edad, raza, peso)

class Gato(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, edad, raza, peso)
        
#main

perro = Perro("Brando", 3, "San Bernardo", 30)
gato = Gato("Roll", 4, "Persa", 3)

print(perro.descripcion())
print(perro.comer())
print(perro.caminar())
print(perro.dormir())
print(gato.descripcion())
print(gato.comer())
print(gato.dormir())
print(gato.dormir())
 
