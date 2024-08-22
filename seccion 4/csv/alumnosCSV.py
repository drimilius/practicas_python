import csv
def escribir_csv(filename, datos):
    with open(filename, mode="W", newline="") as file:
        escritor_csv=csv.writer(file)
        escritor_csv.writerow(["nombre", "apellido", "ciudad"])
        for fila in datos:
            escritor_csv.writerow(fila)
        print ("archivo creado con exito")
    
def leer_csv(filename):
    with open(filename, mode="r") as file:
        lector_csv=csv.reader(file)
        next(lector_csv)  # ignorar la primera fila (cabecera)
        for fila in lector_csv:
            print(fila)
            
def agregar_csv(filename, registro):
    with open(filename, mode="a", newline="") as file:
        escritor_csv=csv.writer(file)
        escritor_csv.writerow(registro)
        
datos_iniciales = [["Moises", "Barrera", ""], ["Edgar", "Carrion", ""] ["Cristopher", "Sanchez", "Santiago"]]
nombre_archivo = "seccion 4/csv/estudent.csv"
escribir_csv = (nombre_archivo, datos_iniciales)
registro_agregar =["Armin", "Cano", "villarica"]
leer_csv = (nombre_archivo)
agregar_csv = (nombre_archivo.registro_agregar)
leer_csv(nombre_archivo)
