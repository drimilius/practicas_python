class Figuras:
    def __init__(self, lado):
        self._lado = lado
    
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, nuevo_lado):
        if nuevo_lado > 0:
            self._lado = nuevo_lado
        else:
            raise ValueError("El lado debe ser un número positivo")
    
    def calcular_perimetro(self):
        pass


class Cuadrado(Figuras):
    def calcular_perimetro(self):
        return self.lado * 4
    
class Pentagono(Figuras):
    def calcular_perimetro(self):
        return self.lado * 5
    
class Exagono(Figuras):
    def calcular_perimetro(self):
        return self.lado * 6
    
class Octagono(Figuras):
    def calcular_perimetro(self):
        return self.lado * 8


cuadrado = Cuadrado(4)
pentagono = Pentagono(5)
exagono = Exagono(6)
octagono = Octagono(8)

print(cuadrado.calcular_perimetro())
print(pentagono.calcular_perimetro())
print(octagono.calcular_perimetro())
print(exagono.calcular_perimetro())

