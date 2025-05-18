# menu.py
from viewer import ver_pelicula, ver_valoraciones_personales, ver_puntuacion_pelicula
from search import buscar_pelicula, buscar_por_autor, buscar_por_genero
from admin import (
    agregar_pelicula, eliminar_pelicula, modificar_pelicula, listar_peliculas,
    crear_usuario, modificar_usuario, eliminar_usuario, listar_usuarios,
    listar_autores, modificar_autor, listar_generos
)
from utilidades import (
    ordenar_peliculas_por_anio, peliculas_del_director, mostrar_info_basica,
    mostrar_generos_unicos, top_3_peliculas
)

def menu(usuario_actual, users, peliculas, valoraciones):
    while True:
        print("\n" + "=" * 50)
        print("📽️  BIENVENIDO AL SISTEMA DE PELÍCULAS".center(50))
        print("=" * 50)

        print("\n🎬 FUNCIONES GENERALES")
        print("1. Buscar Película por Nombre")
        print("2. Ver Película")
        print("3. Ver mis Valoraciones")
        print("4. Ver Puntuación de una Película")
        print("5. Buscar por Autor")
        print("6. Buscar por Género")

        print("\n📊 FUNCIONES DE ANÁLISIS")
        print("7. Películas ordenadas por año")
        print("8. Películas por director")
        print("9. Info básica (título y año)")
        print("10. Ver géneros únicos")
        print("11. Top 3 películas mejor valoradas")

        if users[usuario_actual]["rol"] == "admin":
            print("\n🛠️  FUNCIONES DE ADMINISTRADOR")
            print("12. Gestión de Películas")
            print("13. Gestión de Usuarios")
            print("14. Gestión de Autores")
            print("15. Gestión de Géneros")

        print("\n0. 🔒 Cerrar Sesión")
        print("-" * 50)
        opcion = input("Seleccione una opción: ")

        # Funciones comunes
        if opcion == "1":
            buscar_pelicula(peliculas)
        elif opcion == "2":
            ver_pelicula(peliculas, valoraciones, usuario_actual)
        elif opcion == "3":
            ver_valoraciones_personales(valoraciones, usuario_actual)
        elif opcion == "4":
            ver_puntuacion_pelicula(peliculas, valoraciones)
        elif opcion == "5":
            buscar_por_autor(peliculas)
        elif opcion == "6":
            buscar_por_genero(peliculas)

        # Funciones de análisis
        elif opcion == "7":
            ordenar_peliculas_por_anio(peliculas)
        elif opcion == "8":
            peliculas_del_director(peliculas)
        elif opcion == "9":
            mostrar_info_basica(peliculas)
        elif opcion == "10":
            mostrar_generos_unicos(peliculas)
        elif opcion == "11":
            top_3_peliculas(valoraciones)

        # Submenús del administrador
        elif opcion == "12" and users[usuario_actual]["rol"] == "admin":
            menu_peliculas(peliculas)
        elif opcion == "13" and users[usuario_actual]["rol"] == "admin":
            menu_usuarios(users)
        elif opcion == "14" and users[usuario_actual]["rol"] == "admin":
            menu_autores(peliculas)
        elif opcion == "15" and users[usuario_actual]["rol"] == "admin":
            menu_generos(peliculas)

        elif opcion == "0":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

# SUBMENÚS

def menu_peliculas(peliculas):
    while True:
        print("\n🎞️  GESTIÓN DE PELÍCULAS")
        print("1. Agregar Película")
        print("2. Modificar Película")
        print("3. Eliminar Película")
        print("4. Ver Lista de Películas")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_pelicula(peliculas)
        elif opcion == "2":
            modificar_pelicula(peliculas)
        elif opcion == "3":
            eliminar_pelicula(peliculas)
        elif opcion == "4":
            listar_peliculas(peliculas)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_usuarios(users):
    while True:
        print("\n👤  GESTIÓN DE USUARIOS")
        print("1. Crear Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Ver Usuarios Registrados")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_usuario(users)
        elif opcion == "2":
            modificar_usuario(users)
        elif opcion == "3":
            eliminar_usuario(users)
        elif opcion == "4":
            listar_usuarios(users)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_autores(peliculas):
    while True:
        print("\n🎬  GESTIÓN DE AUTORES")
        print("1. Ver Autores")
        print("2. Modificar Autor")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_autores(peliculas)
        elif opcion == "2":
            modificar_autor(peliculas)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_generos(peliculas):
    while True:
        print("\n🎭  GESTIÓN DE GÉNEROS")
        print("1. Ver Géneros Disponibles")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_generos(peliculas)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
