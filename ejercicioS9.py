#basado en agregar_estudiantes.py
rectangulos=[]

def agregar_rectangulo(base, altura):
    if base > 0 and altura > 0:
        rectangulo={"base": base, "altura": altura, "area": base * altura}
        rectangulos.append(rectangulo)
        print("rectangulo agregado")
    else:
        print("la base y la altura deben ser numeros positivos")

def mostrar_rectangulos():
    if not rectangulos:
        print("No hay rectangulos agregados")
    else:
        for rectangulo in rectangulos:
            print(f"Base: {rectangulo['base']}, Altura: {rectangulo['altura']}, Area: {rectangulo['area']}")

def pedir_info():
    base=float(input("Ingrese la base del rectangulo: "))
    altura=float(input("Ingrese la altura del rectangulo: "))
    return base, altura

def menu():
    print("bienvenido a gestion de Rectangulos")
    print("seleccione una opcion:")
    print("1. agregar rectangulo")
    print("2. Mostrar rectangulo")
    print("3. salir")
    
def main():
    while True:
        menu()
        opcion=int(input("ingrese la opcion deseada:"))
        if opcion==1:
            base, altura=pedir_info()
            agregar_rectangulo(base, altura)
        elif opcion==2:
            mostrar_rectangulos()
        elif opcion==3:
            break
        else:
            print("opcion invalida")

#main
main()
    

