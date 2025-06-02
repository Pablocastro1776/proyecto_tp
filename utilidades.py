from data import generos

def ordenar_peliculas_por_anio():
    try:
        peliculas_validas = sorted(
            (p for p in iterar_peliculas() if p[2].isdigit()),
            key=lambda x: x[2]
        )
        print("\n📅 Películas ordenadas por año:")
        for peli in peliculas_validas:
            print(f"- {peli[0]} ({peli[2]}) - Director: {peli[1]}")
    except Exception as e:
        print(f"❌ Error al ordenar películas: {e}")


def peliculas_del_director():
    try:
        nombre_director = input("🎬 Nombre del director: ").strip().lower()
        if not nombre_director:
            raise ValueError("Debe ingresar un nombre.")

        encontrado = False
        print(f"\nPelículas de {nombre_director.title()}:")
        for peli in iterar_peliculas():
            if peli[1].lower() == nombre_director:
                print(f"- {peli[0]}")
                encontrado = True

        if not encontrado:
            print("⚠️ No se encontraron películas de ese director.")
    except Exception as e:
        print(f"❌ Error: {e}")


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

def iterar_peliculas():
    f = open("peliculas.txt", "r", encoding="utf-8")
    try:
        for linea in f:
            campos = linea.strip().split("|")
            if len(campos) == 4:
                yield campos
    finally:
        f.close()
