import random
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from main import obtenerGananciaMaxima
from test import EjemplosTamanos, EjemplosEsfuerzos, EjemplosEnergias

def graficoEjemplos():
    resultados = []
    t_inicio = time.time()

    for i in range(0, len(EjemplosTamanos)):
        inicio = time.time()
        obtenerGananciaMaxima(EjemplosTamanos[i], EjemplosEsfuerzos[i], EjemplosEnergias[i])
        resultados.append(time.time() - inicio)
    
    print(f'Tiempo total tardado: {time.time() - t_inicio} segundos')

    plt.figure(figsize=(8, 6))
    plt.grid(True)

    plt.scatter(EjemplosTamanos, resultados, label='Algoritmo', color='b')

    plt.xlabel('Cantidad de días de entrenamiento')
    plt.ylabel('Tiempo consumido [s]')
    plt.title('Tiempo transcurrido para obtener la ganancia máxima de los entrenamientos')

    plt.xlim(0, 26)
    plt.show()

def generarValoresAleatorios(n = 1, rango = 100, alpha = 0):
    esfuerzos = []
    energias = []
    energiaAnterior = rango
    for i in range(n):
        esfuerzos.append(random.randint(1, int(rango)))
        energiaAnterior = random.randint(int(energiaAnterior * alpha + 1), energiaAnterior)
        energias.append(energiaAnterior)
    return (n, esfuerzos, energias)

def graficoValoresAleatorios(maximo = 100, paso = 1):
    tamanoElementos = range(1, maximo, paso)
    resultados = []
    t_inicio = time.time()
    for i in tamanoElementos:
        (n, esfuerzos, energias) = generarValoresAleatorios(n = i, alpha = 0.5)
        inicio = time.time()
        obtenerGananciaMaxima(n, esfuerzos, energias)
        resultados.append(time.time() - inicio)

    print(f'Tiempo total tardado: {time.time() - t_inicio} segundos')

    plt.figure(figsize=(8, 6))
    plt.grid(True)

    plt.scatter(tamanoElementos, resultados, label='Algoritmo', color='b')


    plt.xlabel('Cantidad de días de entrenamiento')
    plt.ylabel('Tiempo consumido [s]')
    plt.title('Tiempo transcurrido para obtener la ganancia máxima de los entrenamientos')

    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        graficoEjemplos()
    else:
        if sys.argv[1] == '-r':
            if len(sys.argv) == 2:
                graficoValoresAleatorios()
            elif len(sys.argv) == 3:
                graficoValoresAleatorios(int(sys.argv[2]))
            else:
                graficoValoresAleatorios(int(sys.argv[2]), int(sys.argv[3]))
        else:
            print('Comando no reconocido')

