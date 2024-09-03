# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Inicializar la variable que almacenará el factorial
factorial = 1

# Calcular el factorial utilizando un bucle for
for i in range(1, numero + 1):
    factorial *= i

# Imprimir el resultado
print(f"El factorial de {numero} es: {factorial}")
