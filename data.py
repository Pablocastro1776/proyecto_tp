# data.py

import json
import os

# Archivos
USERS_FILE = "users.json"
PELICULAS_FILE = "peliculas.txt"
VALORACIONES_FILE = "valoraciones.json"
GENEROS_FILE = "generos.json"


# Inicialización de datos si los archivos no existen
def cargar_datos():
    if not os.path.exists(USERS_FILE):
        f = open(USERS_FILE, "w")
        try:
            json.dump({"admin": {"rol": "admin", "password": "admin123"}}, f)
        finally:
            f.close()

    if not os.path.exists(PELICULAS_FILE):
        peliculas_iniciales = [
            ["Titanic", "James Cameron", "1997", "Romance"],
            ["Inception", "Christopher Nolan", "2010", "Ciencia Ficción"],
            ["Gladiator", "Ridley Scott", "2000", "Acción"]
        ]
        f = open(PELICULAS_FILE, "w", encoding="utf-8")
        try:
            for peli in peliculas_iniciales:
                f.write("|".join(peli) + "\n")
        finally:
            f.close()

    if not os.path.exists(VALORACIONES_FILE):
        f = open(VALORACIONES_FILE, "w")
        try:
            json.dump([], f)
        finally:
            f.close()

    if not os.path.exists(GENEROS_FILE):
        generos_por_defecto = {
            "1": "Acción", "2": "Aventura", "3": "Animación", "4": "Biografía",
            "5": "Ciencia Ficción", "6": "Comedia", "7": "Crimen", "8": "Documental",
            "9": "Drama", "10": "Familia", "11": "Fantasía", "12": "Historia",
            "13": "Musical", "14": "Misterio", "15": "Romance", "16": "Suspenso",
            "17": "Terror", "18": "Guerra", "19": "Western", "20": "Deporte"
        }
        f = open(GENEROS_FILE, "w", encoding="utf-8")
        try:
            json.dump(generos_por_defecto, f, ensure_ascii=False, indent=2)
        finally:
            f.close()
            
# Funciones para cargar
def cargar_usuarios():
    f = open(USERS_FILE, "r")
    try:
        return json.load(f)
    finally:
        f.close()

def buscar_pelicula_por_nombre(nombre_buscado):
    f = open("peliculas.txt", "r", encoding="utf-8")
    try:
        for linea in f:
            campos = linea.strip().split("|")
            if len(campos) == 4 and nombre_buscado.lower() in campos[0].lower():
                print(f"Encontrada: {campos}")
                return
    finally:
        f.close()


def cargar_generos():
    f = open(GENEROS_FILE, "r", encoding="utf-8")
    try:
        return json.load(f)
    finally:
        f.close()


def cargar_valoraciones():
    f = open(VALORACIONES_FILE, "r")
    try:
        return json.load(f)
    finally:
        f.close()

# Funciones para guardar
def guardar_usuarios(users):
    f = open(USERS_FILE, "w")
    try:
        json.dump(users, f)
    finally:
        f.close()

def guardar_valoraciones(valoraciones):
    f = open(VALORACIONES_FILE, "w")
    try:
        json.dump(valoraciones, f)
    finally:
        f.close()


def guardar_generos(diccionario_generos):
    f = open(GENEROS_FILE, "w", encoding="utf-8")
    try:
        json.dump(diccionario_generos, f, ensure_ascii=False, indent=2)
    finally:
        f.close()

#Funciones para iterar
def iterar_peliculas():
    try:
        f = open("peliculas.txt", "r", encoding="utf-8")
        return _leer_lineas_recursivo(f)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return []
        
def _leer_lineas_recursivo(f, acumulador=None):
    if acumulador is None:
        acumulador = []

    linea = f.readline()
    if not linea:
        f.close()
        if not acumulador:
            print("⚠️ Ya no hay más películas almacenadas.")
        return acumulador

    campos = linea.strip().split("|")
    if len(campos) == 4:
        acumulador.append(campos)

    return _leer_lineas_recursivo(f, acumulador)

def iterar_valoraciones():
    f = open("valoraciones.json", "r")
    try:
        datos = json.load(f)
        for val in datos:
            yield val
    finally:
        f.close()
        
def iterar_generos():
    f = open(GENEROS_FILE, "r", encoding="utf-8")
    try:
        for clave, valor in json.load(f).items():
            yield clave, valor
    finally:
        f.close()

