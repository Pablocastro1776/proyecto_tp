# viewer.py

import re

def ver_pelicula(peliculas, valoraciones, usuario_actual):
    patron = input("Escribí el nombre (o parte) de la película que querés ver: ")
    regex = re.compile(f".*{patron}.*", re.IGNORECASE)
    coincidencias = []

    for peli in peliculas:
        if regex.search(peli[0]):
            coincidencias.append(peli)

    if len(coincidencias) == 0:
        print("No se encontraron películas.")
        return

    print("¿Cuál de estas querés ver?")
    for idx, peli in enumerate(coincidencias):
        print(f"{idx + 1}. {peli[0]} - {peli[1]} ({peli[2]}) - {peli[3]}")

    seleccion = input("Seleccioná el número o presioná Enter para cancelar: ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(coincidencias):
            peli = coincidencias[seleccion - 1]
            print(f"Reproduciendo '{peli[0]}' de {peli[1]} ({peli[2]}) - Género: {peli[3]}")

            # Validación de puntaje con assert
            while True:
                try:
                    puntaje = int(input("¿Qué puntaje le das del 1 al 5? "))
                    assert 1 <= puntaje <= 5, "El puntaje debe estar entre 1 y 5."
                    break
                except ValueError:
                    print("⚠️ Ingresá un número entero válido.")
                except AssertionError as e:
                    print(f"⚠️ {e}")

            valoraciones.append([usuario_actual, peli[0], str(puntaje)])
            print("¡Gracias por valorar la película!")

def ver_puntuacion_pelicula(peliculas, valoraciones):
    patron = input("Escribí el nombre (o parte) de la película: ")
    regex = re.compile(f".*{patron}.*", re.IGNORECASE)
    coincidencias = []

    for peli in peliculas:
        if regex.search(peli[0]):
            coincidencias.append(peli)

    if len(coincidencias) == 0:
        print("No se encontraron coincidencias.")
        return

    print("¿Te referías a alguna de estas?")
    for idx, peli in enumerate(coincidencias):
        print(f"{idx + 1}. {peli[0]} - {peli[1]}")

    seleccion = input("Seleccioná el número (o enter para cancelar): ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(coincidencias):
            nombre_peli = coincidencias[seleccion - 1][0]
            total = 0
            cantidad = 0
            for val in valoraciones:
                if val[1] == nombre_peli:
                    total += int(val[2])
                    cantidad += 1
            if cantidad > 0:
                promedio = total / cantidad
                print(f"La película '{nombre_peli}' tiene un promedio de {promedio:.2f} puntos basado en {cantidad} valoraciones.")
            else:
                print("Esta película no tiene valoraciones aún.")

def ver_valoraciones_personales(valoraciones, usuario_actual):
    print(f"\nValoraciones de {usuario_actual}:")
    encontrado = False
    for val in valoraciones:
        if val[0] == usuario_actual:
            print(f"Película: {val[1]} | Puntaje: {val[2]}")
            encontrado = True
    if not encontrado:
        print("No has valorado ninguna película todavía.")
