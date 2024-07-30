import unittest
from main import tiempo_minimo

Ejemplos_tiempos = [[(96,120), (78, 150), (26, 64)],
                    [(96,120), (78, 230), (26, 64)],
                    [(96,96), (78, 78), (26, 26)],
                    [(96,120), (77,48), (25,30), (1, 5)],
                    [(96,120), (77,48), (25,30), (1, 5), (45,1)],
                    [(96,120), (78, 150), (26, 64), (77,48), (25,30), (1, 5)],
                    [(96,120), (78, 150), (26, 64), (77,48), (25,30), (1, 5), (9,60)],
                    [(96,48), (78, 39), (26, 13),(30, 15),(76, 38),(100, 50),(150, 75),(56, 25)],
                    [(96,48), (78, 39), (26, 13),(30, 15),(76, 38),(100, 50),(150, 75),(56, 25), (23, 46)],
                    [(96,48), (78, 39), (26, 13),(30, 15),(76, 38),(100, 50),(150, 75),(56, 25), (23, 46), (1,2)]]

Ejemplos_soluciones = [294, 308, 252, 228, 245, 332, 341, 625, 648, 648]

class TestSum(unittest.TestCase):

    def test_vacio(self):
        tiempos = []
        resultado = 0
        self.assertEqual(tiempo_minimo(tiempos), resultado)

    def test_valores(self):
        for i in range(len(Ejemplos_tiempos)):
            self.assertEqual(tiempo_minimo(Ejemplos_tiempos[i]), Ejemplos_soluciones[i])

if __name__ == '__main__':
    unittest.main()
