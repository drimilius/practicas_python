class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
    
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_sexo(self):
        return self.sexo

    def get_edad(self):
        return self.edad

    def get_estatura(self):
        return self.estatura

    def get_peso(self):
        return self.peso

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_edad(self, edad):
        self.edad = edad

    def set_estatura(self, estatura):
        self.estatura = estatura

    def set_peso(self, peso):
        self.peso = peso

persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)
print(f"Persona 1: Nombre: {persona_1.get_nombre()}, Apellido: {persona_1.get_apellido()}, Edad: {persona_1.get_edad()} años, Estatura: {persona_1.get_estatura()} mts, Peso: {persona_1.get_peso()} Kg")
print(f"Persona 2: Nombre: {persona_2.get_nombre()}, Apellido: {persona_2.get_apellido()}, Edad: {persona_2.get_edad()} años, Estatura: {persona_2.get_estatura()} mts, Peso: {persona_2.get_peso()} Kg")



persona_1.set_edad(21)
persona_2.set_apellido("Santiago")

print(f"Actualizacion: Nombre: {persona_1.get_nombre()}, Apellido: {persona_1.get_apellido()}, Edad: {persona_1.get_edad()} años, Estatura: {persona_1.get_estatura()} mts, Peso: {persona_1.get_peso()} Kg")
print(f"Actualizacion: Nombre: {persona_2.get_nombre()}, Apellido: {persona_2.get_apellido()}, Edad: {persona_2.get_edad()} años, Estatura: {persona_2.get_estatura()} mts, Peso: {persona_2.get_peso()} Kg")
