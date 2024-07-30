import csv
import random
import matplotlib.pyplot as plt
import numpy as np
import time
import pulp
import sys

def leerArchivo(nombreArchivo):
    pedidosPrensa = []
    try:
        with open(nombreArchivo, 'r') as file:
            readerArchivo = csv.reader(file)
            for linea in readerArchivo:
                pedidosPrensa.append(set(linea))
    except Exception as e:
        print(f"No se podido abrir el archivo. El error es el siguient: \n{e}")
    return pedidosPrensa

def verificadorSolucion(subconjuntos, solucion):
    subconjuntos_marcados = []
    for b in subconjuntos:
        for j in b:
            if j in solucion:
                subconjuntos_marcados.append(b)
                break
        if b not in subconjuntos_marcados:
            return False
    return True


# Backtracking

def backtrackHittingSet(subconjuntos, posibleC, mejorSolucion):
    if not subconjuntos:
        if not mejorSolucion or len(posibleC) < len(mejorSolucion):
          return posibleC.copy()
        return mejorSolucion
    if mejorSolucion and len(posibleC) >= len(mejorSolucion):
        return mejorSolucion 
    if any(elemento in posibleC for elemento in subconjuntos[0]):
        return backtrackHittingSet(subconjuntos[1:], posibleC, mejorSolucion)
    for elemento in subconjuntos[0]:
        posibleC.add(elemento)
        mejorSolucion = backtrackHittingSet(subconjuntos[1:], posibleC, mejorSolucion)
        posibleC.remove(elemento)
    return mejorSolucion

def solucionBacktracking(subconjuntos):
    mejorSolucion = backtrackHittingSet(subconjuntos, set(), [])
    return mejorSolucion


#Algoritmo de programacion lineal (optimo y aproximacion)

def crearVariables(subset, elementosContemplados, continuo):
    for elemento in subset:
        if elemento not in elementosContemplados:
            if continuo:
                elementosContemplados[elemento] = pulp.LpVariable(name = str(elemento), lowBound = 0, upBound = 1, cat='Continuous')
            else:
                elementosContemplados[elemento] = pulp.LpVariable(name = str(elemento), cat='Binary')

def solucionProgramacionLineal(B, continuo = False):
    problema = pulp.LpProblem("sum", pulp.LpMinimize)
    elementosContemplados = {}
    for subset in B:
      crearVariables(subset, elementosContemplados, continuo)
      expresion = pulp.lpSum(elementosContemplados[elemento] for elemento in subset)
      problema += expresion >= 1
    objectivo = pulp.lpSum(elementosContemplados.values())
    problema += objectivo
    problema.solve(pulp.apis.PULP_CBC_CMD(msg=False))
    solucion = set()
    treshold = 1/(len(max(B, key=len))) if continuo else 1/2
    for elemento, variable in elementosContemplados.items():
      if variable.value() >= treshold:
        solucion.add(elemento)
    return solucion


#Algoritmo de aproximacion greedy

def aproximacionGreedy(subsets):
    elementos = {}
    solucion = set()
    for subset in subsets:
        for element in subset:
            elementos[element] = elementos.get(element, 0) + 1
    setsNoConsiderados = set(map(frozenset, subsets))
    while elementos and setsNoConsiderados:
        element, _ = max(elementos.items(), key=lambda x: x[1])
        del elementos[element]
        setsConsiderados = set()
        for subset in setsNoConsiderados:
            if element in subset:
                for e in subset:
                    if e in elementos:
                        elementos[e] -= 1
                setsConsiderados.add(subset)
                solucion.add(element)
        setsNoConsiderados.difference_update(setsConsiderados)
    return solucion



def main():
    if (len(sys.argv)) < 3:
        print('Faltan argumentos')
    elif sys.argv[2] == "-p":
        solucion = solucionProgramacionLineal(leerArchivo(sys.argv[1]), False)
        print(f'Un conjunto mínimo de jugadores que deben jugar para contentar a la prensa: \n\n{solucion} ({len(solucion)} jugadores)')
    elif sys.argv[2] == "-b":
        solucion = solucionBacktracking(leerArchivo(sys.argv[1]))
        print(f'Un conjunto mínimo de jugadores que deben jugar para contentar a la prensa: \n\n{solucion} ({len(solucion)} jugadores)')
    elif sys.argv[2] == "-g":
        solucion = aproximacionGreedy(leerArchivo(sys.argv[1]))
        print(f'Un conjunto aproximadamente mínimo de jugadores que deben jugar para contentar a la prensa: \n\n{solucion} ({len(solucion)} jugadores)')
    elif sys.argv[2] == "-q":
        solucion = solucionProgramacionLineal(leerArchivo(sys.argv[1]), True)
        print(f'Un conjunto aproximadamente mínimo de jugadores que deben jugar para contentar a la prensa: \n\n{solucion} ({len(solucion)} jugadores)')
    else:
        print('No se reconoce el algoritmo a utilizar')
    return 0

if __name__ == '__main__':
    main()
