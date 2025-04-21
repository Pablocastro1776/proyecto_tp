# menu.py

from viewer import ver_pelicula, ver_valoraciones_personales
from search import buscar_pelicula
from admin import agregar_pelicula

def menu(usuario_actual, users, peliculas, valoraciones):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Buscar Película")
        print("2. Ver Película")
        print("3. Ver mis Valoraciones")
        if users[usuario_actual]["rol"] == "admin":
            print("4. Agregar Película")
        print("0. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_pelicula(peliculas)
        elif opcion == "2":
            ver_pelicula(peliculas, valoraciones, usuario_actual)
        elif opcion == "3":
            ver_valoraciones_personales(valoraciones, usuario_actual)
        elif opcion == "4" and users[usuario_actual]["rol"] == "admin":
            agregar_pelicula(peliculas)
        elif opcion == "0":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")
