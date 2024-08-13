class cuadrilatero:
    def __init__(self, lados):
        self.lados = lados
        self.suma_angulos = 360
    def perimetro(self):
        return sum(self.lados)

class cuadrado(cuadrilatero):
    def __init__(self, lados):
        super().__init__(lados)
        
cuadrado1 = cuadrado([4, 4, 4, 4])
perimetro1 = cuadrado.perimetro()
print=(perimetro1)
print=(cuadrado1.suma_angulos)




