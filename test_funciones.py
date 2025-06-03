import pytest  # type: ignore

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

# Primer TEST 
def test_opcion_valida():
    assert procesar_opcion_usuario("1", []) == "crear"
    assert procesar_opcion_usuario("0", []) == "salir"

def test_opcion_invalida():
    with pytest.raises(ValueError):
        procesar_opcion_usuario("9", [])


# Segundo TEST

def test_agregar_pelicula_valida():
    peliculas = []
    generos = {'1': 'Acción', '2': 'Drama'}
    resultado = agregar_pelicula(peliculas, "Matrix", "Wachowski", "1999", "1", generos)
    assert resultado == ["Matrix", "Wachowski", "1999", "Acción"]
    assert len(peliculas) == 1

def test_agregar_pelicula_nombre_vacio():
    peliculas = []
    generos = {'1': 'Acción'}
    with pytest.raises(ValueError, match="nombre no puede estar vacío"):
        agregar_pelicula(peliculas, "", "Nolan", "2010", "1", generos)
