# -*- coding: utf-8 -*-
import unittest
import time
from datetime import datetime

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
    def test_fecha_hito_anterior_a_ahora(self):
        fecha_hito = datetime.strptime(str(self.hitos.uno(0)["fecha"]), "%d/%m/%Y")
        fecha_actual=datetime.now()
        self.assertLessEqual( fecha_hito, fecha_actual)

if __name__ == '__main__':
    unittest.main()
