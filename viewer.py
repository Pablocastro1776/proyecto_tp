# viewer.py
import re
from data import guardar_valoraciones
    
def ver_pelicula(valoraciones, usuario_actual):
    try:
        patron = input("🎬 Escribí el nombre (o parte) de la película que querés ver: ").strip()
        if not patron:
            raise ValueError("Debés ingresar al menos una palabra.")

        regex = re.compile(f".*{patron}.*", re.IGNORECASE)
        coincidencias = []

        f = open("peliculas.txt", "r", encoding="utf-8")
        try:
            for linea in f:
                campos = linea.strip().split("|")
                if len(campos) == 4 and regex.search(campos[0]):
                    coincidencias.append(campos)
        finally:
            f.close()

        if not coincidencias:
            print("⚠️ No se encontraron películas.")
            return

        print("¿Cuál de estas querés ver?")
        for idx, peli in enumerate(coincidencias, start=1):
            print(f"{idx}. {peli[0]} - {peli[1]} ({peli[2]}) - Género: {peli[3]}")

        seleccion = input("Seleccioná el número (o enter para cancelar): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(coincidencias):
                peli = coincidencias[seleccion - 1]
                print(f"🎥 Reproduciendo '{peli[0]}' de {peli[1]} ({peli[2]}) - Género: {peli[3]}")
                while True:
                    try:
                        puntaje = int(input("⭐ ¿Qué puntaje le das del 1 al 5? "))
                        if 1 <= puntaje <= 5:
                            break
                        else:
                            print("⚠️ Debe ser un número entre 1 y 5.")
                    except ValueError:
                        print("⚠️ Ingresá un número válido.")
                valoraciones.append([usuario_actual, peli[0], str(puntaje)])
                print("¡Gracias por valorar la película!")
    except Exception as e:
        print(f"❌ Error: {e}")


def ver_puntuacion_pelicula():
    try:
        nombre = input("🎬 Ingresá parte del nombre de la película: ").strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        regex = re.compile(f".*{nombre}.*", re.IGNORECASE)
        coincidencias = []

        for peli in iterar_peliculas():
            if regex.search(peli[0]):
                coincidencias.append(peli)

        if not coincidencias:
            print("⚠️ No se encontraron coincidencias.")
            return

        for idx, peli in enumerate(coincidencias, start=1):
            print(f"{idx}. {peli[0]} - Director: {peli[1]}")

        seleccion = input("Seleccione el número: ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(coincidencias):
                nombre_peli = coincidencias[seleccion - 1][0]
                total = 0
                cantidad = 0
                for val in iterar_valoraciones():
                    if val[1] == nombre_peli:
                        total += int(val[2])
                        cantidad += 1
                if cantidad > 0:
                    promedio = total / cantidad
                    print(f"⭐ Promedio: {promedio:.2f} basado en {cantidad} valoraciones.")
                else:
                    print("⚠️ La película no tiene valoraciones aún.")
    except Exception as e:
        print(f"❌ Error al mostrar puntuación: {e}")

def ver_valoraciones_personales(valoraciones, usuario_actual):
    try:
        print(f"\nValoraciones de {usuario_actual}:")
        encontrado = False
        for val in valoraciones:
            if val[0] == usuario_actual:
                print(f"Película: {val[1]} | Puntaje: {val[2]}")
                encontrado = True
        if not encontrado:
            print("No has valorado ninguna película todavía.")
    except Exception as e:
        print(f"⚠️ Error al mostrar tus valoraciones: {e}")
