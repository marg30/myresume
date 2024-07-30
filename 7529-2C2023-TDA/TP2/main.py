import sys
import numpy as np

def leerArchivo(nombreArchivo):
  with open(nombreArchivo, 'r') as file:
    numeroDias = file.readline()
    if len(numeroDias) == 0:
      return (0, [], [])
    else:
      e_i = []
      for i in range(0, int(numeroDias)):
        e_i.append(int(file.readline()))
      s_i = []
      for i in range(0, int(numeroDias)):
        s_i.append(int(file.readline()))
      return (int(numeroDias), e_i, s_i)

def obtenerGanancias(n, e_i, s_i): 
  matriz = [ [0]*(n + 1) for _ in range(n + 1) ]
  matriz[0][0] = 0
  for i in range(1, n + 1):
    for j in range(0, i + 1):
      if j == 0:
        matriz[i][j] = max(matriz[i-1])
      else:
        matriz[i][j] = min(e_i[i - 1], s_i[j - 1]) + matriz[i - 1][j - 1]
  return matriz

def obtenerGananciaMaxima(n, e_i, s_i):
  return max(obtenerGanancias(n, e_i, s_i)[n])

def obtenerEntrenamientos(n, e_i, s_i):
  entrenamientos = []
  matriz = obtenerGanancias(n, e_i, s_i)
  posicionActual = matriz[n].index(max(matriz[n]))
  for i in range(n - 1, -1, -1):
    if posicionActual == 0:
      entrenamientos.insert(0, "Descanso")
      posicionActual = matriz[i].index(max(matriz[i]))
    else:
      entrenamientos.insert(0, "Entreno")
      posicionActual -= 1
  return entrenamientos

def main():
    if (len(sys.argv)) < 2:
        print('Faltan argumentos')
    elif (len(sys.argv)) < 3:
        (n, e_i, s_i) = leerArchivo(sys.argv[1])
        print(f'Ganancia máxima obtenida de los días de entrenamiento: {obtenerGananciaMaxima(n, e_i, s_i)}')
    elif sys.argv[2] == "-s":
        (n, e_i, s_i) = leerArchivo(sys.argv[1])
        print(f'La secuencia de entrenamientos y descansos es: \n {obtenerEntrenamientos(n, e_i, s_i)}')
    return 0

if __name__ == '__main__':
    main()
