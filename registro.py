# registro.py

from data import guardar_usuarios

def registrarse(users):
    try:
        nombre = input("Ingrese su nombre de usuario: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if nombre in users:
            print("Ese usuario ya existe.")
        else:
            password = input("Ingrese una contraseña: ").strip()
            if not password:
                raise ValueError("La contraseña no puede estar vacía.")
            users[nombre] = {"rol": "usuario", "password": password}
            guardar_usuarios(users)
            print("✅ Usuario registrado con éxito.")
    except ValueError as e:
        print(f"⚠️ Error: {e}")
    except Exception as e:
        print(f"⚠️ Error inesperado al registrar: {e}")


def iniciar_sesion(users):
    try:
        nombre = input("Ingrese su nombre de usuario: ").strip()
        if nombre not in users:
            print("Usuario no encontrado.")
            return None

        password = input("Ingrese su contraseña: ").strip()
        if users[nombre]["password"] == password:
            print(f"Bienvenido, {nombre}.")
            return nombre
        else:
            print("Contraseña incorrecta.")
            return None
    except Exception as e:
        print(f"⚠️ Error durante el inicio de sesión: {e}")
        return None
