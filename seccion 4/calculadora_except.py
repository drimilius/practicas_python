"""def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Debes ingresar un número.")
#main
num1 = solicitar_numero("introduce el primer numero")
num2 = solicitar_numero("introduce el segundo numero")

"""
def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Debes ingresar un número.")
def realizar_operacion(a,b,operador):
    try:
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            return a / b
        else:
            raise ValueError("Operador no válido.")
        
    except ValueError as e:
        print(e)
        return None
#main
num1 = solicitar_numero("introduce el primer numero")
num2 = solicitar_numero("introduce el segundo numero")

operacion = input("introduce el operador a usar (+,-,*, /):")
resultado = realizar_operacion(num1,num2,operacion)
print(f"el resultado de {num1}{operacion}{num2} es: {resultado}")