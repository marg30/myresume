import unittest
from main import obtenerGananciaMaxima

EjemplosTamanos = [1, 1, 2, 7, 7, 10, 25]
EjemplosEsfuerzos = [[10], [5], [2, 15], [10 , 15, 17, 16, 1, 74, 14], [90, 72, 54, 28, 39, 87, 62], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [54, 12, 87, 34, 68, 91, 42, 7, 15, 29, 56, 98, 5, 71, 23, 77, 39, 2, 63, 84, 9, 46, 60, 20, 73]]
EjemplosEnergias = [[5], [10], [10, 2], [10, 2, 2, 2, 2, 2, 2], [85, 70, 56, 44, 30, 24, 15], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [96, 94, 90, 88, 81, 78, 72, 70, 67, 65, 59, 52, 49, 47, 41, 33, 30, 26, 25, 17, 14, 11, 8, 6, 3]]
EjemplosSoluciones = [5, 5, 10, 34, 384, 45, 1127]

class TestSum(unittest.TestCase):
    
    def test_vacio(self):
        tamano = 0
        esfuerzos = []
        energias = []
        resultado = 0
        self.assertEqual(obtenerGananciaMaxima(tamano, esfuerzos, energias), resultado)

    def test_valores(self):
        for i in range(0, len(EjemplosTamanos)):
            self.assertEqual(obtenerGananciaMaxima(EjemplosTamanos[i], EjemplosEsfuerzos[i], EjemplosEnergias[i]), EjemplosSoluciones[i])

if __name__ == '__main__':
    unittest.main()
