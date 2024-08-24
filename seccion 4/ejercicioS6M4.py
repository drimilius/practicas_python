suma = 3000
contador = 0

try:
    resultado = suma / contador
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Division por cero")
    
    