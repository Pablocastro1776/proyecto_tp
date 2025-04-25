# auth.py

def inicio(users, peliculas, valoraciones):
    from menu import menu
    from registro import registrarse, iniciar_sesion
    usuario_actual = None
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarse(users)
        elif opcion == "2":
            usuario_actual = iniciar_sesion(users)
            if usuario_actual:
                menu(usuario_actual, users, peliculas, valoraciones)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
