try:
    with open("seccion 4/ejercicioS9M4/informacion.dat", "r") as file:
        lineas = file.readlines()
        
    with open("seccion 4/ejercicioS9M4/informacion.dat", "w",) as file:
        for linea in lineas:
            file.write(linea)
            if "Datos de información en la línea 5." in linea:               
                file.write("Hola Mundo\n")
                file.write("Este es una nueva línea en el archivo\n")
                file.write("agregando la segunda línea del archivo\n")
                file.write("finalizando la línea agregada\n")
except FileNotFoundError as error:
    print(f"El archivo no fue encontrado: {error}")
finally:
    print("El proceso ha finalizado.")