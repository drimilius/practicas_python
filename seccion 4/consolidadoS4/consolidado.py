import csv
#parte 3 del consolidado 
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, {self.nro_ruedas} ruedas"

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(clase, atributos):
        if clase == "Particular":
            return Particular(**atributos)
        elif clase == "Carga":
            return Carga(**atributos)
        elif clase == "Bicicleta":
            return Bicicleta(**atributos)
        elif clase == "Motocicleta":
            return Motocicleta(**atributos)

    def guardar_datos_csv(self, nombre_archivo="seccion 4/consolidadoS4/vehiculos.csv"):
        try:
            with open(nombre_archivo, 'a', newline='') as archivo:  # 'a' para agregar sin sobrescribir
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow([self.__class__.__name__, self.to_dict()])
            print(f"Datos del {self.__class__.__name__} guardados en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    @staticmethod
    def leer_datos_csv(nombre_archivo="seccion 4/consolidadoS4/vehiculos.csv"):
        vehiculos = {
            "Particular": [],
            "Carga": [],
            "Bicicleta": [],
            "Motocicleta": []
        }
        try:
            with open(nombre_archivo, 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                for fila in archivo_csv:
                    clase, atributos = fila
                    atributos = eval(atributos)
                    vehiculo = Vehiculo.from_dict(clase, atributos)
                    vehiculos[clase].append(vehiculo)
            print("Datos recuperados exitosamente de vehiculos.csv")
        except Exception as e:
            print(f"Error al leer los datos: {e}")
        return vehiculos

#parte 1 del consolidado
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.nro_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{super().__str__()} Carga: {self.carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

#guardar los datos de los vehiculos
def guardar_vehiculos():
    vehiculos = []
    n = int(input("¿Cuántos Vehículos desea insertar? "))

    for i in range(n):
        print(f"\nSelecciona el tipo de vehículo {i + 1}:")
        print("1. Particular")
        print("2. Carga")
        print("3. Bicicleta")
        print("4. Motocicleta")
        tipo = int(input("Opción: "))

        marca = input("Inserte la marca del vehículo: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))

        if tipo == 1:  # Particular
            velocidad = int(input("Inserte la velocidad en km/h: "))
            cilindrada = int(input("Inserte el cilindraje en cc: "))
            nro_puestos = int(input("Inserte el número de puestos: "))
            vehiculo = Particular(marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos)

        elif tipo == 2:  # Carga
            velocidad = int(input("Inserte la velocidad en km/h: "))
            cilindrada = int(input("Inserte el cilindraje en cc: "))
            carga = int(input("Inserte el peso de la carga en kg: "))
            vehiculo = Carga(marca, modelo, nro_ruedas, velocidad, cilindrada, carga)

        elif tipo == 3:  # Bicicleta
            tipo_bici = input("Inserte el tipo de bicicleta (Urbana/Carrera): ")
            vehiculo = Bicicleta(marca, modelo, nro_ruedas, tipo_bici)

        elif tipo == 4:  # Motocicleta
            tipo_bici = input("Inserte el tipo de motocicleta (Deportiva/Turismo): ")
            motor = input("Inserte el tipo de motor (2T/4T): ")
            cuadro = input("Inserte el tipo de cuadro: ")
            nro_radios = int(input("Inserte el número de radios: "))
            vehiculo = Motocicleta(marca, modelo, nro_ruedas, tipo_bici, motor, cuadro, nro_radios)

        else:
            print("Opción no válida.")
            continue

        vehiculos.append(vehiculo)
        vehiculo.guardar_datos_csv()  # Guardar cada vehículo en el CSV

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehiculo in enumerate(vehiculos, 1):
        print(f"Datos del vehículo {i}: {vehiculo}")

#menu
def leer_vehiculos():
    print("\n¿Qué tipo de vehiculo desea ver?")
    print("1. Todos los vehículos")
    print("2. Solo vehículos particulares")
    print("3. Solo vehículos de carga")
    print("4. Solo bicicletas")
    print("5. Solo motocicletas")
    opcion = int(input("Opción: "))

    vehiculos_leidos = Vehiculo.leer_datos_csv()

    if opcion == 1:
        for tipo, vehiculos in vehiculos_leidos.items():
            print(f"Lista de Vehículos {tipo}:")
            for vehiculo in vehiculos:
                print(vehiculo)
    elif opcion == 2:
        print("Lista de Vehículos Particular:")
        for vehiculo in vehiculos_leidos["Particular"]:
            print(vehiculo)
    elif opcion == 3:
        print("Lista de Vehículos Carga:")
        for vehiculo in vehiculos_leidos["Carga"]:
            print(vehiculo)
    elif opcion == 4:
        print("Lista de Bicicletas:")
        for vehiculo in vehiculos_leidos["Bicicleta"]:
            print(vehiculo)
    elif opcion == 5:
        print("Lista de Motocicletas:")
        for vehiculo in vehiculos_leidos["Motocicleta"]:
            print(vehiculo)
    else:
        print("Opción no válida.")


def main():
    print("¿Qué desea hacer?")
    print("1. Guardar datos")
    print("2. Leer datos")
    opcion = int(input("Opción: "))

    if opcion == 1:
        guardar_vehiculos()
    elif opcion == 2:
        leer_vehiculos()
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
