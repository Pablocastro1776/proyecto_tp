# admin.py
import re

def agregar_pelicula(peliculas):
    print("\n" + "-" * 50)
    print("🎞️  CARGA DE NUEVA PELÍCULA".center(50))
    print("-" * 50)
    nombre = input("🎬 Nombre: ")
    autor = input("🎬 Director: ")
    anio = input("📅 Año de estreno: ")
    genero = input("🎭 Género: ")
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
            
def listar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas cargadas.")
    else:
        print("\nLista de películas:")
        for idx, peli in enumerate(peliculas):
            print(f"{idx+1}. {peli[0]} - {peli[1]} ({peli[2]}) - Género: {peli[3]}")


def modificar_pelicula(peliculas):
    patron = input("Escribí parte del nombre de la película a modificar: ")
    regex = re.compile(f".*{patron}.*", re.IGNORECASE)
    coincidencias = []

    for peli in peliculas:
        if regex.search(peli[0]):
            coincidencias.append(peli)

    if not coincidencias:
        print("No se encontraron coincidencias.")
        return

    print("Películas encontradas:")
    for idx, peli in enumerate(coincidencias):
        print(f"{idx+1}. {peli[0]} - Director: {peli[1]}")

    seleccion = input("Seleccioná el número de la película a modificar (o enter para cancelar): ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(coincidencias):
            peli = coincidencias[seleccion - 1]
            print(f"Modificando: {peli[0]}")
            nuevo_nombre = input("Nuevo nombre (o enter para mantener actual): ")
            nuevo_autor = input("Nuevo autor/director (o enter para mantener actual): ")
            nuevo_anio = input("Nuevo año (o enter para mantener actual): ")
            nuevo_genero = input("Nuevo género (o enter para mantener actual): ")

            if nuevo_nombre:
                peli[0] = nuevo_nombre
            if nuevo_autor:
                peli[1] = nuevo_autor
            if nuevo_anio:
                peli[2] = nuevo_anio
            if nuevo_genero:
                peli[3] = nuevo_genero

            print("Película modificada con éxito.")

def listar_usuarios(users):
    print("\nLista de usuarios registrados:")
    for nombre, datos in users.items():
        print(f"- {nombre} | Rol: {datos['rol']}")

def crear_usuario(users):
    nombre = input("Nuevo nombre de usuario: ")
    if nombre in users:
        print("El usuario ya existe.")
        return
    password = input("Contraseña para el nuevo usuario: ")
    rol = input("Rol (usuario/admin): ")
    if rol not in ["usuario", "admin"]:
        print("Rol inválido. Se asigna 'usuario' por defecto.")
        rol = "usuario"
    users[nombre] = {"rol": rol, "password": password}
    print("Usuario creado correctamente.")

def modificar_usuario(users):
    nombre = input("Nombre del usuario a modificar: ")
    if nombre not in users:
        print("Usuario no encontrado.")
        return
    print(f"Modificando usuario: {nombre}")
    nueva_contra = input("Nueva contraseña (o enter para mantener actual): ")
    nuevo_rol = input("Nuevo rol (usuario/admin) (o enter para mantener actual): ")

    if nueva_contra:
        users[nombre]["password"] = nueva_contra
    if nuevo_rol in ["usuario", "admin"]:
        users[nombre]["rol"] = nuevo_rol
    print("Usuario actualizado correctamente.")

def eliminar_usuario(users):
    nombre = input("Nombre del usuario a eliminar: ")
    if nombre == "admin":
        print("No se puede eliminar al administrador principal.")
        return
    if nombre in users:
        confirmacion = input(f"¿Estás seguro que querés eliminar al usuario '{nombre}'? (s/n): ")
        if confirmacion.lower() == "s":
            del users[nombre]
            print("Usuario eliminado correctamente.")
    else:
        print("Usuario no encontrado.")

def listar_autores(peliculas):
    autores = set(peli[1] for peli in peliculas)
    print("\nAutores registrados en el sistema:")
    for autor in sorted(autores):
        print(f"- {autor}")

def modificar_autor(peliculas):
    autor_actual = input("Nombre actual del autor/director a modificar: ")
    encontrado = False
    for peli in peliculas:
        if peli[1] == autor_actual:
            encontrado = True
            break

    if not encontrado:
        print("No se encontraron películas con ese autor.")
        return

    nuevo_autor = input("Nuevo nombre del autor/director: ")
    for peli in peliculas:
        if peli[1] == autor_actual:
            peli[1] = nuevo_autor

    print(f"Autor modificado exitosamente de '{autor_actual}' a '{nuevo_autor}'.")

def listar_generos(peliculas):
    generos = set(peli[3] for peli in peliculas)
    print("\nGéneros registrados en el sistema:")
    for genero in sorted(generos):
        print(f"- {genero}")

def modificar_genero(peliculas):
    genero_actual = input("Género actual a modificar: ")
    encontrado = False
    for peli in peliculas:
        if peli[3] == genero_actual:
            encontrado = True
            break

    if not encontrado:
        print("No se encontraron películas con ese género.")
        return

    nuevo_genero = input("Nuevo nombre del género: ")
    for peli in peliculas:
        if peli[3] == genero_actual:
            peli[3] = nuevo_genero

    print(f"Género modificado exitosamente de '{genero_actual}' a '{nuevo_genero}'.")
