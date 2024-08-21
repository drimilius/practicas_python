import csv
with open("files/ejericio/csv/alumnos.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        print(fila)

#escribir un archivo csv

datos = [["nombre", "edad",], ["edgar", 34], ["Gonzalo", 33]]
with open("files/ejericio/csv/nuevo_datos.csv", "w", newline="") as archivo_csv:
    escribir = csv.writer(archivo_csv)
    for fila in datos:
        escribir.writerow(fila)
        