users = {}
movies = {"Inception": "Sci-Fi", "Titanic": "Romance", "The Matrix": "Action"}

def menu():
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Buscar Película")
        print("4. Ver Película")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrarse()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            buscar_pelicula()
        elif opcion == "4":
            ver_pelicula()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

def registrarse():
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in users:
        print("El usuario ya existe.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        users[usuario] = contrasena
        print("Registro exitoso.")

def iniciar_sesion():
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in users and users[usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

def buscar_pelicula():
    pelicula = input("Ingrese el nombre de la película: ")
    if pelicula in movies:
        print(f"{pelicula} encontrada. Género: {movies[pelicula]}")
    else:
        print("Película no encontrada.")

def ver_pelicula():
    pelicula = input("Ingrese el nombre de la película que desea ver: ")
    if pelicula in movies:
        print(f"Reproduciendo {pelicula}...")
    else:
        print("Película no encontrada.")

menu()
