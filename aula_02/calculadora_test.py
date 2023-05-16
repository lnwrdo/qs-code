import unittest
from calculadora import Calculadora
#python -m unittest calculadora_test.py

class CalculadoraTest(unittest.TestCase):

    def test_soma01(self):
        saida = Calculadora.somar(1, 1)
        esperado = 2
        self.assertEqual(saida, esperado)
    
    #def test_soma02(self):
    #    saida = Calculadora.somar(3, 2)
    #    esperado = 5
    #    self.assertEqual(saida, esperado)
    
    #def test_soma03(self):
    #    saida = Calculadora.somar(5, 9)
    #    esperado = 14
    #    self.assertEqual(saida, esperado)
    
    #teste de subtração
    #def test_sub01(self):
    #    saida = Calculadora.subtrair(1, 1)
    #    esperado = 0
    #    self.assertEqual(saida, esperado)

    #teste de subtração
    #def test_sub02(self):
    #    saida = Calculadora.subtrair(2, 1)
    #    esperado = 1
    #    self.assertEqual(saida, esperado)

    #def test_sub03(self):
    #    saida = Calculadora.subtrair(4, 2)
    #    esperado = 2
    #    self.assertEqual(saida, esperado)
    