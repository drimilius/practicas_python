#copiar el contenido de un archivo a otro
def copiar_archivo(archivo_origen, archivo_destino):
    try:
        #abrimos el archivo origen en modo lectura
        with open(archivo_origen, 'r') as origen:
            contenido = origen.read() #leemos el contenido origen
        
        #abrimos el archivo destino en modo escritura
        with open(archivo_destino, 'w') as destino:
            destino.write(contenido) #escribimos el contenido al archivo destino
    except FileNotFoundError:
        print(f"El archivo {archivo_origen} no fue encontrado.")
        
        
#contar palabras de un archivo
def contar_palabra(archivo):
    try:
        with open(archivo,"r") as origen:
            contenido = origen.read()
            palabras = contenido.split()
            print(f"el archivo {archivo} contiene {len(palabras)} palabras")       
                
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
            
def reemplazar_palabra(archivo_origen, palabra_buscar, palabra_remplazo, archivo_destino):
    try:
        
       with open(archivo_origen,"r") as origen:
           contenido = origen.read()
           
           #reemplazar palabra
           contenido_modificado = contenido.replace(palabra_buscar,palabra_remplazo)
           with open(archivo_destino, "w") as destino:
               destino.write(contenido_modificado)
               print("Palabra Cambiada")
               
    except FileNotFoundError:
        print(f"El archivo {archivo_origen} no fue encontrado.")            


#main
copiar_archivo("files/ejemplo.txt", "files/ejemplo2.txt")
contar_palabra("files/ejemplo.txt")    