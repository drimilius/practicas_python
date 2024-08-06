#definir la palabra
palabra = "paralelepipedo"
#definir las vocales
vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = [(indice, letra) for indice, letra in enumerate(palabra) if letra not in vocales]

for posicion, consonantes in consonantes:
    print(f"La consonante '{consonantes}' se encuentra en la posición {posicion+1} de la palabra.")