#ducktyping
class Pato:
    def volar(self):
        print("el pato vuela")
    def nadar(self):
        print("el pato nada")
class Persona:
    def volar(self):
        print("la persona puede volar en avion")
    def nadar(self):
        print("la persona nada en la piscina")
class Pez:
    def volar(self):
        print("el pez vuela cuando salta")
    def nadar(self):
        print("el pez nada en el mar")        
def hacer_volar_y_nadar(objeto):
    objeto.volar()
    objeto.nadar()
    
lucas = Pato()
roberto = Persona()
nemo= Pez()

hacer_volar_y_nadar(lucas)
hacer_volar_y_nadar(roberto)
hacer_volar_y_nadar(nemo)

