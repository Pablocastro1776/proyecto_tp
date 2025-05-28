# main.py

from auth import inicio
from data import cargar_datos,cargar_usuarios, guardar_usuarios, cargar_peliculas, guardar_peliculas, cargar_valoraciones, guardar_valoraciones

if __name__ == "__main__":
    # Inicializar archivos si no existen
    cargar_datos()

    # Cargar datos desde archivos
    users = cargar_usuarios()
    peliculas = cargar_peliculas()
    valoraciones = cargar_valoraciones()

    inicio(users, peliculas, valoraciones)

    # Guardar todo al salir (backup general)
    guardar_usuarios(users)
    guardar_peliculas(peliculas)
    guardar_valoraciones(valoraciones)
