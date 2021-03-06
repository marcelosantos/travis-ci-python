from unittest import TestCase
from source_code.figura_geometrica import FiguraGeometrica

# O nome da classe deve iniciar com a palavra Test
class TestFiguraGeometrico(TestCase):
    
    # Serve para incializar variavei que usaremos
    # globalmente nos testes
    def setUp(self):
        TestCase.setUp(self)
        self.fig = FiguraGeometrica()

    # Retorna uma NotImplementedError
    # O nome do metodo deve comecar com test
    def test_get_area(self):
        self.assertRaises(NotImplementedError, self.fig.get_area)

    # Retorna uma NotImplementedError
    # O nome do metodo deve comecar com test
    def test_get_perimetro(self):
        self.assertRaises(NotImplementedError, self.fig.get_perimetro)
        
