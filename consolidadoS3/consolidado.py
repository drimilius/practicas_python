#lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

#agregar "el gran"

def grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "el gran " + magos[i]

#imprimir el nombre
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

#separacion en grupos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientiificos = ["Newton", "Hawking", "Einstein"]
otros = []

for nombre in nombres:
    if nombre not in magos and nombre not in cientiificos:
        otros.append(nombre)
        
#imprimir pantalla
print("lista completa de nombres:")
imprimir_nombres(nombres)

grandioso(magos)

#imprimir magos 
print("\nMagos grandiosos:")
imprimir_nombres(magos)

#imprimir cientiificos
print("\nCientiificos:")
imprimir_nombres(cientiificos)

#imprimir otros
print("\nOtros:")
imprimir_nombres(otros)
