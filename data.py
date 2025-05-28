# data.py

import json
import os

# Archivos
USERS_FILE = "users.json"
PELICULAS_FILE = "peliculas.json"
VALORACIONES_FILE = "valoraciones.json"

# Inicialización de datos si los archivos no existen
def cargar_datos():
    if not os.path.exists(USERS_FILE):
        f = open(USERS_FILE, "w")
        try:
            json.dump({"admin": {"rol": "admin", "password": "admin123"}}, f)
        finally:
            f.close()

    if not os.path.exists(PELICULAS_FILE):
        f = open(PELICULAS_FILE, "w")
        try:
            json.dump([
                ["Titanic", "James Cameron", "1997", "Romance"],
                ["Inception", "Christopher Nolan", "2010", "Ciencia Ficción"],
                ["Gladiator", "Ridley Scott", "2000", "Acción"]
            ], f)
        finally:
            f.close()

    if not os.path.exists(VALORACIONES_FILE):
        f = open(VALORACIONES_FILE, "w")
        try:
            json.dump([], f)
        finally:
            f.close()

# Funciones para cargar
def cargar_usuarios():
    f = open(USERS_FILE, "r")
    try:
        return json.load(f)
    finally:
        f.close()

def cargar_peliculas():
    f = open(PELICULAS_FILE, "r")
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

def guardar_peliculas(peliculas):
    f = open(PELICULAS_FILE, "w")
    try:
        json.dump(peliculas, f)
    finally:
        f.close()

def guardar_valoraciones(valoraciones):
    f = open(VALORACIONES_FILE, "w")
    try:
        json.dump(valoraciones, f)
    finally:
        f.close()

generos = {
    "1": "Acción", "2": "Aventura", "3": "Animación", "4": "Biografía", "5": "Ciencia Ficción",
    "6": "Comedia", "7": "Crimen", "8": "Documental", "9": "Drama", "10": "Familia",
    "11": "Fantasía", "12": "Historia", "13": "Musical", "14": "Misterio", "15": "Romance",
    "16": "Suspenso", "17": "Terror", "18": "Guerra", "19": "Western", "20": "Deporte"
}
