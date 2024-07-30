import csv
import sys

def merge_sort(tiempos):

    if len(tiempos) <= 1:
        return tiempos

    izq = tiempos[0:len(tiempos) // 2]
    der = tiempos[len(tiempos) // 2:]

    merge_izq = merge_sort(izq)
    merge_der = merge_sort(der)

    sorted = merge(merge_izq, merge_der)
    return sorted

def merge(izq, der):
    resultado = []
    i = 0
    j = 0
    while i < len(izq) and j < len(der):
        if izq[i][1] > der[j][1]:
            resultado.append(izq[i])
            i += 1
            continue
        resultado.append(der[j])
        j += 1

    while i < len(izq):
        resultado.append(izq[i])
        i = i + 1

    while j < len(der):
        resultado.append(der[j])
        j = j + 1

    return resultado


def tiempo_minimo(tiempos):
    tiempos = merge_sort(tiempos)
    tiempo_scaloni = 0
    tiempo_maximo = 0
    for tiempo in tiempos:
        tiempo_scaloni += tiempo[0]
        tiempo_actual = tiempo_scaloni + tiempo[1]
        if tiempo_actual > tiempo_maximo:
            tiempo_maximo = tiempo_actual
    return tiempo_maximo

def parsear_csv(path):
  tiempos = []
  with open(path) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        tiempos.append((int(row['S_i']), int(row['A_i'])))
  return tiempos


def main():
    if (len(sys.argv)) < 2:
        print(f'Faltan argumentos')
    elif (len(sys.argv)) < 3:
        print(f'Tiempo mínimo requerido para analizar todos los videos: {tiempo_minimo(parsear_csv(sys.argv[1]))}')
    elif sys.argv[2] == "-o":
        print(f'El orden para ver los videos en el menor tiempo posible es: {merge_sort(parsear_csv(sys.argv[1]))}')
    return 0

if __name__ == '__main__':
    main()
