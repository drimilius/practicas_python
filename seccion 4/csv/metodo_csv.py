#leer un archivo

import csv

with open("seccion 4/csv/Libro1.csv", mode = "r", newline="") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)
        
with open("seccion 4/csv/people2.csv", mode="w", newline="") as file:
    escritor_csv = csv.writer(file)
    escritor_csv.writerow(["nombre", "apellido", "ciudad"])
    escritor_csv.writerow(["Juan", "Perez", "Osorno"])
    escritor_csv.writerow(["Maria", "Garcia", "Antofagasta"])
    escritor_csv.writerow(["Pedro", "Lopez", "Temuco"])
    
#agregar un registro a un archivo csv

with open("seccion 4/csv/people.csv", mode="w", newline="") as f:
    escritor_csv = csv.writer(f)
    escritor_csv.writerow(["Cristian", "Castillo", "Concepcion"])

