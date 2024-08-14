class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "guau"
class Gato(Animal):
    def hacer_sonido(self):
        return "miau"
class Vaca(Animal):
    def hacer_sonido(self):
        return "mu"

def animal_sonido(animal):
    print(animal.hacer_sonido())

perro = Perro()
gato = Gato()    
vaca = Vaca()
animal_sonido(perro)   
animal_sonido(gato)
animal_sonido(vaca)

animales = [Perro(), Gato(), Vaca(), Perro(), Vaca()]
for animal in animales:
    animal_sonido(animal)



