# search.py
import re
from data import generos

def buscar_pelicula(peliculas):
    try:
        patron = input("Escribe parte del nombre de la película: ")
        regex = re.compile(f".*{patron}.*", re.IGNORECASE)
        coincidencias = [p for p in peliculas if regex.search(p[0])]

        if not coincidencias:
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
                else:
                    print("Selección inválida.")
            else:
                print("Búsqueda cancelada.")
    except Exception as e:
        print(f"⚠️ Error al buscar película: {e}")


def buscar_por_autor(peliculas):
    try:
        autor = input("Escribí el nombre (o parte) del autor/director: ")
        regex = re.compile(f".*{autor}.*", re.IGNORECASE)
        coincidencias = [p for p in peliculas if regex.search(p[1])]

        if not coincidencias:
            print("No se encontraron películas con ese autor.")
        else:
            print("Películas encontradas:")
            for peli in coincidencias:
                print(f"- {peli[0]} ({peli[2]}) - Género: {peli[3]}")
    except Exception as e:
        print(f"⚠️ Error al buscar por autor: {e}")


def buscar_por_genero(peliculas):
    try:
        print("🎭 Seleccione un género para buscar:")
        for clave, valor in generos.items():
            print(f"{clave}. {valor}")
        while True:
            opcion_genero = input("Número de género: ").strip()
            if opcion_genero in generos:
                genero = generos[opcion_genero]
                break
            else:
                print("Opción inválida. Ingresá un número válido.")

        coincidencias = [p for p in peliculas if p[3] == genero]

        if not coincidencias:
            print("No se encontraron películas de ese género.")
        else:
            print("Películas encontradas:")
            for peli in coincidencias:
                print(f"- {peli[0]} ({peli[2]}) - Director: {peli[1]}")
    except Exception as e:
        print(f"⚠️ Error al buscar por género: {e}")
