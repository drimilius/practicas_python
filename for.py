frutas = ["manzana", "pera", "uva"]
print(frutas)
for fr in frutas:
    print(f"el nombre de la fruta es :{frutas}")

# ejemplo en diccionario
# estudiantes = {"ana": 25, "juan": 30, "pedro": 28}
# for nombre, edad in estudiantes:
#    print(nombre)

# recorriendo una palabra
palabra = "python"
for letra in palabra:
    print(letra.upper())

palabra = "python"
for letra in palabra:
    print(f"esta es una letra de la palabra:{letra.upper()}")

# recorriendo un diccionario
estudiante = {"matias": 10, "Roberto": 7, "axel": 9}
for nombre in estudiante:
    print(nombre)

    print(f"la calificacion de {nombre} es: {estudiante[nombre]}")
    for nombre, calificacion in estudiante.items():
        print(f"{nombre} tiene una calificacion de: {calificacion}")

# recorriendo numeros
numeros = [23, 24, 37, 45, 54]
suma = 0
for numero in numeros:
    suma += numero  # suma=numero + suma
    print(f"la suma de los numeros es: {suma}")
media = suma / len(numeros)
print(f"la mediana de los numeros es: {media}")
mediana = suma / len(numeros)
print(f"la mediana de los numeros es: {mediana}")
moda = suma / len(numeros)
print(f"la mediana de los es {moda}")
# sumar valores de un diccionario
ventas = {"enero": 1000, "febrero": 1500, "marzo": 2000}
total_ventas = 0
for mes, cantidad in ventas.items():
    total_ventas += cantidad  # totalventas= cantidad + total_ventas
    print(f"El total de ventas en {mes} es: {total_ventas}")

# agrega numeros a la variable pares que se encuentra vacia
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pares = []
for numbers in numbers:
    if numbers % 2 == 0:
        pares.append(numbers)
print(f"Los numeros pares son: {pares}")

nums = [10, 20, 30, 5, 50, 20]
for num in nums:
    if num <= 0:
        print(f"El numero {num} es negativo o cero")
        break
    else:
        print("todo los numeros son positivos")
