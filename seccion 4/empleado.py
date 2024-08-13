class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre #publico
        self._departamento = None #protegido
        self.__salario = salario #privado

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario no puede ser negativo.")
            
    def _asignar_departamento(self, departamento):
        self.departamento = departamento
    
    def _calcular_bonus(self):
        return self.__salario * 0.1

#main
Empleado = Empleado("roberto", 200)
print(Empleado.nombre) #acceso directo a un atributo publico
Empleado.salario2= 550 #uso de setter
print(Empleado.salario) #uso de getter
Empleado._asignar_departamento("Ventas") #uso de metodo protegido

print(Empleado.__salario)
Empleado._calcular_bonus()




