import csv
class ProcesadorCsv:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
        self.datos = []

    def leer_datos(self):
        with open(self.archivo_entrada, mode="r") as file:
            reader = csv.DictReader(file)
            self.datos = [fila for fila in reader]
            