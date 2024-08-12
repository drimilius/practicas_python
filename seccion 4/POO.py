""" #clase

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} está ladrando."
    
#todo: create instance of the class
book1 = Book()

#todo: print the class and property

#todo: create a basic class
class Book:
    def __init__(self, title):
        self.title = title

#todo: create instance of the class


"""
#class libro
class Book:
    #pass #para declarar que una clase no haga nada
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        
#class periodico
class NewsPaper:
    def __init__(self, title):
        self.title = title
#class revista        
class Revista:
    def __init__(self, title):
        self.title = title
#class folleto
class Folleto:
    def __init__(self, title):
        self.title = title
        
#main
book1= Book("100 años de soledad", "Garcia Marquez")
book2= Book("Codigo limpio", "Robert C. Martin")
periodico= NewsPaper("El Universal")
periodico2= NewsPaper("Times")
revista= Revista("Ciencia y Desarrollo")
folleto= Folleto("Python")

#invocando objetos de la clase book
print(book1)
print(book2)
print(book2.title)
print(book1.autor)
print(book2.autor)

#invocando objeto de la clase NewsPaper

print(periodico.title)
print(periodico2.title)

#invocando objeto de clase Revista
print(revista.title)

#invocando objeto de clase Folleto
print(folleto.title)

#metodos

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #metodo
    def ladrar(self):
        print (f"{self.nombre} ladra fuerte y tiene {self.edad} años")
    #metodo
    def salir_a_pasear(self):
        print(f"{self.nombre} saldrá a pasear")
    
    #metodo
    def comer(self):
        print(f"{self.nombre} come comida")

#invocando objeto clase Perro        
perro1=Perro("Buddy", 3)
perro2=Perro("Lazaron", 4)
perro1.ladrar() #invoca al metodo
perro1.salir_a_pasear() #invoca al metodo
perro2.salir_a_pasear()
perro1.comer()
perro2.comer()





