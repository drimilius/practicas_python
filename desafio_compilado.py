# Lista de niveles con sus respectivos puntos
niveles = ["Facil", "Medio", "Dificil", "Experto"]
puntos_por_nivel = [10, 20, 30, 50]

# Diccionario para almacenar los jugadores y sus puntuaciones
jugadores = {
    "Alice": 0,
    "Alejandro": 10,
    "Camila": 50
}

# Solicitar el nombre del jugador
nombre_jugador = input("Introduce el nombre del jugador: ")

# Verificar si el jugador existe en el diccionario
if jugadores.get(nombre_jugador) is None:
    print("El jugador no existe en el sistema.")
else:
    # Solicitar el nivel completado
    nivel_completado = input("Introduce el nivel completado (Facil, Medio, Dificil, Experto): ")
    if nivel_completado not in niveles:
        print("El nivel ingresado no es válido.")
    else:
        # Solicitar el tiempo para completar el nivel
        tiempo_completado = input("Introduce el tiempo en segundos que tardó en completar el nivel: ")
        if not tiempo_completado.isdigit() or float(tiempo_completado) <= 0:
            print("El tiempo debe ser un número positivo.")
        else:
            # Calcular la puntuación basada en el nivel completado
            indice_nivel = niveles.index(nivel_completado)
            puntos = puntos_por_nivel[indice_nivel]

            # Aplicar bonificación si corresponde
            if (nivel_completado == "facil" or nivel_completado == "medio") and float(tiempo_completado) <= 10:
                puntos += 5  # Bonificación de 5 puntos
                
            if (nivel_completado == "Difícil" or nivel_completado == "Experto") and float(tiempo_completado) <= 30:
                puntos += 10  # Bonificación de 10 puntos

            # Actualizar la puntuación del jugador
            jugadores[nombre_jugador] += puntos

            # Mostrar las puntuaciones actuales de todos los jugadores
            print("\nPuntuaciones actuales:")
            print(f"Alice: {jugadores['Alice']} puntos")
            print(f"Alejandro: {jugadores['Alejandro']} puntos")
            print(f"Camila: {jugadores['Camila']} puntos")

            # Determinar el líder actual del juego
            max_puntuacion = max(jugadores['Alice'], jugadores['Alejandro'], jugadores['Camila'])

            lider1 = lider2 = lider3 = None
            if jugadores['Alice'] == max_puntuacion:
                lider1 = "Alice"
            if jugadores['Alejandro'] == max_puntuacion:
                lider2 = "Alejandro"
            if jugadores['Camila'] == max_puntuacion:
                lider3 = "Camila"

            print("\nLíder actual(es) del juego:")
            if lider1:
                print(f"{lider1} con {max_puntuacion} puntos")
            if lider2:
                print(f"{lider2} con {max_puntuacion} puntos")
            if lider3:
                print(f"{lider3} con {max_puntuacion} puntos")

            print("\n" + "-"*30 + "\n")
