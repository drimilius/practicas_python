def reemplazar_texto():
    reemplazos = 0

    try:
        with open("seccion 4/evaluacionS9M4/informacion.dat", "r", encoding="utf-8") as file:
            lineas = file.readlines()
            
        with open("seccion 4/ejercicioS9M4/informacion.dat", "w", encoding="utf-8") as file:
            for linea in lineas:
                conteo_reemplazos = linea.lower().count("informacion")
                if conteo_reemplazos > 0:
                    reemplazos += conteo_reemplazos
                    linea = linea.replace("informacion", "Procesamiento")
                file.write(linea)

        print(f"Se realizaron: {reemplazos} reemplazos")
        
    except FileNotFoundError as error:
        print(f"El archivo no fue encontrado: {error}")
        
reemplazar_texto()

