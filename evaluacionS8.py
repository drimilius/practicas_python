"""Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
• Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
• Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
• Finalmente, imprimiremos en pantalla el diccionario resultante.
Ejemplo de impresión en pantalla:
"""
#listas
listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

#diccionario

diccionario = {
    "A": listas[0],
    "B": listas[1],
    "C": listas[2],
    "D": listas[3]
}

#recorrer la sublista
#Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
def sub_lista(listas): #no olvidar nunca el def (mensaje personal)
    for sublista in listas:
        if sublista[0]== 0:
            continue
    # Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
        for numero in sublista:
            if numero != 0:
                print(numero, end="")
        print()

#diccionario
#• Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
# segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
def diccionarios(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
        
    
#imprimir el diccionario
#Finalmente, imprimiremos en pantalla el diccionario resultante.
print("datos sublistas: ")
sub_lista(listas)
print("\ndiccionario resultante:")
diccionarios(diccionario)

