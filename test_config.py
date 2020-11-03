import unittest

from HitosIV.config import Config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.config,Config, "Objeto creado correctamente")

    def test_should_have_port( self):
        self.assertIsInstance(self.config.port, int, "El puerto es un entero")
        self.assertGreater(self.config.port, 3, "El número de hitos es mayor que 0")

if __name__ == '__main__':
    unittest.main()
