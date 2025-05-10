# admin.py
import re

def agregar_pelicula(peliculas):
    nombre = input("Nombre de la película: ")
    autor = input("Autor/Director: ")
    anio = input("Año de salida: ")
    genero = input("Género: ")
    nueva_peli = [nombre, autor, anio, genero]
    peliculas.append(nueva_peli)
    print("Película agregada con éxito.")



def eliminar_pelicula(peliculas):
    patron = input("Escribe parte del nombre de la película a eliminar: ")
    regex = re.compile(f".*{patron}.*", re.IGNORECASE)
    coincidencias = []

    for peli in peliculas:
        if regex.search(peli[0]):
            coincidencias.append(peli)

    if not coincidencias:
        print("No se encontraron coincidencias.")
    else:
        print("Películas encontradas:")
        for idx, peli in enumerate(coincidencias):
            print(f"{idx+1}. {peli[0]} - Director: {peli[1]}")

        seleccion = input("Seleccioná el número de la película a eliminar (o enter para cancelar): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(coincidencias):
                peli_eliminada = coincidencias[seleccion - 1]
                peliculas.remove(peli_eliminada)
                print(f"Película eliminada: {peli_eliminada[0]}")
            else:
                print("Selección inválida.")
        else:
            print("Operación cancelada.")