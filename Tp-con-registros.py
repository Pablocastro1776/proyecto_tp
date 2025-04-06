users = {"admin": "admin"}
peliculas = [
    ["Inception", "Christopher Nolan", "2010", "Sci-Fi"],
    ["Titanic", "James Cameron", "1997", "Romance"],
    ["The Matrix", "Lana Wachowski y Lilly Wachowski", "1999", "Acción"]
]
usuario_actual = None

def inicio():
    global usuario_actual
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarse()
        elif opcion == "2":
            if iniciar_sesion():
                menu()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

def menu():
    while True:
        print("\n1. Buscar Película")
        print("2. Ver Película")
        if usuario_actual == "admin":
            print("3. Agregar Película")
            print("4. Cerrar Sesión")
        else:
            print("3. Cerrar Sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar_pelicula()
        elif opcion == "2":
            ver_pelicula()
        elif opcion == "3" and usuario_actual == "admin":
            agregar_pelicula()
        elif opcion == "3" or (opcion == "4" and usuario_actual == "admin"):
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")

def registrarse():
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in users:
        print("El usuario ya existe.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        users[usuario] = contrasena
        print("Registro exitoso.")

def iniciar_sesion():
    global usuario_actual
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in users and users[usuario] == contrasena:
        print("Inicio de sesión exitoso.")
        usuario_actual = usuario
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False

def buscar_pelicula():
    nombre = input("Ingrese el nombre de la película: ")
    encontrada = False
    for peli in peliculas:
        if peli[0].lower() == nombre.lower():
            print(f"\nPelícula encontrada:")
            print(f"Nombre: {peli[0]}")
            print(f"Autor: {peli[1]}")
            print(f"Año: {peli[2]}")
            print(f"Género: {peli[3]}")
            encontrada = True
            break
    if not encontrada:
        print("Película no encontrada.")

def ver_pelicula():
    nombre = input("Ingrese el nombre de la película que desea ver: ")
    for peli in peliculas:
        if peli[0].lower() == nombre.lower():
            print(f"Reproduciendo {peli[0]}...")
            return
    print("Película no encontrada.")

def agregar_pelicula():
    nombre = input("Ingrese el nombre de la película: ")
    autor = input("Ingrese el autor de la película: ")
    anio = input("Ingrese el año de salida: ")
    genero = input("Ingrese el género: ")
    peliculas.append([nombre, autor, anio, genero])
    print("Película agregada exitosamente.")

inicio()
