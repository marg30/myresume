import random
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from main import solucionBacktracking, solucionProgramacionLineal, aproximacionGreedy
from test import EjemplosSubsetsSolucionesUnicas, EjemplosSolucionesSolucionesUnicas, EjemplosSubsetsSolucionesMultiples, EjemplosSolucionesSolucionesMultiples

def graficoEjemplos(algoritmo):
    resultados = []
    t_inicio = time.time()
    
    todosLosSubsets = EjemplosSubsetsSolucionesUnicas.copy()
    todosLosSubsets += EjemplosSubsetsSolucionesMultiples    

    for i in range(0, len(todosLosSubsets)):
        inicio = time.time()
        algoritmo(todosLosSubsets[i])
        resultados.append(time.time() - inicio)
    
    print(f'Tiempo total tardado: {time.time() - t_inicio} segundos')

    plt.figure(figsize=(8, 6))
    plt.grid(True)

    plt.scatter([len(ejemplo) for ejemplo in todosLosSubsets], resultados, label='Algoritmo', color='b')

    plt.xlabel('Cantidad de pedidos de prensa')
    plt.ylabel('Tiempo consumido [s]')
    plt.title('Tiempo transcurrido para obtener la el conjunto mínimo para contentar a toda la prensa')

    plt.xlim(0, 26)
    plt.show()

#a es la cantidad de elementos que se desea que tenga el set A. b es la cantidad de subsets B que se desea que se generen. j y p son la cantidad maxima y minima de elementos que puede tener un subset, respectivamente.
def generarValoresAleatorios(a=42, b=5, j=7, p=3):
  subsets = []
  A = set(range(1, a+1))
  for i in range(0, b):
    subset = set()
    for q in range(0, random.randint(p, j)):
      subset.add(str(random.randint(1, a)))
    subsets.append(subset)
  return subsets

def graficoValoresAleatorios(algoritmo, maximo = 100, paso = 1):
    tamanoElementos = range(1, maximo, paso)
    resultados = []
    t_inicio = time.time()
    for i in tamanoElementos:
        subsets = generarValoresAleatorios(i*3, i, i*2, 1)
        inicio = time.time()
        algoritmo(subsets)
        resultados.append(time.time() - inicio)

    print(f'Tiempo total tardado: {time.time() - t_inicio} segundos')

    plt.figure(figsize=(8, 6))
    plt.grid(True)

    plt.plot(tamanoElementos, resultados, label='Algoritmo', color='b')


    plt.xlabel('Cantidad de pedidos de prensa')
    plt.ylabel('Tiempo consumido [s]')
    plt.title('Tiempo transcurrido para obtener la el conjunto mínimo para contentar a toda la prensa')

    plt.show()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "-p":
            algoritmo = lambda subsets: solucionProgramacionLineal(subsets, False)
            graficoEjemplos(algoritmo)
        elif sys.argv[1] == "-b":
            algoritmo = lambda subsets: solucionBacktracking(subsets)
            graficoEjemplos(algoritmo)
        elif sys.argv[1] == "-g":
            graficoEjemplos(aproximacionGreedy)
        elif sys.argv[1] == "-q":
            algoritmo = lambda subsets: solucionProgramacionLineal(subsets, True)
            graficoEjemplos(algoritmo)
        else:
            print("Comando no reconocido")
    elif len(sys.argv) >= 3:
        if sys.argv[1] == '-r':
            if sys.argv[2] == "-p":
                algoritmo = lambda subsets: solucionProgramacionLineal(subsets, False)
                graficoValoresAleatorios(algoritmo, (int(sys.argv[3])+1 if len(sys.argv) > 3 else 100), (int(sys.argv[4]) if len(sys.argv) > 4 else 1))
            elif sys.argv[2] == "-b":
                algoritmo = lambda subsets: solucionBacktracking(subsets)
                graficoValoresAleatorios(algoritmo, (int(sys.argv[3])+1 if len(sys.argv) > 3 else 25), (int(sys.argv[4]) if len(sys.argv) > 4 else 1))
            elif sys.argv[2] == "-g":
                graficoValoresAleatorios(aproximacionGreedy, (int(sys.argv[3])+1 if len(sys.argv) > 3 else 100), (int(sys.argv[4]) if len(sys.argv) > 4 else 1))
            elif sys.argv[2] == "-q":
                algoritmo = lambda subsets: solucionProgramacionLineal(subsets, True)
                graficoValoresAleatorios(algoritmo, (int(sys.argv[3])+1 if len(sys.argv) > 3 else 100), (int(sys.argv[4]) if len(sys.argv) > 4 else 1))
            else:
                print("Comando no reconocido")
    else:
        print('Comando no reconocido')

