import unittest
from HitosIV import HitosIV


class TestHitosIV(unittest.TestCase):

    def setUp(self):
        self.hitos = HitosIV()
    
    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.hitos,HitosIV, "Objeto creado correctamente")

    def test_should_have_hitos_stored_correctly( self):
        self.assertIsInstance( self.hitos.todos_hitos(), dict, "El objeto hitos contiene un diccionario")
        self.assertEqual(self.hitos.cuantos(), 2, "El número de hitos es incorrecto")
            
    def test_should_return_hitos_correctly_and_raise_error(self):
        self.assertEqual( self.hitos.uno(0)["file"],  "0.Repositorio" )
        with self.assertRaises(IndexError):
            zape = self.hitos.uno(-1)

        with self.assertRaises(IndexError):
            zipi = self.hitos.uno(99)

     
if __name__ == '__main__':
    unittest.main()
