# main.py

from auth import inicio
from data import cargar_datos, cargar_usuarios, guardar_usuarios, cargar_valoraciones, guardar_valoraciones

if __name__ == "__main__":
    cargar_datos()
    users = cargar_usuarios()
    valoraciones = cargar_valoraciones()

    inicio(users, valoraciones)
 

    guardar_usuarios(users)
    guardar_valoraciones(valoraciones)