class Animal:
    def __init__(self):
        self.patas = 4
   
    def hacer_sonido(self):
        return "Grrr!"
    def comer(self):
        return "Esta comiendo"
    
class Perro(Animal):  
    def __init__(self):
      super().__init__()
      self.patas = 4    
      
    def hacer_sonido(self):
        return "Gua!"
class Canguro(Animal):
      def __init__(self):
        super().__init__()
        self.patas = 2
      
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!Miau!"
    def salta(self):
        return "Salta muy alto"
         
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu!"
    def comer(self):
        return "Comiendo Pasto"
       
def animal_sonido(animal):
    print(animal.hacer_sonido())
def animal_comiendo(animal):
    print(animal.comer())   
    
perro =Perro
gato = Gato
vaca = Vaca
canguro=Canguro
 
print(gato.salta)
print(perro.patas)
print(canguro.patas)
# print(perro.name)
# animal_sonido(perro)
# animal_sonido(gato)
# animal_sonido(vaca)
animales = [Perro(),Gato(),Vaca(),Perro(),Vaca()]
for animal in animales:
    animal_sonido(animal)
    animal_comiendo(animal)