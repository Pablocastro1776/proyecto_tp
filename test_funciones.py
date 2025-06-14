import pytest  # type: ignore

#Primera funcion a testear 

def procesar_opcion_usuario(opcion, users):
    if opcion == "1":
        return "crear"
    elif opcion == "2":
        return "modificar"
    elif opcion == "3":
        return "eliminar"
    elif opcion == "4":
        return "listar"
    elif opcion == "0":
        return "salir"
    else:
        raise ValueError("Opción inválida.")
    

#Segunda funcion a testear 

def agregar_pelicula(peliculas, nombre, autor, anio, genero_clave, generos_dict):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not autor.strip():
        raise ValueError("El director no puede estar vacío.")
    if not anio.isdigit() or len(anio) != 4:
        raise ValueError("Ingresá un año válido de 4 cifras.")
    if genero_clave not in generos_dict:
        raise ValueError("Número de género inválido.")

    genero = generos_dict[genero_clave]
    nueva_peli = [nombre.strip(), autor.strip(), anio.strip(), genero]
    peliculas.append(nueva_peli)
    return nueva_peli

def obtener_peliculas_por_defecto():
    return [
        {"titulo": "Titanic", "director": "James Cameron", "anio": "1997", "genero": "Romance"},
        {"titulo": "Inception", "director": "Christopher Nolan", "anio": "2010", "genero": "Ciencia Ficción"},
        {"titulo": "Gladiator", "director": "Ridley Scott", "anio": "2000", "genero": "Acción"}
    ]
#tercera funcion a testear

def pelicula_esta_en_lista(valor_busqueda, campo="titulo", peliculas=None):
    if not isinstance(valor_busqueda, str):
        raise ValueError("El valor de búsqueda debe ser una cadena de texto")
    if campo not in ["titulo", "director"]:
        raise ValueError("El campo debe ser 'titulo' o 'director'")
    
    if peliculas is None:
        peliculas = obtener_peliculas_por_defecto()
    
    for pelicula in peliculas:
        if pelicula[campo].lower() == valor_busqueda.lower():
            return True
    return False

#Primer TEST 
def test_opcion_valida():
     procesar_opcion_usuario("1", []) == "crear"
     procesar_opcion_usuario("0", []) == "salir"

#Segundo TEST

def test_agregar_pelicula_valida():
    peliculas = []
    generos = {'1': 'Acción', '2': 'Drama'}
    resultado = agregar_pelicula(peliculas, "Matrix", "Wachowski", "1999", "1", generos)
    assert resultado == ["Matrix", "Wachowski", "1999", "Acción"]
    assert len(peliculas) == 1

#Tercer Test
def test_pelicula_esta_en_lista():
    assert pelicula_esta_en_lista("Titanic") == True
    assert pelicula_esta_en_lista("avatar") == False
    assert pelicula_esta_en_lista("James Cameron", campo="director") == True
    assert pelicula_esta_en_lista("Quentin Tarantino", campo="director") == False