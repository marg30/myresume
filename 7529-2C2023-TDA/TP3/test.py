import unittest
from main import verificadorSolucion, solucionBacktracking, solucionProgramacionLineal, aproximacionGreedy

EjemplosSubsetsSolucionesUnicas = [[{'1','2'}, {'1','3'}, {'2','3'}, {'2','3'}, {'2','4'}, {'2','6'}, {'3','4'}, {'3','5'}, {'4','5'}, {'4','6'}],
                                   [{'1','2'}, {'2','3'}, {'3','4'}, {'4','5'}]]
EjemplosSolucionesSolucionesUnicas = [{'2','3','4'}, {'2','4'}]

EjemplosSubsetsSolucionesMultiples = [[{'2','3'}, {'1','3','4','6'}, {'1','2','4','5'}, {'2','3','5','6'}, {'3','4'}, {'2','4'}],
                                      [{'1','2','3','4'}, {'2','5','6'}, {'3','4','5'}, {'1','4','6'}, {'2','3'}, {'1','5'}]]
EjemplosSolucionesSolucionesMultiples = [{'2','3'}, {'1','3','5'}]

class TestSum(unittest.TestCase):
    
    def testVacioVerificador(self):
        subconjuntos = []
        solucionPropuesta = {}
        self.assertTrue(verificadorSolucion(subconjuntos, solucionPropuesta))

    def testTodosLosValoresVerificador(self):
        todosLosSubsets = EjemplosSubsetsSolucionesUnicas.copy()
        todosLosSubsets += EjemplosSubsetsSolucionesMultiples
        todasLasSoluciones = EjemplosSolucionesSolucionesUnicas.copy()
        todasLasSoluciones += EjemplosSolucionesSolucionesMultiples
        for i in range(0, len(todosLosSubsets)):
            self.assertTrue(verificadorSolucion(todosLosSubsets[i], todasLasSoluciones[i]))

    def testValoresSolucionesUnicasBacktracking(self):
        for i in range(0, len(EjemplosSubsetsSolucionesUnicas)):
            self.assertEqual(solucionBacktracking(EjemplosSubsetsSolucionesUnicas[i]), EjemplosSolucionesSolucionesUnicas[i])

    def testValoresSolucionesMultiplesBacktraking(self):
        for i in range(0, len(EjemplosSubsetsSolucionesMultiples)):
            self.assertTrue(verificadorSolucion(EjemplosSubsetsSolucionesMultiples[i], solucionBacktracking(EjemplosSubsetsSolucionesMultiples[i])))

    def testValoresSolucionesUnicasProgramacionLineal(self):
        for i in range(0, len(EjemplosSubsetsSolucionesUnicas)):
            self.assertEqual(solucionProgramacionLineal(EjemplosSubsetsSolucionesUnicas[i], False), EjemplosSolucionesSolucionesUnicas[i])

    def testValoresSolucionesMultiplesProgramacionLineal(self):
        for i in range(0, len(EjemplosSubsetsSolucionesMultiples)):
            self.assertTrue(verificadorSolucion(EjemplosSubsetsSolucionesMultiples[i], solucionProgramacionLineal(EjemplosSubsetsSolucionesMultiples[i], False)))

    def testValoresSolucionesUnicasGreedy(self):
        for i in range(0, len(EjemplosSubsetsSolucionesUnicas)):
            self.assertTrue(verificadorSolucion(EjemplosSubsetsSolucionesUnicas[i], aproximacionGreedy(EjemplosSubsetsSolucionesUnicas[i])))

    def testValoresSolucionesMultiplesGreedy(self):
        for i in range(0, len(EjemplosSubsetsSolucionesMultiples)):
            self.assertTrue(verificadorSolucion(EjemplosSubsetsSolucionesMultiples[i], aproximacionGreedy(EjemplosSubsetsSolucionesMultiples[i])))

    def testValoresSolucionesUnicasProgramacionLinealRelajada(self):
        for i in range(0, len(EjemplosSubsetsSolucionesUnicas)):
            self.assertTrue(verificadorSolucion(EjemplosSubsetsSolucionesUnicas[i], solucionProgramacionLineal(EjemplosSubsetsSolucionesUnicas[i], True)))

    def testValoresSolucionesMultiplesProgramacionLinealRelajada(self):
        for i in range(0, len(EjemplosSubsetsSolucionesMultiples)):
            self.assertTrue(verificadorSolucion(EjemplosSubsetsSolucionesMultiples[i], solucionProgramacionLineal(EjemplosSubsetsSolucionesMultiples[i], True)))


if __name__ == '__main__':
    unittest.main()
