# search.py

import re

def buscar_pelicula(peliculas):
    patron = input("Escribe parte del nombre de la película: ")
    regex = re.compile(f".*{patron}.*", re.IGNORECASE)
    coincidencias = []
    
    for peli in peliculas:
        if regex.search(peli[0]):
            coincidencias.append(peli)

    if len(coincidencias) == 0:
        print("No se encontraron coincidencias.")
    else:
        print("¿Te referías a alguna de estas?")
        for idx, peli in enumerate(coincidencias):
            print(f"{idx+1}. {peli[0]} - Director: {peli[1]}")

        seleccion = input("Seleccioná el número si era alguna (o enter para salir): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(coincidencias):
                peli = coincidencias[seleccion - 1]
                print(f"Seleccionaste: {peli[0]} de {peli[1]} ({peli[2]})")
