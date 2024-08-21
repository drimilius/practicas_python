# Reto Completo: Gestor de Tareas con Archivos
# Descripción:
# Crea un programa en Python que gestione una lista de tareas utilizando archivos. El programa permitirá al usuario realizar las siguientes operaciones:
# 1.	Añadir nuevas tareas.
# 2.	Mostrar todas las tareas guardadas.
# 3.	Contar cuántas tareas hay en total.
# 4.	Buscar y reemplazar una palabra en todas las tareas.
# 5.	Copiar las tareas a un nuevo archivo de respaldo.
# Instrucciones:
# 1.	Añadir Tareas:
# -	El programa pedirá al usuario que ingrese una nueva tarea.
# -	Si el usuario escribe "salir", el programa dejará de pedir tareas.
# -	Cada tarea se guardará en un archivo de texto llamado tareas.txt.
# 2.	Mostrar Tareas:
# -	El programa leerá y mostrará todas las tareas guardadas en tareas.txt, una por línea.
# 3.	Contar Tareas:
# -	El programa contará cuántas líneas (tareas) hay en el archivo tareas.txt y mostrará el número total.
# 4.	Buscar y Reemplazar:
# o	El programa pedirá al usuario una palabra a buscar y otra con la que reemplazarla.
# o	Buscará la palabra en todas las tareas y la reemplazará.
# o	Guardará las tareas modificadas en un archivo llamado tareas_modificadas.txt.
# 5.	Copiar Tareas:
# -	El programa copiará el contenido de tareas.txt a un nuevo archivo llamado respaldo_tareas.txt.
# Pistas:
# •	Usa funciones para organizar el código, cada operación puede ser una función diferente.
# •	Maneja las excepciones para asegurarte de que el programa no falle si el archivo no existe o si ocurre algún otro error.
# •	Recuerda cerrar los archivos después de leer o escribir para evitar problemas de acceso a archivos.
# Ejemplo de Flujo del Programa:
# 1.	Menú Inicial:
# 1. Añadir nueva tarea
# 2. Mostrar todas las tareas
# 3. Contar el número de tareas
# 4. Buscar y reemplazar palabra en tareas
# 5. Copiar tareas a un archivo de respaldo
# 6. Salir


def añadir_tarea():
    with open("files/ejericio/tareas.txt", "a") as file:
        while True:
            tarea = input("Ingrese una nueva tarea (o 'salir' para terminar): ")
            if tarea.lower() == "salir":
                break
            file.write(f"{tarea}\n")
        print("Tareas añadidas exitosamente")

def mostrar_tareas():
    try:
        with open("files/ejericio/tareas.txt", "r") as file:
            tareas = file.readlines()
            for tarea in tareas:
                print(tarea.strip())
    except FileNotFoundError:
        print("El archivo tareas.txt no existe")

def contar_tareas():
    try:
        with open("files/ejericio/tareas.txt", "r") as file:
            tareas = file.readlines()            
            print(f"Número total de tareas: {len(tareas)}")
            return len(tareas)
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return 0
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return 0


def buscar_reemplazar():
    try:
        with open("files/ejericio/tareas.txt", "r") as file:
            tareas = file.readlines()
    
        palabra_buscar = input("ingrese la palabra a buscar:")
        palabra_reemplazar = input("ingrese la palabra con la que reemplazarla:")
        
        palabra_encontrada = False
    
        with open("files/ejericio/tareas_modificadas.txt", "w") as file_modificadas:
            for tarea in tareas:
                if palabra_buscar in tarea:
                    palabra_encontrada = True
                tarea_modificada = tarea.replace(palabra_buscar, palabra_reemplazar)
                file_modificadas.write(tarea_modificada)
        if palabra_encontrada:
            print("Palabra reemplazada y tareas guardadas en tareas_modificadas.txt")
        else:
            print("La palabra no se encontró en las tareas")
    except FileNotFoundError:
        print("No se encuentra el archivo tareas.txt")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
def copiar_tarea():
    try:
        with open("files/ejericio/tareas.txt", "r") as file_original:
            with open("files/ejericio/respaldo_tareas.txt", "w") as file_respaldo:
                file_respaldo.write(file_original.read())
        print("Copia de tareas realizada exitosamente en respaldo_tareas.txt")
    except FileNotFoundError:
        print("No se encuentra el archivo tareas.txt")

def menu():
    while True:
        print("Menú Inicial:")
        print("1. Añadir nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Contar el número de tareas")
        print("4. Buscar y reemplazar palabra en tareas")
        print("5. Mostrar tareas reemplazadas")
        print("5. Copiar tareas a un archivo de respaldo")
        print("6. Salir")
        
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "1":
            añadir_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            contar_tareas()
        elif opcion == "4":
            buscar_reemplazar()
        elif opcion == "6":
            copiar_tarea()
        elif opcion == "7":
            print("gracias por usar")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
