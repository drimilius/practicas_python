try:
    with open("seccion 4/evaluacionS8M4/informacion.dat","x") as file:
        file.write("Datos de información en la línea 1.\n")
        file.write("Datos de información en la línea 2.\n")
        file.write("Datos de información en la línea 3.\n")
        file.write("Datos de información en la línea 4.\n")
        file.write("Datos de información en la línea 5.\n")
except FileExistsError:
    print("El archivo ya existe, ha sido creado previamente")
    

#manejo de errores
with open("seccion 4/evaluacionS8M4/informacion.dat","r") as file:
    try:
        contenido = file.read()
        print(contenido)
    except FileNotFoundError:
        print("No se encuentra este archivo.") 
    except IOError as e:
        print("el archivo no se encuentra")