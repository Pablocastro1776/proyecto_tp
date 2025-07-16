# menu.py
from viewer import ver_pelicula, ver_valoraciones_personales, ver_puntuacion_pelicula
from search import buscar_pelicula, buscar_por_autor, buscar_por_genero
from admin import agregar_pelicula_txt, eliminar_pelicula_txt, modificar_pelicula_txt, listar_peliculas, crear_usuario, modificar_usuario, eliminar_usuario, listar_usuarios, listar_autores_txt, modificar_autor_txt, listar_generos, crear_genero, eliminar_genero, modificar_genero, eliminar_autor_txt,totalizar_peliculas_por_genero
from utilidades import ordenar_peliculas_por_anio, peliculas_del_director, mostrar_info_basica, mostrar_generos_unicos, top_3_peliculas

def menu(usuario_actual, users, valoraciones):
    if users[usuario_actual]["rol"] == "admin":
        menu_admin(users, valoraciones)
    else:
        menu_usuario(usuario_actual, users, valoraciones)

# ========== MENÚ PARA USUARIOS COMUNES ==========

def menu_usuario(usuario_actual, users, valoraciones):
    while True:
        print("\n" + "=" * 50)
        print("📽️  SISTEMA DE PELÍCULAS".center(50))
        print("=" * 50)
        print("1. Buscar Película por Nombre")
        print("2. Ver Película")
        print("3. Ver mis Valoraciones")
        print("4. Ver Puntuación de una Película")
        print("5. Buscar por Autor")
        print("6. Buscar por Género")
        print("0. 🔒 Cerrar Sesión")
        print("-" * 50)

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            buscar_pelicula()
        elif opcion == "2":
            ver_pelicula(valoraciones, usuario_actual)
        elif opcion == "3":
            ver_valoraciones_personales(valoraciones, usuario_actual)
        elif opcion == "4":
            ver_puntuacion_pelicula()
        elif opcion == "5":
            buscar_por_autor()
        elif opcion == "6":
            buscar_por_genero()
        elif opcion == "0":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

# ========== MENÚ ADMINISTRADOR ==========

def menu_admin(users, valoraciones):
    while True:
        print("\n" + "=" * 50)
        print("🔧 PANEL DE ADMINISTRADOR".center(50))
        print("=" * 50)
        print("1. Gestión de Películas")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Autores")
        print("4. Gestión de Géneros")
        print("5. Funciones de Análisis")
        print("0. 🔒 Cerrar Sesión")
        print("-" * 50)

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_peliculas_admin(valoraciones)
        elif opcion == "2":
            menu_usuarios(users)
        elif opcion == "3":
            menu_autores()
        elif opcion == "4":
            menu_generos()
        elif opcion == "5":
            menu_analisis(valoraciones)
        elif opcion == "0":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")

# ========== SUBMENÚS ADMIN ==========

def menu_peliculas_admin(valoraciones):
    while True:
        print("\n🎬 GESTIÓN DE PELÍCULAS")
        print("1. Agregar Película")
        print("2. Modificar Película")
        print("3. Eliminar Película")
        print("4. Ver Lista de Películas")
        print("5. Reproducir Película")
        print("6. Ver Puntuación de una Película")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_pelicula_txt()
        elif opcion == "2":
            modificar_pelicula_txt()
        elif opcion == "3":
            eliminar_pelicula_txt()
        elif opcion == "4":
            listar_peliculas()
        elif opcion == "5":
            ver_pelicula(valoraciones, "admin")
        elif opcion == "6":
            ver_puntuacion_pelicula()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_usuarios(users):
    while True:
        print("\n👤 GESTIÓN DE USUARIOS")
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

def menu_autores():
    while True:
        print("\n🎬  GESTIÓN DE AUTORES")
        print("1. Ver Autores")
        print("2. Modificar Autor")
        print("3. Eliminar Autor")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_autores_txt()
        elif opcion == "2":
            modificar_autor_txt()
        elif opcion == "3":
            eliminar_autor_txt()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_generos():
    while True:
        print("\n🎭  GESTIÓN DE GÉNEROS")
        print("1. Ver Géneros Disponibles")
        print("2. Crear Nuevo Género")
        print("3. Eliminar Género")
        print("4. Modificar Género")
        print("5. Totalizar películas por género")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_generos()
        elif opcion == "2":
            crear_genero()
        elif opcion == "3":
            eliminar_genero()
        elif opcion == "4":
            modificar_genero()
        elif opcion == "5":
            totalizar_peliculas_por_genero()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_analisis(valoraciones):
    while True:
        print("\n📊 FUNCIONES DE ANÁLISIS")
        print("1. Películas ordenadas por año")
        print("2. Películas por director")
        print("3. Info básica (título y año)")
        print("4. Ver géneros únicos")
        print("5. Top 3 películas mejor valoradas")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ordenar_peliculas_por_anio()
        elif opcion == "2":
            peliculas_del_director()
        elif opcion == "3":
            mostrar_info_basica()
        elif opcion == "4":
            mostrar_generos_unicos()
        elif opcion == "5":
            top_3_peliculas(valoraciones)
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")