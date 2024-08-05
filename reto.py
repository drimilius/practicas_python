import random

# generar un numero secreto entre 1 y 100
numero_secreto = random.randint(1, 100)


def adivina_el_numero(numero_secreto):
    intentos = 0  # contador de intentos
    max_intentos = 4  # número máximo de intentos
    print("Adivine el número secreto (entre 1 y 100): ")
    print("he generado un numero secreto entre 1 y 100")

    for _ in range(max_intentos):
        while True:
            try:
                adivinanza = int(input("Ingresa tu adivinanza: "))
                break
            except ValueError:
                print("Debes ingresar un número entero.")

        intentos += 1

        # comparacion
        if adivinanza == numero_secreto:
            print(f"��Felicidades! Has adivinado el número secreto en {intentos} intentos.")
            return

        if adivinanza < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("El número secreto es menor. Intenta de nuevo.")

    # mensaje final
    print(f"No pudiste adivinar el número secreto, el numero secreto era {numero_secreto}.")


adivina_el_numero(numero_secreto)

# Desafío: Adivina el Número Secreto
# Objetivo: Implementar un juego en Python donde el usuario debe adivinar un número secreto entre 1 y 100.
# El programa debe indicar si el número ingresado es mayor o menor al número secreto y continuar preguntando hasta que el usuario lo adivine.

# Instrucciones:
# Generar un número secreto aleatorio entre 1 y 100.
# Pedir al usuario que adivine el número secreto.
# Comparar el número ingresado por el usuario con el número secreto:
# Si el número ingresado es mayor que el número secreto, mostrar el mensaje: "El número secreto es menor. Intenta de nuevo."
# Si el número ingresado es menor que el número secreto, mostrar el mensaje: "El número secreto es mayor. Intenta de nuevo."
# Si el número ingresado es igual al número secreto, mostrar el mensaje: "¡Felicidades! Has adivinado el número secreto." y terminar el juego.
# Continuar pidiendo al usuario que adivine hasta que acierte el número secreto.
