#duck
#Vamos a pasar este codigo, usando herencia , usando atributos, usand property, usan polimorimifismo,  o inicializador

class Figuras:
    def calcular_perimetro():
        pass
class Cuadrado:
    def perimetro(self,lado):
        return lado * 4
class Pentagono:  
    def perimetro(self,lado):
        return lado * 5
class Exagono:  
    def perimetro(self,lado):
        return lado * 6   
class Octagono:
    def perimetro(self,lado): 
        return   lado * 8    
    
octagono = Octagono()
pentagono= Pentagono()
print(octagono.perimetro(5))
print(pentagono.perimetro(5))



