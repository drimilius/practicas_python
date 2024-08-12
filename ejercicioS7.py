#lista de numeros
numeros = [12, 0, 3, 1, 0, 19, 22, 7, 9, 4]

#recorrer la lista
for numero in numeros:
    if numero == 0:
        print(f"{numero} es cero.")
    elif numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")
        