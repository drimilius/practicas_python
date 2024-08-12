#solicitar numero
numero = int(input("ingrese el numero "))


#evaluacion del numero 
if numero > 0:
    print("El numero es positivo")
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
elif numero < 0:
    print("El numero es negativo")
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("El numero es cero")
    
    