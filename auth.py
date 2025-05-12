# auth.py

def inicio(users, peliculas, valoraciones):
    from menu import menu
    from registro import registrarse, iniciar_sesion
    usuario_actual = None
    while True:
        print("\n" + "=" * 50)
        print("🎬  INICIO DE SESIÓN - SISTEMA DE PELÍCULAS".center(50))
        print("=" * 50)
        print("1. Crear nueva cuenta")
        print("2. Iniciar sesión")
        print("3. Salir del sistema")
        print("-" * 50)
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
