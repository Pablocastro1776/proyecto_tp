# search.py

import re
from data import generos

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

def buscar_por_autor(peliculas):
    autor = input("Escribí el nombre (o parte) del autor/director: ")
    regex = re.compile(f".*{autor}.*", re.IGNORECASE)
    coincidencias = []

    for peli in peliculas:
        if regex.search(peli[1]):
            coincidencias.append(peli)

    if not coincidencias:
        print("No se encontraron películas con ese autor.")
    else:
        print("Películas encontradas:")
        for peli in coincidencias:
            print(f"- {peli[0]} ({peli[2]}) - Género: {peli[3]}")
            
def buscar_por_genero(peliculas):
    print("🎭 Seleccione un género para buscar:")
    for clave, valor in generos.items():
        print(f"{clave}. {valor}")
    while True:
        opcion_genero = input("Número de género: ").strip()
        if opcion_genero in generos:
            genero = generos[opcion_genero]
            break
        else:
            print("Opción inválida.")
    
    coincidencias = []
    for peli in peliculas:
        if peli[3] == genero:
            coincidencias.append(peli)

    if not coincidencias:
        print("No se encontraron películas de ese género.")
    else:
        print("Películas encontradas:")
        for peli in coincidencias:
            print(f"- {peli[0]} ({peli[2]}) - Director: {peli[1]}")
