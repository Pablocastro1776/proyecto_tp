#admin.py

import json
import re
import os
from data import cargar_generos, guardar_usuarios,iterar_generos, guardar_generos

GENEROS_FILE = "generos.json"

def agregar_pelicula_txt():
    try:
        generos = cargar_generos()
        if not generos:
            print("⚠️ No hay géneros disponibles.")
            return

        nombre = input("🎬 Nombre: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        director = input("🎬 Director: ").strip()
        if not director:
            raise ValueError("El director no puede estar vacío.")

        anio = input("📅 Año: ").strip()
        if not anio.isdigit() or len(anio) != 4:
            raise ValueError("El año debe ser numérico y de 4 dígitos.")

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
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
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
    except PermissionError:
        print("❌ Permiso denegado al acceder o modificar archivos.")
    except UnicodeDecodeError:
        print("❌ Error de codificación al leer el archivo.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def listar_peliculas():
    try:
        f = open("peliculas.txt", "r", encoding="utf-8")
        try:
            print("\n📃 Lista de películas:")
            listar_peliculas_recursiva(f)
        finally:
            try:
                f.close()
            except OSError as close_error:
                print(f"⚠️ Error al cerrar el archivo: {close_error}")
    except FileNotFoundError:
        print("❌ El archivo de películas no fue encontrado.")
    except OSError as os_err:
        print(f"❌ Error de lectura del archivo: {os_err}")
    except Exception as e:
        print(f"⚠️ Error al listar películas: {e}")

def listar_peliculas_recursiva(f, idx=1):
    try:
        linea = f.readline()
        if not linea:
            return
        campos = linea.strip().split("|")
        if len(campos) == 4:
            print(f"{idx}. {campos[0]} - {campos[1]} ({campos[2]}) - Género: {campos[3]}")
        else:
            print(f"⚠️ Línea con formato inválido en índice {idx}.")
        listar_peliculas_recursiva(f, idx + 1)
    except UnicodeDecodeError as ude:
        print(f"⚠️ Error al decodificar una línea del archivo: {ude}")
    except RecursionError:
        print("❌ Error: Se alcanzó el límite de recursividad.")
    except Exception as e:
        print(f"❌ Error inesperado al procesar la película en índice {idx}: {e}")

def modificar_pelicula_txt():
    try:
        generos = cargar_generos()
        if not generos:
            print("⚠️ No hay géneros disponibles.")
            return

        patron = input("🔎 Ingrese parte del nombre de la película a modificar: ").strip().lower()
        modificada = False

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
        if not nombre:
            raise ValueError("El nombre de usuario no puede estar vacío.")
        if nombre in users:
            print("El usuario ya existe.")
            return

        password = input("Contraseña para el nuevo usuario: ").strip()
        if not password:
            raise ValueError("La contraseña no puede estar vacía.")

        rol = input("Rol (usuario/admin): ").strip().lower()
        if rol not in ["usuario", "admin"]:
            print("Rol inválido. Se asigna 'usuario' por defecto.")
            rol = "usuario"

        users[nombre] = {"rol": rol, "password": password}
        guardar_usuarios(users)
        print("✅ Usuario creado correctamente.")

    except ValueError as ve:
        print(f"⚠️ Error de validación: {ve}")
    except KeyError as ke:
        print(f"❌ Error con clave: {ke}")
    except TypeError as te:
        print(f"❌ Error de tipo de dato: {te}")
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
    except ValueError as ve:
        print(f"⚠️ Error de validación: {ve}")
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
    except ValueError as ve:
        print(f"⚠️ Error de validación: {ve}")
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

def eliminar_autor_txt():
    try:
        autor = input("🧑‍🎬 Ingresá el nombre del autor/director a eliminar: ").strip()
        if not autor:
            raise ValueError("El nombre del autor no puede estar vacío.")

        peliculas_autor = []
        f = open("peliculas.txt", "r", encoding="utf-8")
        try:
            for linea in f:
                campos = linea.strip().split("|")
                if len(campos) == 4 and campos[1].lower() == autor.lower():
                    peliculas_autor.append(campos)
        finally:
            f.close()

        if not peliculas_autor:
            print("⚠️ No se encontraron películas de ese autor.")
            return

        print(f"\n🎞️ Películas dirigidas por '{autor}':")
        for peli in peliculas_autor:
            print(f"- {peli[0]} ({peli[2]})")

        print("\n¿Qué desea hacer con las películas de este autor?")
        print("1. Eliminar TODAS las películas de este autor")
        print("2. Reasignar a otro director")
        decision = input("Seleccione una opción (1 o 2): ").strip()

        nueva_lista = []
        original = open("peliculas.txt", "r", encoding="utf-8")
        temporal = open("peliculas_temp.txt", "w", encoding="utf-8")

        try:
            for linea in original:
                campos = linea.strip().split("|")
                if len(campos) == 4:
                    if campos[1].lower() == autor.lower():
                        if decision == "1":
                            continue  # No la escribimos, se elimina
                        elif decision == "2":
                            nuevo_autor = input(f"Ingrese nuevo director para '{campos[0]}': ").strip()
                            campos[1] = nuevo_autor
                    temporal.write("|".join(campos) + "\n")
        finally:
            original.close()
            temporal.close()

        os.remove("peliculas.txt")
        os.rename("peliculas_temp.txt", "peliculas.txt")

        print("✅ Operación completada con éxito.")

    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def listar_generos():
    try:
        print("\n🎭 Géneros disponibles en el sistema:")
        vacio = True
        for clave, valor in iterar_generos():
            print(f"{clave}. {valor}")
            vacio = False
        if vacio:
            print("⚠️ No hay géneros cargados en el sistema.")
    except Exception as e:
        print(f"❌ Error al listar géneros: {e}")

def crear_genero():
    try:
        clave = input("🔢 Ingresá el número del nuevo género: ").strip()
        if not clave.isdigit():
            raise ValueError("La clave debe ser un número.")
        
        # Verificar si ya existe
        for k, _ in iterar_generos():
            if k == clave:
                print("⚠️ Esa clave ya está registrada.")
                return
        
        valor = input("🎭 Ingresá el nombre del género: ").strip()
        if not valor:
            raise ValueError("El nombre del género no puede estar vacío.")
        
        # Leer y agregar
        f = open("generos.json", "r", encoding="utf-8")
        try:
            datos = json.load(f)
        finally:
            f.close()
        
        datos[clave] = valor
        
        f = open("generos.json", "w", encoding="utf-8")
        try:
            json.dump(datos, f, ensure_ascii=False, indent=2)
        finally:
            f.close()
        
        print("✅ Género agregado correctamente.")
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        
def eliminar_genero():
    try:
        generos = cargar_generos()

        if not generos:
            print("⚠️ No hay géneros para eliminar.")
            return

        print("\n🎭 Géneros disponibles:")
        for clave, valor in generos.items():
            print(f"{clave}. {valor}")

        clave = input("🔢 Ingresá el número del género a eliminar: ").strip()

        if clave not in generos:
            print("⚠️ Género no encontrado.")
            return

        nombre_genero = generos[clave]

        # Verificar si está en uso
        en_uso = False
        for peli in iterar_peliculas():
            if peli[3] == nombre_genero:
                en_uso = True
                break

        if en_uso:
            print(f"❌ No se puede eliminar el género '{nombre_genero}' porque está en uso en alguna película.")
            return

        confirm = input(f"¿Seguro que querés eliminar el género '{nombre_genero}'? (s/n): ").strip().lower()
        if confirm != "s":
            print("❌ Operación cancelada.")
            return

        del generos[clave]
        guardar_generos(generos)
        print("✅ Género eliminado correctamente.")

    except Exception as e:
        print(f"❌ Error al eliminar género: {e}")

def modificar_genero():
    try:
        generos = cargar_generos()

        if not generos:
            print("⚠️ No hay géneros para modificar.")
            return

        print("\n🎭 Géneros disponibles:")
        for clave, valor in generos.items():
            print(f"{clave}. {valor}")

        clave_a_modificar = input("🔧 Ingresá el número del género a modificar: ").strip()
        if clave_a_modificar not in generos:
            print("⚠️ Clave de género no encontrada.")
            return

        nuevo_nombre = input(f"✏️ Nuevo nombre para '{generos[clave_a_modificar]}': ").strip()
        if not nuevo_nombre:
            raise ValueError("El nombre del género no puede estar vacío.")

        viejo_nombre = generos[clave_a_modificar]
        generos[clave_a_modificar] = nuevo_nombre
        guardar_generos(generos)

        # Actualizar en peliculas.txt
        original = open("peliculas.txt", "r", encoding="utf-8")
        temporal = open("peliculas_temp.txt", "w", encoding="utf-8")

        try:
            for linea in original:
                campos = linea.strip().split("|")
                if len(campos) == 4 and campos[3] == viejo_nombre:
                    campos[3] = nuevo_nombre
                temporal.write("|".join(campos) + "\n")
        finally:
            original.close()
            temporal.close()

        os.remove("peliculas.txt")
        os.rename("peliculas_temp.txt", "peliculas.txt")

        print("✅ Género modificado correctamente.")
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
