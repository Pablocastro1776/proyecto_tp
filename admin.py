# admin.py

def agregar_pelicula(peliculas):
    nombre = input("Nombre de la película: ")
    autor = input("Autor/Director: ")
    anio = input("Año de salida: ")
    genero = input("Género: ")
    nueva_peli = [nombre, autor, anio, genero]
    peliculas.append(nueva_peli)
    print("Película agregada con éxito.")
