#resultados
resultados = [] 

#funciones
def sumar(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "no se puede dividir por 0"
    
#calcular
def calular(a,b):
    suma = sumar(a,b)
    resta = restar(a,b)
    multiplicacion = multiplicar(a,b)
    division = dividir(a,b)
    return (suma, resta,multiplicacion, division)

#resultados
def agregar_resultados(a,b):
    suma, resta, multiplicar, division = calular(a,b)
    resultados_dicc = {
        "suma": suma,
        "resta": resta,
        "multiplicacion": multiplicar,
        "division": division
    }
    resultados.append(resultados_dicc)
    print("resultados agregados")
    
#mostrar resultados

def mostrar_resultados():
    if not resultados:
        print("no hay resultados agregados")
    else:
        for resultado in resultados:
            print(f"suma: {resultado['suma']}, resta: {resultado['resta']}, multiplicacion: {resultado['multiplicacion']}, division: {resultado['division']}")

#ingresar numeros
def ingresar_numeros():
    a = float(input("ingrese el primer numero: "))
    b = float(input("ingrese el segundo numero: "))
    return a, b

#menu
def menu():
    print("bienvenido")
    print("ingrese una opcion:")
    print("1. agregar resultados")
    print("2. mostrar resultados")
    print("3. salir")
    

def menu_operaciones():
    while True:
        menu()
        opcion = int(input("ingrese la opcion deseada: "))
        if opcion == 1:
            a, b = ingresar_numeros()
            agregar_resultados(a, b)
        elif opcion == 2:
            mostrar_resultados()
        elif opcion == 3:
            break
        else:
            print("opcion invalida")

menu_operaciones()