class GestorTareas:
    def __init__(self,archivo_tareas="tareas.txt"):
        self.archivo_tareas = archivo_tareas
        
    def anadir_tareas(self,tarea):
        with  open( self.archivo_tareas,'a') as archivo:
            archivo.write(tarea + '\n')
        print("Tarea agregada con exito")  
    
    def mostrar_tareas(self):
        with open("files/ejericio/tareas.txt", "r") as file:
            tareas = file.readlines()
            for tarea in tareas:
                print(tarea.strip())
    
    def contar_tareas(self):
        with open("files/ejericio/tareas.txt", "r") as file:
            tareas = file.readlines()            
            print(f"Número total de tareas: {len(tareas)}")
            return len(tareas)
    
    def buscar_reemplazar_palabra(self, palabra_buscar, palabra_reemplazar):
        with open("files/ejericio/tareas.txt", "r") as file:
            tareas = file.readlines()
    
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
    
    def copiar_tareas_respaldo(self):
        with open("files/ejericio/tareas.txt", "r") as file_original:
            with open("files/ejericio/respaldo_tareas.txt", "w") as file_respaldo:
                file_respaldo.write(file_original.read())
        print("Copia de tareas realizada exitosamente en respaldo_tareas.txt")
            
    def mostrar_tareas_reemplazadas(self):
        with open("files/ejericio/tareas_reemplazadas.txt", "r") as file:
            tareas = file.readlines()
            for tarea in tareas:
                print(tarea.strip())
    
    
def main():
    gestor = GestorTareas()
    while True:
        print("Menú Inicial:")
        print("1. Añadir nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Contar el número de tareas")
        print("4. Buscar y reemplazar palabra en tareas")
        print("5. Mostrar tareas reemplazadas")
        print("6. Copiar tareas a un archivo de respaldo")
        print("7. Salir")
        
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == "1":
            tarea = input("Ingresa una nueva tarea")
            gestor.anadir_tareas(tarea)
            
        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            gestor.contar_tareas()
                        
        elif opcion == "4":
            palabra_buscar = input("ingrese la palabra a buscar")
            palabra_reemplazar=input("ingrese la palabra a reemplazar")
            gestor.buscar_reemplazar_palabra()
        elif opcion == "5":
            gestor.mostrar_tareas_reemplazadas()
        elif opcion == "6":            
            gestor.copiar_tareas_respaldo()
            
        elif opcion == "7":
            print("gracias por usar")
            break
        else:
            print("Opción no válida")

if __name__ == '__main__':
    main()