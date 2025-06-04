#admin.py

import re
import os
from data import generos, guardar_usuarios


def agregar_pelicula_txt():
    try:
        nombre = input("🎬 Nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        director = input("🎬 Director: ").strip()
        if not director:
            raise ValueError("El director no puede estar vacío.")

        anio = input("📅 Año: ").strip()
        if not anio.isdigit() or len(anio) != 4:
            raise ValueError("El año debe ser numérico y de 4 dígitos.")

        # Selección de género
        print("🎭 Géneros disponibles:")
        for clave, valor in generos.items():
            print(f"{clave}. {valor}")

        opcion_genero = input("Seleccione el número del género: ").strip()
        if opcion_genero not in generos:
            raise ValueError("Opción de género inválida.")

        genero = generos[opcion_genero]
        nueva_linea = f"{nombre}|{director}|{anio}|{genero}\n"

        f = open("peliculas.txt", "a", encoding="utf-8")
        try:
            f.write(nueva_linea)
            print("✅ Película agregada correctamente.")
        finally:
            f.close()
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")



def eliminar_pelicula_txt():
    try:
        patron = input("🔎 Ingrese parte del nombre de la película a eliminar: ").strip().lower()
        if not patron:
            raise ValueError("El nombre a buscar no puede estar vacío.")

        encontrada = False
        original = open("peliculas.txt", "r", encoding="utf-8")
        temporal = open("peliculas_temp.txt", "w", encoding="utf-8")

        try:
            for linea in original:
                campos = linea.strip().split("|")
                if len(campos) == 4 and patron in campos[0].lower():
                    print(f"🗑️ Eliminando: {campos[0]}")
                    encontrada = True
                    continue  # No copiamos esta línea → se elimina
                temporal.write(linea)
        finally:
            original.close()
            temporal.close()

        os.remove("peliculas.txt")
        os.rename("peliculas_temp.txt", "peliculas.txt")

        if not encontrada:
            print("⚠️ No se encontró ninguna película con ese nombre.")
        else:
            print("✅ Película eliminada exitosamente.")
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def listar_peliculas():
    try:
        f = open("peliculas.txt", "r", encoding="utf-8")
        try:
            vacio = True
            for idx, linea in enumerate(f, start=1):
                campos = linea.strip().split("|")
                if len(campos) == 4:
                    print(f"{idx}. {campos[0]} - {campos[1]} ({campos[2]}) - Género: {campos[3]}")
                    vacio = False
            if vacio:
                print("⚠️ No hay películas registradas.")
        finally:
            f.close()
    except Exception as e:
        print(f"⚠️ Error al listar películas: {e}")



def modificar_pelicula_txt():
    patron = input("🔎 Ingrese parte del nombre de la película a modificar: ").strip().lower()
    modificada = False

    try:
        original = open("peliculas.txt", "r", encoding="utf-8")
        temporal = open("peliculas_temp.txt", "w", encoding="utf-8")

        try:
            for linea in original:
                campos = linea.strip().split("|")
                if len(campos) == 4 and patron in campos[0].lower():
                    print(f"✏️ Modificando: {campos[0]}")
                    nuevo_nombre = input("Nuevo nombre (enter para mantener): ").strip() or campos[0]
                    nuevo_director = input("Nuevo director (enter para mantener): ").strip() or campos[1]

                    nuevo_anio = input("Nuevo año (enter para mantener): ").strip()
                    if nuevo_anio and (not nuevo_anio.isdigit() or len(nuevo_anio) != 4):
                        raise ValueError("El año debe tener 4 dígitos.")
                    nuevo_anio = nuevo_anio or campos[2]

                    print("🎭 Géneros disponibles (enter para mantener actual):")
                    for clave, valor in generos.items():
                        print(f"{clave}. {valor}")
                    opcion_genero = input("Seleccione el número del género: ").strip()
                    nuevo_genero = generos.get(opcion_genero, campos[3])

                    nueva_linea = f"{nuevo_nombre}|{nuevo_director}|{nuevo_anio}|{nuevo_genero}\n"
                    temporal.write(nueva_linea)
                    modificada = True
                else:
                    temporal.write(linea)
        finally:
            original.close()
            temporal.close()

        os.remove("peliculas.txt")
        os.rename("peliculas_temp.txt", "peliculas.txt")

        if modificada:
            print("✅ Película modificada con éxito.")
        else:
            print("⚠️ No se encontró la película.")
    except ValueError as ve:
        print(f"⚠️ Error de validación: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")



def crear_usuario(users):
    try:
        nombre = input("Nuevo nombre de usuario: ").strip()
        if nombre in users:
            print("El usuario ya existe.")
            return
        password = input("Contraseña para el nuevo usuario: ")
        rol = input("Rol (usuario/admin): ").strip().lower()
        if rol not in ["usuario", "admin"]:
            print("Rol inválido. Se asigna 'usuario' por defecto.")
            rol = "usuario"
        users[nombre] = {"rol": rol, "password": password}
        guardar_usuarios(users)
        print("Usuario creado correctamente.")
    except Exception as e:
        print(f"⚠️  Error al crear usuario: {e}")


def modificar_usuario(users):
    try:
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
        guardar_usuarios(users)
        print("Usuario actualizado correctamente.")
    except Exception as e:
        print(f"⚠️  Error al modificar usuario: {e}")


def eliminar_usuario(users):
    try:
        nombre = input("Nombre del usuario a eliminar: ")
        if nombre == "admin":
            print("No se puede eliminar al administrador principal.")
            return
        if nombre in users:
            confirmacion = input(f"¿Estás seguro que querés eliminar al usuario '{nombre}'? (s/n): ")
            if confirmacion.lower() == "s":
                del users[nombre]
                guardar_usuarios(users)
                print("Usuario eliminado correctamente.")
        else:
            print("Usuario no encontrado.")
    except Exception as e:
        print(f"⚠️  Error al eliminar usuario: {e}")


def listar_usuarios(users):
    try:
        print("\nLista de usuarios registrados:")
        for nombre, datos in users.items():
            print(f"- {nombre} | Rol: {datos['rol']}")
    except Exception as e:
        print(f"⚠️  Error al listar usuarios: {e}")


def listar_autores_txt():
    try:
        autores = set()
        f = open("peliculas.txt", "r", encoding="utf-8")
        try:
            for linea in f:
                campos = linea.strip().split("|")
                if len(campos) == 4:
                    autores.add(campos[1])
        finally:
            f.close()

        if autores:
            print("\n🧑‍🎬 Autores/Directores registrados en el sistema:")
            for autor in sorted(autores):
                print(f"- {autor}")
        else:
            print("⚠️ No hay autores registrados aún.")
    except Exception as e:
        print(f"⚠️ Error al listar autores: {e}")

def modificar_autor_txt():
    try:
        autor_actual = input("Nombre actual del autor/director a modificar: ").strip()
        if not autor_actual:
            raise ValueError("El nombre del autor no puede estar vacío.")

        encontrado = False

        original = open("peliculas.txt", "r", encoding="utf-8")
        temporal = open("peliculas_temp.txt", "w", encoding="utf-8")

        try:
            for linea in original:
                campos = linea.strip().split("|")
                if len(campos) == 4:
                    if campos[1].lower() == autor_actual.lower():
                        if not encontrado:
                            print(f"🛠️  Modificando películas de: {autor_actual}")
                            nuevo_autor = input("Nuevo nombre del autor/director: ").strip()
                            if not nuevo_autor:
                                raise ValueError("El nuevo nombre del autor no puede estar vacío.")
                        campos[1] = nuevo_autor
                        encontrado = True
                    nueva_linea = "|".join(campos) + "\n"
                    temporal.write(nueva_linea)
        finally:
            original.close()
            temporal.close()

        os.remove("peliculas.txt")
        os.rename("peliculas_temp.txt", "peliculas.txt")

        if encontrado:
            print(f"✅ Autor modificado exitosamente de '{autor_actual}' a '{nuevo_autor}'.")
        else:
            print("⚠️ No se encontraron películas con ese autor.")
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def listar_generos():
    try:
        print("\nGéneros disponibles en el sistema:")
        for genero in sorted(set(generos.values())):
            print(f"- {genero}")
    except Exception as e:
        print(f"⚠️  Error al listar géneros: {e}")
