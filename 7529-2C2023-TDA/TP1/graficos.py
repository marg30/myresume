import matplotlib.pyplot as plt
import numpy as np
import time
from main import *
from test import Ejemplos_tiempos
import sys
import random

def grafico_ejemplos_tiempos():
    ejemplos = Ejemplos_tiempos

    tamano_elementos = [len(ejemplo) for ejemplo in ejemplos]

    resultados = []
    t_inicio = time.time()

    for ejemplo in ejemplos:
        inicio = time.time()
        tiempo_minimo(ejemplo)
        resultados.append(time.time() - inicio)

    print(f'Tiempo total tardado: {time.time() - t_inicio} segundos')

    plt.figure(figsize=(8, 6))

    plt.scatter(tamano_elementos, resultados, label='Algoritmo', color='b')

    plt.xlabel('Cantidad de videos a analizar')
    plt.ylabel('Tiempo consumido [s]')
    plt.title('Tiempo transcurrido para obtener el tiempo mínimo para analizar los videos')

    plt.xlim(0, 11)

    plt.legend()
    plt.grid(True)
    plt.show()

#n: cantidad de tiempos a generar; rango: tiempo máximo posible a generar; proporcion: proporcion de tiempo que tardan los ayudantes respecto de scaloni (~Ai/Si)
def generar_tiempos_aleatorios(n = 3, rango = 120, proporcion = 1):
    if proporcion >= 1:
        multiplicador_scaloni = proporcion
        multiplicador_ayudantes = 1
    else:
        multiplicador_scaloni = 1
        multiplicador_ayudantes = proporcion
    tiempos = []
    for i in range(n):
        scaloni_i = random.randint(1, int(rango // multiplicador_scaloni) + 1)
        ayudante_i = random.randint(1, int(rango * multiplicador_ayudantes) + 1)
        tiempos.append((scaloni_i, ayudante_i))
    return tiempos

def grafico_volumen():
    tamano_elementos = range(1, 100000, 1000) #Comenzar mínimo con 1 elemento. Si se comienza con 0 elementos, el código funciona correctamente, pero al graficar la funcion lineal-logarítmica, numpy lanza una excepción
    resultados = []
    t_inicio = time.time()
    for i in tamano_elementos:
        elementos = generar_tiempos_aleatorios(n = i)
        inicio = time.time()
        tiempo_minimo(elementos)
        resultados.append(time.time() - inicio)

    print(f'Tiempo total tardado: {time.time() - t_inicio} segundos')

    plt.figure(figsize=(8, 6))

    plt.scatter(tamano_elementos, resultados, label='Algoritmo', color='b')

    plt.xlabel('Cantidad de videos a analizar')
    plt.ylabel('Tiempo consumido [s]')
    plt.title('Tiempo transcurrido para obtener el tiempo mínimo para analizar los videos')

    plt.legend()
    plt.grid(True)
    plt.show()
     


if __name__ == '__main__':
    if len(sys.argv) < 2:
        grafico_ejemplos_tiempos()
    elif sys.argv[1] == '-v':
        grafico_volumen()
    else:
        print("Comando no reconocido")
        
