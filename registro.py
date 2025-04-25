# registro.py

def registrarse(users):
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre in users:
        print("Ese usuario ya existe.")
    else:
        password = input("Ingrese una contraseña: ")
        users[nombre] = {"rol": "usuario", "password": password}
        print("Usuario registrado con éxito.")

def iniciar_sesion(users):
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre in users:
        password = input("Ingrese su contraseña: ")
        if users[nombre]["password"] == password:
            print(f"Bienvenido, {nombre}.")
            return nombre
        else:
            print("Contraseña incorrecta.")
            return None
    else:
        print("Usuario no encontrado.")
        return None
