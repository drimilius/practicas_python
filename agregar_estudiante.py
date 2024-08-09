# Crea un programa en Python que gestione la información de los estudiantes de una escuela.
# El programa debe permitir
    # agregar nuevos estudiantes,
    # mostrar la lista de estudiantes
    #buscar un estudiante por su nombre.
    
# Requisitos
# Funciones:
# agregar_estudiante(nombre, edad, grado): Agrega un nuevo estudiante a la lista.
# mostrar_estudiantes(): Muestra la lista completa de estudiantes.
# buscar_estudiante(nombre): Busca un estudiante por su nombre y muestra su información.
 
# Interacción con el Usuario:
# El programa debe mostrar un menú con las opciones:
    # "Agregar estudiante",
    # "Mostrar estudiantes",
    # "Buscar estudiante" y
    # "Salir".
    
# La opción "Agregar estudiante"
    #   debe pedir el nombre,
    #   edad
    #    grado del estudiante.
 
# La opción "Mostrar estudiantes"
#   debe mostrar la lista completa de estudiantes.
# La opción "Buscar estudiante"
#   debe pedir el nombre del estudiante y mostrar su información si se encuentra en la lista.

#metodos
estudiantes = []

def agregar_estudiante(nombre, edad, grado):
    estudiante={"nombre":nombre, "edad":edad, "grado":grado}
    estudiantes.append(estudiante)
def mostrar_estudiantes(): # es la opción mostrar estudiantes
    if not estudiantes:  #es la opc1ion mostrar si no hay estudiantes
        print("No hay estudiantes agregados.")
    else:
        for estudiante in estudiantes:
            print(f"El Nombre del estudiante es: {estudiante['nombre']}, su edad es: {estudiante['edad']}, su grado es: {estudiante['grado']}")


def buscar_estudiante(nombre): # es la opción buscar estudiante
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"Estudiante encontrado sus datos son:\nNombre: {estudiante['nombre']},\nEdad: {estudiante['edad']},\nGrado: {estudiante['grado']}")
        break
    else: 
        print("El estudiante no se encuentra en la lista.")

def pedir_info_alumno():
    nombre=input("ingrese el nombre del estudiante:")
    edad=int(input("ingrese la edad del estudiante:"))
    grado=int(input("ingrese el grado del estudiante:"))
    return nombre, edad, grado
def mostrar_menu():
    print("bienvenido a Gestion de Estudiantes 0077****")
    print("seleccione una opción:")
    print("1.agregar estudiante")
    print("2.Mostrar estudiantes")
    print("3.Buscar estudiante")
    print("4.Salir") 


def menu_estudiant(): # menu estudiante
    while True:
        
        mostrar_menu()
        opcion=int(input("ingrese la opcion deseada:"))
        if opcion==1:
            nombre, edad, grado= pedir_info_alumno()
            agregar_estudiante(nombre, edad, grado)
            print("Estudiante agregado correctamente.")
        elif opcion==2:
            mostrar_estudiantes()
        elif opcion==3:
            nombre=input("ingrese el nombre del estudiante a buscar:")
            buscar_estudiante(nombre) 
        elif opcion==4:
            print("Gracias por usar Gestion de Estudiantes 0077****")
            break
        else:
            print("opcion no valida")                 

#main
menu_estudiant()
