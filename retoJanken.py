import random

# 1 opciones del juego
# 2 funciones del juego para saber el ganador
# 3 creacion de puntajes
# 4 bucle del juego
# 5 mostrar los puntajes al finalizar el juego


# opciones del juego

opciones = ["piedra", "papel", "tijera"]


# función para saber el ganador
def ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    elif (jugador == "piedra" and computadora == "tijera") or\
         (jugador == "papel" and computadora == "piedra") or\
         (jugador == "tijera" and computadora == "papel"):
        return "jugador"
    else:
        return "computadora"

# puntajes
puntaje_jugador = 0
puntaje_computadora = 0

# juego
while True:  # bucle del juego
# eleccion del jugador
    eleccion_jugador = input("Escoja: piedra, papel o tijera (o 'salir' para terminar): ").lower()

    if eleccion_jugador == "salir":
        break
    if eleccion_jugador not in opciones:
        print("Opción inválida. Intente nuevamente.")
        continue
#eleccion de la computadora
    eleccion_computadora = random.choice(opciones)
    print(f"la computadora eligio : {eleccion_computadora}")
# determinar el ganador
    resultado = ganador(eleccion_jugador, eleccion_computadora)

    if resultado == "jugador":
        print("Ganaste!")
        puntaje_jugador += 1
    elif resultado == "computadora":
        print("Perdiste!")
        puntaje_computadora += 1
    else:
        print("Empate!")

    print(f"Puntaje jugador: {puntaje_jugador}, Puntaje computadora: {puntaje_computadora}")

# mostrar el resultado final
print("Juego Terminado!")
print(f"puntaje final =jugador: {puntaje_jugador}, computadora: {puntaje_computadora}")
if puntaje_jugador > puntaje_computadora:
    print("Ganaste la partida!")
elif puntaje_jugador < puntaje_computadora:
    print("Perdiste la partida!")
else:
    print("Empate!")
