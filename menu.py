# menu.py

from viewer import ver_pelicula, ver_valoraciones_personales, ver_puntuacion_pelicula
from search import buscar_pelicula, buscar_por_autor, buscar_por_genero
from admin import agregar_pelicula, eliminar_pelicula, modificar_pelicula, listar_peliculas, crear_usuario, modificar_usuario, eliminar_usuario, listar_usuarios, listar_autores, modificar_autor, listar_generos, modificar_genero
from utilidades import ordenar_peliculas_por_anio, peliculas_del_director, mostrar_info_basica, mostrar_generos_unicos

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

        if users[usuario_actual]["rol"] == "admin":
            print("\n🛠️  FUNCIONES DE ADMINISTRADOR")
            print("11. Agregar Película")
            print("12. Eliminar Película")
            print("13. Modificar Película")
            print("14. Ver Lista de Películas")
            print("15. Crear Usuario")
            print("16. Modificar Usuario")
            print("17. Eliminar Usuario")
            print("18. Ver Usuarios Registrados")
            print("19. Ver Autores")
            print("20. Modificar Autor")
            print("21. Ver Géneros")
            print("22. Modificar Género")

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

        # Funciones de admin
        elif opcion == "11" and users[usuario_actual]["rol"] == "admin":
            agregar_pelicula(peliculas)
        elif opcion == "12" and users[usuario_actual]["rol"] == "admin":
            eliminar_pelicula(peliculas)
        elif opcion == "13" and users[usuario_actual]["rol"] == "admin":
            modificar_pelicula(peliculas)
        elif opcion == "14" and users[usuario_actual]["rol"] == "admin":
            listar_peliculas(peliculas)
        elif opcion == "15" and users[usuario_actual]["rol"] == "admin":
            crear_usuario(users)
        elif opcion == "16" and users[usuario_actual]["rol"] == "admin":
            modificar_usuario(users)
        elif opcion == "17" and users[usuario_actual]["rol"] == "admin":
            eliminar_usuario(users)
        elif opcion == "18" and users[usuario_actual]["rol"] == "admin":
            listar_usuarios(users)
        elif opcion == "19" and users[usuario_actual]["rol"] == "admin":
            listar_autores(peliculas)
        elif opcion == "20" and users[usuario_actual]["rol"] == "admin":
            modificar_autor(peliculas)
        elif opcion == "21" and users[usuario_actual]["rol"] == "admin":
            listar_generos(peliculas)
        elif opcion == "22" and users[usuario_actual]["rol"] == "admin":
            modificar_genero(peliculas)

        elif opcion == "0":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")
