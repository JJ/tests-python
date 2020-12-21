
from HitosIV.core import HitosIV

hitos = HitosIV() # Arrange

def test_should_initialize_object_OK():
    assert type(hitos) is HitosIV, "No se han podido inicializar los hitos"

def test_should_have_hitos_stored_correctly():
    assert type(hitos.todos_hitos()) is dict, "hitos no contiene un diccionario"
    assert hitos.cuantos() is 2, "El número de hitos es incorrecto"

def test_should_return_hitos_correctly_and_raise_error():
    assert hitos.uno(0)["file"] ==  "0.Repositorio"
    try:
        zipi = hitos.uno(-1)
    except Exception as fallo:
        assert type(fallo) is IndexError

    try:
        zipi = hitos.uno(99)
    except Exception as fallo:
        assert type(fallo) is IndexError

