# metodos
def sumar(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a/b
def solicitar_numeros(a,b,resultados):
    num1 = float(input(f"Ingrese el primer numero de {a} y {b}: "))
    num2 = float(input(f"Ingrese el segundo numero de {a} y {b}: "))
    resultados.append(sumar(num1, num2))
    resultados.append(resta(num1, num2))
    resultados.append(multiplicar(num1, num2))
    resultados.append(dividir(num1, num2))
    return num1, num2
def calculadora ():
    print("---------bienvenido a la calculadora--------")
    while True:
        print("\nseleccione una operacion")
        print("1.sumar")
        print("2.resta")
        print("3.multiplicar")
        print("4.dividir")
        print("5.salir")
        opcion = input("ingresa tu opcion del (1-5)") #opcion = int(input("ingresa tu opcion del (1-5)"))
        # main
###
###        if opcion == "1":
###            num1 = float(input("Ingrese el primer numero: "))
###            num2 = float(input("Ingrese el segundo numero: "))
###            resultado = sumar(num1, num2)
###            print(f"el resultado de la suma de {num1} y {num2} es: {resultado}")
###        elif opcion == "2":
###            num1 = float(input("Ingrese el primer numero: "))
###            num2 = float(input("Ingrese el segundo numero: "))
###            resultado = resta(num1, num2)
###            print(f"el resultado de la resta de {num1} y {num2} es: {resultado}")
###        elif opcion == "3":
###            num1 = float(input("Ingrese el primer numero: "))
###            num2 = float(input("Ingrese el segundo numero: "))
###            resultado = multiplicar(num1, num2)
###            print(f"el resultado de la multiplicacion de {num1} y {num2} es: {resultado}")
###        elif opcion == "4":
###            num1 = float(input("Ingrese el primer numero: "))
###            num2 = float(input("Ingrese el segundo numero: "))
###            resultado = dividir(num1, num2)
###            print(f"el resultado de la division de {num1} y {num2} es: {resultado}")
###        elif opcion == "5":
###            print("hasta la proxima")
###            break
###        else:
###            print("Opcion invalida, intente nuevamente")

# main calculadora()

 
        resultados = []
        if opcion in ["1", "2", "3", "4"]:
            num1, num2 = solicitar_numeros("a", "b", resultados)
            if opcion == "1":
                print(f"El resultado de la suma de {num1} y {num2} es: {resultados[0]}")
            elif opcion == "2":
                print(f"El resultado de la resta de {num1} y {num2} es: {resultados[1]}")
            elif opcion == "3":
                print(f"El resultado de la multiplicacion de {num1} y {num2} es: {resultados[2]}")
            elif opcion == "4":
                print(f"El resultado de la division de {num1} y {num2} es: {resultados[3]}")
        elif opcion == "5":
            print("hasta la proxima")
            break
        else:
            print("Opcion invalida, intente nuevamente")

calculadora()