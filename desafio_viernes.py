""" 
Proyecto Práctico en Python: "Gestión de una Biblioteca Digital"
Descripción:
En este proyecto, los alumnos desarrollarán un programa para gestionar una biblioteca digital. El programa permitirá agregar, buscar, y listar libros. Además, contará con funcionalidades para llevar un registro de los libros prestados y devueltos. El proyecto integrará varios conceptos clave como if, for, while, funciones, estructuras de datos (listas y diccionarios), sentencias condicionales, control de flujo y operadores lógicos.
Objetivos:
Aplicar estructuras de control de flujo (if, for, while).
Definir y utilizar funciones.
Manipular estructuras de datos como listas y diccionarios.
Implementar operadores lógicos para la toma de decisiones.
Instrucciones:
Crear el Menú Principal:
El programa debe mostrar un menú con las siguientes opciones:
Agregar un libro.
Buscar un libro.
Listar todos los libros.
Registrar un préstamo.
Registrar una devolución.
Salir.
Agregar un Libro:
Solicitar al usuario ingresar el título del libro, autor, y el año de publicación.
Almacenar la información en una lista de diccionarios.
Cada libro debe ser representado como un diccionario con las claves: titulo, autor, año, y prestado (inicialmente  False).
Buscar un Libro:
Permitir buscar un libro por título.
Utilizar un bucle for para recorrer la lista de libros y encontrar coincidencias.
Mostrar los detalles del libro si se encuentra, o un mensaje indicando que no existe.
Listar Todos los Libros:
Recorrer la lista de libros utilizando un bucle for.
Mostrar el título, autor, año de publicación y si está prestado o disponible.
Registrar un Préstamo:
Solicitar el título del libro que se desea prestar.
Verificar si el libro está disponible (prestado == False).
Si está disponible, marcarlo como prestado (prestado = True).
Si no está disponible, mostrar un mensaje indicando que ya está prestado.
Registrar una Devolución:
Solicitar el título del libro que se desea devolver.
Verificar si el libro está prestado (prestado == True).
Si está prestado, marcarlo como disponible (prestado = False).
Si no está prestado, mostrar un mensaje indicando que no se encontraba prestado.
Salir:
Terminar la ejecución del programa cuando el usuario selecciona la opción de salida.
Extensiones Sugeridas:
Agregar un sistema de usuarios: Crear una lista de usuarios que puedan prestar libros.
Implementar un límite de préstamos: Establecer un máximo de libros que un usuario puede prestar a la vez.
Historial de préstamos: Registrar y mostrar un historial de los libros prestados y devueltos por cada usuario.
"""


# Crear la lista de libros
libros = []
def agregar_libro():
    Titulo_libro = input("Ingrese el titulo del libro: ")
    Autor= input("ingrese el nombre del autor: ")
    Fecha = input("Ingrese la fecha de publicacion (dd/mm/yyyy): ")
    libro= {"Titulo":Titulo_libro, "Autor":Autor, "Fecha":Fecha}
    libros.append(libro)
    print(f"Libro '{Titulo_libro}' agregado con éxito")

def buscar_libro():
    titulo_busqueda = input("Ingrese el titulo del libro que desea buscar: ")
    for libro in libros:
        if libro["Titulo"].lower()== titulo_busqueda.lower():
            print(f"Libro encontrado:\nNombre: {libro["Titulo"]},\nAutor: {libro["Autor"]},\nFecha: {libro["Fecha"]}")
            break
        else:
            print("Libro no encontrado")    
       
def registrar_prestamos():
    titulo_prestamo = input("ingrese el titulo del libro que desea;" )
    for libro in libros:
        if libro["Titulo"].lower()== titulo_prestamo.lower():
            nombre_usuario = input("ingrese nombre del usuario: ")
            fecha_prestamo =input("ingrese fecha de prestamo (dd/mm/yyyy): ")
            prestamo.append({"titulo": libro["Titulo"], "usuario": nombre_usuario, "fechaPrestamo":fecha_prestamo})
            print (f"prestamo registrado: {libro["Titulo"]} prestado a {nombre_usuario} el {fecha_prestamo}")
            break
    else:
        print("Libro no encontrado")    
    


def registrar_devoluciones():
    titulo_devolucion = input("ingrese el titulo del libro a devolucion:")
    for prestamo in prestamos:
        if prestamo["Titulo"].lower()== titulo_devolucion.lower():
            prestamos.remove(prestamo)
            print(f"Devolucion registrada: {titulo_devolucion} devuelto por {prestamo['usuario']}")
            break
    else:
        print("Libro no encontrado en el historial de prestamos")           
    
def historial_prestamos():
    if prestamos:
        print("historial de prestamos.")
        for prestamos in prestamos:
            print(f"Titulo: {prestamo['Titulo']}, Usuario: {prestamo['usuario']}, Fecha: {prestamo['fechaPrestamo']}")
    else:
        print("No hay historial de prestamos")
        
    
    
    
def mostrar_menu():
    print("Menú Principal")
    print("1. agregar un libro")
    print("2. buscar un libro")
    print("3. registrar prestamo")
    print("4. registrar devolucion")
    print("5. historial de prestamos")
    print("6. Salir")

def menu(): # menu estudiante
    while True:
        
        mostrar_menu()
        opcion=int(input("ingrese la opcion deseada:"))
        if opcion==1:
            agregar_libro()
            print("Libro agregado a la Biblioteca")
        elif opcion==2:
            buscar_libro()
        elif opcion==3:
            registrar_prestamos()             
        elif opcion==4:
            registrar_devoluciones
            break
        elif opcion==5:
            historial_prestamos()
        elif opcion==6:
            print("gracias por usar nuestro sistema")
            break
        else:
            print("opcion no valida")      

#main

menu()