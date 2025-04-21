# viewer.py

def ver_pelicula(peliculas, valoraciones, usuario_actual):
    nombre = input("Ingrese el nombre exacto de la película a ver: ")
    encontrada = False
    for peli in peliculas:
        if peli[0].lower() == nombre.lower():
            print(f"Reproduciendo '{peli[0]}' de {peli[1]} ({peli[2]}), Género: {peli[3]}")
            puntaje = input("¿Qué puntaje le das del 1 al 5? ")
            valoraciones.append([usuario_actual, peli[0], puntaje])
            print("¡Gracias por valorar la película!")
            encontrada = True
            break
    if not encontrada:
        print("Película no encontrada.")

def ver_valoraciones_personales(valoraciones, usuario_actual):
    print(f"\nValoraciones de {usuario_actual}:")
    encontrado = False
    for val in valoraciones:
        if val[0] == usuario_actual:
            print(f"Película: {val[1]} | Puntaje: {val[2]}")
            encontrado = True
    if not encontrado:
        print("No has valorado ninguna película todavía.")
