class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def Movimiento(self):
        print (f"{self.nombre} esta caminando")

#subclase Maratonista        
class Maratonista(Persona):
    def Movimiento(self):
        print (f"{self.nombre} esta trotando")
        

#subclase Ciclista

class Ciclista(Persona):
    def Movimiento(self):
        print (f"{self.nombre} esta rodando")


#instancias
persona = Persona("Ivan")
maratonista = Maratonista("Carlos")
ciclista = Ciclista("Ana")

print (persona.Movimiento())
print (maratonista.Movimiento())
print (ciclista.Movimiento())