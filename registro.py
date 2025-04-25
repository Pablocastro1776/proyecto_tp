# registro.py

def registrarse(users):
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre in users:
        print("Ese usuario ya existe.")
    else:
        users[nombre] = {"rol": "usuario"}
        print("Usuario registrado con éxito.")

def iniciar_sesion(users):
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre in users:
        print(f"Bienvenido, {nombre}.")
        return nombre
    else:
        print("Usuario no encontrado.")
        return None
