def ordenar_peliculas_por_anio(peliculas):
    peliculas_ordenadas = sorted(peliculas, key=lambda x: x[2])
    print("\nPelículas ordenadas por año:")
    for peli in peliculas_ordenadas:
        print(f"- {peli[0]} ({peli[2]}) - Director: {peli[1]}")

def peliculas_del_director(peliculas):
    nombre_director = input("Nombre del director: ")
    lista = [p[0] for p in peliculas if p[1].lower() == nombre_director.lower()]
    if lista:
        print(f"Películas de {nombre_director}:")
        for titulo in lista:
            print(f"- {titulo}")
    else:
        print("No se encontraron películas de ese director.")

def mostrar_info_basica(peliculas):
    print("\nListado básico de películas (usando tuplas):")
    for peli in peliculas:
        info = (peli[0], peli[2])  # (nombre, año)
        print(f"Título: {info[0]}, Año: {info[1]}")

def mostrar_generos_unicos(peliculas):
    generos = {peli[3] for peli in peliculas}  # conjunto (set)
    print("Géneros únicos en la base de datos:")
    for genero in sorted(generos):
        print(f"- {genero}")
