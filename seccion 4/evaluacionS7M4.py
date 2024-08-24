class SalarioError(Exception):
    def __init__(self, salario):
        self.salario = salario
        super().__init__(f"El salario {salario} no se encuentra en el rango de 1000 a 2000.")
         
def solicitar_salario():
    while True:
        try:
            salario = float(input("Ingrese su salario: "))
            validar_salario(salario)
            return salario
        except ValueError:
            print("Debe ingresar un número.")
        except SalarioError as e:
            print(e)

def validar_salario(salario):
    if salario < 1000 or salario > 2000:
        raise SalarioError(salario)

salario = solicitar_salario()


print(f"Salario ingresado: {salario}")
    

