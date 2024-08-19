from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def comer(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "Woof!"
    
    def comer(self):
        return "Comiendo Carne"

class Cat(Animal):
    def sound(self):
        return "Meow!"
    
    def comer(self):
        return "Comiendo pescado"

class Cerdo(Animal):
    def sound(self):
        return "oing!"
    def comer(self):
        return "Comiendo"

#main
perro = Dog()
gato = Cat()
cerdo = Cerdo()

print (gato.sound())
print (perro.sound())
print (cerdo.comer())

