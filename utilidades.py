#utilidades.py
import re
from data import iterar_generos,iterar_peliculas

def ordenar_peliculas_por_anio():
    try:
        peliculas = iterar_peliculas()
        if not peliculas:
            return  

        peliculas_validas = sorted(
            (p for p in peliculas if p[2].isdigit()),
            key=lambda x: x[2]
        )
        print("\n📅 Películas ordenadas por año:")
        for peli in peliculas_validas:
            print(f"Título: {peli[0]}, Director: {peli[1]}, Año: {peli[2]}, Género: {peli[3]}")
    except Exception as e:
        print(f"❌ Error al ordenar películas: {e}")

def peliculas_del_director():
    try:
        nombre_director = input("🎬 Ingresá parte del nombre del director: ").strip()
        if not nombre_director:
            raise ValueError("Debe ingresar un nombre.")

        regex = re.compile(f".*{nombre_director}.*", re.IGNORECASE)

        directores_encontrados = set()
        peliculas = []

        for peli in iterar_peliculas():
            if regex.search(peli[1]):
                directores_encontrados.add(peli[1])
                peliculas.append(peli)

        if not directores_encontrados:
            print("⚠️ No se encontraron directores que coincidan.")
            return

        directores_encontrados = sorted(directores_encontrados)

        # Si hay más de un director, pedimos al usuario que elija uno
        if len(directores_encontrados) > 1:
            print("\n🔍 Se encontraron varios directores que coinciden:")
            for idx, d in enumerate(directores_encontrados, 1):
                print(f"{idx}. {d}")
            seleccion = input("Seleccione el número del director que buscaba (o Enter para cancelar): ").strip()
            if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(directores_encontrados)):
                print("❌ Búsqueda cancelada.")
                return
            director_final = directores_encontrados[int(seleccion) - 1]
        else:
            director_final = directores_encontrados[0]
            confirmar = input(f"¿Te referís a '{director_final}'? (s/n): ").strip().lower()
            if confirmar != "s":
                print("❌ Búsqueda cancelada.")
                return

        print(f"\n🎞️ Películas dirigidas por '{director_final}':")
        for peli in peliculas:
            if peli[1] == director_final:
                print(f"Título: {peli[0]}, Año: {peli[2]}, Género: {peli[3]}")
                
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def mostrar_info_basica():
    try:
        print("\n🗂️ Listado básico de películas:")
        for peli in iterar_peliculas():
            print(f"Título: {peli[0]}, Año: {peli[2]}")
    except Exception as e:
        print(f"❌ Error al mostrar información: {e}")


def mostrar_generos_unicos():
    try:
        generos_set = set()
        for peli in iterar_peliculas():
            generos_set.add(peli[3])

        print("\n🎭 Géneros únicos encontrados:")
        for genero in sorted(generos_set):
            print(f"- {genero}")
    except Exception as e:
        print(f"❌ Error al listar géneros únicos: {e}")


def top_3_peliculas(valoraciones):
    if not valoraciones:
        print("Todavía no hay valoraciones registradas.")
        return

    promedios = {}

    for val in valoraciones:
        nombre = val[1]
        puntaje = int(val[2])
        if nombre not in promedios:
            promedios[nombre] = [0, 0]
        promedios[nombre][0] += puntaje
        promedios[nombre][1] += 1

    lista_promedios = []
    for nombre, datos in promedios.items():
        promedio = datos[0] / datos[1]
        lista_promedios.append((nombre, promedio))

    lista_ordenada = sorted(lista_promedios, key=lambda x: x[1], reverse=True)
    top_3 = lista_ordenada[:3]

    print("\n🎖️ Top 3 películas mejor valoradas:")
    for nombre, promedio in top_3:
        print(f"- {nombre}: {promedio:.2f} puntos")

"""def iterar_peliculas(f=None):
    if f is None:
        f = open("peliculas.txt", "r", encoding="utf-8")

    try:
        linea = f.readline()
        if not linea:
            return 
        campos = linea.strip().split("|")
        if len(campos) == 4:
            print(f"Título: {campos[0]}, Director: {campos[1]}, Año: {campos[2]}, Género: {campos[3]}")
        iterar_peliculas(f)
    finally:
        if f and not f.closed:
            f.close()
"""