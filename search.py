# search.py
import re
from data import iterar_generos
import json

def iterar_peliculas():
    f = open("peliculas.txt", "r", encoding="utf-8")
    try:
        for linea in f:
            campos = linea.strip().split("|")
            if len(campos) == 4:
                yield campos
    finally:
        f.close()

def iterar_valoraciones():
    f = open("valoraciones.json", "r")
    try:
        datos = json.load(f)
        for val in datos:
            yield val  # val = [usuario, pelicula, puntuacion]
    finally:
        f.close()

def buscar_pelicula():
    try:
        patron = input("🔎 Ingresá parte del nombre de la película: ").strip()
        if not patron:
            raise ValueError("Debés ingresar al menos una letra.")
        regex = re.compile(f".*{patron}.*", re.IGNORECASE)
        coincidencias = []

        for peli in iterar_peliculas():
            if regex.search(peli[0]):
                coincidencias.append(peli)

        if coincidencias:
            print("📋 Coincidencias:")
            for idx, peli in enumerate(coincidencias, start=1):
                print(f"{idx}. {peli[0]} - Director: {peli[1]}")
        else:
            print("⚠️ No se encontraron coincidencias.")
    except ValueError as ve:
        print(f"⚠️ Error: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def buscar_por_autor():
    try:
        autor = input("🧑‍🎬 Ingresá parte del nombre del director: ").strip()
        if not autor:
            raise ValueError("Ingresá un nombre válido.")
        regex = re.compile(f".*{autor}.*", re.IGNORECASE)
        encontrados = []

        for peli in iterar_peliculas():
            if regex.search(peli[1]):
                encontrados.append(peli)

        if encontrados:
            print("🎬 Películas encontradas:")
            for peli in encontrados:
                print(f"- {peli[0]} ({peli[2]}) - Género: {peli[3]}")
        else:
            print("⚠️ No se encontraron películas de ese autor.")
    except Exception as e:
        print(f"❌ Error al buscar por autor: {e}")


def buscar_por_genero():
    try:
        print("🎭 Seleccione un género:")
        generos_dict = {}  # Para mapear clave -> valor
        for clave, valor in iterar_generos():
            print(f"{clave}. {valor}")
            generos_dict[clave] = valor

        opcion = input("Número de género: ").strip()
        if opcion not in generos_dict:
            raise ValueError("Género inválido.")

        genero_objetivo = generos_dict[opcion]
        encontrados = []

        for peli in iterar_peliculas():
            if peli[3] == genero_objetivo:
                encontrados.append(peli)

        if encontrados:
            print(f"\n🎬 Películas del género {genero_objetivo}:")
            for peli in encontrados:
                print(f"- {peli[0]} ({peli[2]}) - Director: {peli[1]}")
        else:
            print("⚠️ No se encontraron películas en ese género.")
    except Exception as e:
        print(f"❌ Error en búsqueda por género: {e}")
