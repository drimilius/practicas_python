class MiExcepcion(Exception):
    def __init__(self, message):
        super().__init__(message)


        
def solicitar_edad():
    while True:
        try:
            edad = int(input("ingrese su edad: "))
            validar_edad(edad)
            return edad
        
        except ValueError:
            print("Error: debe ingresar un numero entero. intente nuevamente")
        
        except MiExcepcion as e:
            print(e)
            
def validar_edad(edad):
    if edad < 0:
        raise MiExcepcion("La edad no puede ser negativa. intente nuevamente")
    elif edad < 18:
        raise MiExcepcion("La edad debe ser mayor a 18")

edad = solicitar_edad()

if edad >=18:
    print("Usted es Adulto")
else:
    print("No es un adulto.")


