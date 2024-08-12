class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def describir(self):
        return f"Este coche es de marca {self.marca}, \nmodelo {self.modelo},\nfue fabricado en el año {self.año}"
    def arrancar(self):
        return f"el {self.marca}, {self.modelo},esta arrancando"

    
class Moto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def mostrar_detalle(self):
        return f"Esta moto es de marca {self.marca}, \nmodelo {self.modelo},\nfue fabricada en el año {self.año}"
    def prender(self):
        return f"la {self.marca}, {self.modelo},esta prendida"

mi_moto = Moto("Honda", "CBR", "2020")
mi_moto2 = Moto("TRK", "502", "2021")
mi_coche = Coche("Toyota", "yaris", "2017")

print (mi_moto.mostrar_detalle())
print (mi_moto2.mostrar_detalle())     
print(mi_coche.describir())
print(mi_coche.arrancar())       