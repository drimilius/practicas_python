def calcular_precio_final(precio_inicial, descuento):
    if descuento < 0 or descuento > 100:
        return "Invalid"
    elif descuento == 0:
        return precio_inicial
    elif descuento == 100:
        return 0
    else:
        precio_final = precio_inicial *(1 - descuento / 100)
        return precio_final

def solicitar_numeros():
    precio_inicial = float(input("Ingrese el precio inicial: "))
    descuento = float(input("Ingrese el descuento: "))
    resultados = calcular_precio_final(precio_inicial, descuento)
    print(f"el precio final con descuento es {resultados}")

solicitar_numeros()    