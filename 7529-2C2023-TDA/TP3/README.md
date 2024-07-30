# Teoría de Algoritmos I - TP 3 - Problemas NP-Completos

## Dependencias

* Matplotlib
* PuLP

## Estructura de los archivos

Todos los archivos se deben encontrar en el mismo directorio.

## Modo de ejecución

Para ejecutar el programa y obtener una solución óptima para el problema, se debe utilizar la siguiente linea de código:
```python
python3 main.py <path_al_archivo_con_los_elementos> <flag_de_algoritmo>
```

El archivo con los elementos debe ser un archivo .txt, en el cual, en cada linea se deben contener los jugadores que desea que jueguen cada uno de los pedidos de la prensa (Mismo formato que los archivos provistos por la cátedra)

Los algoritmos disponibles son:
  * *-p*: Ejecuta el algoritmo de programación lineal
  * *-b*: Ejecuta el algoritmo de backtracking
  * *-g*: Ejecuta una log(b*)-aproximación greedy (Donde b* es la longitud del subset con más elementos)
  * *-q*: Ejecuta una b*-aproximación por programación lineal continua (Donde b* es la longitud del subset con más elementos)

### Uso alternativo

Si se desea utilizar solamente alguna de las funciones de solución óptima o aproximada, se puede importar las funciones del archivo, y se le debe pasar por parámetros:

  * Una lista con los subsets a cubrir

  * En el caso de programación lineal, si se desea que esta sea continua o no

Adicionalmente se incluye una función que permite verificar si una solución propuesta es valida para un conjunto de subsets.

## Testing

Se adjunta un archivo `test.py` que contiene pruebas para los algoritmos desarrollados. Asimismo posee listas subsets con soluciones únicas y multiples, consus respectivas soluciones (En el caso de los conjuntos de subsets con soluciones multiples, se provee una unica solución) que pueden ser utilizadas para realizar pruebas individuales con los algoritmos desarrollados.

## Gráficos

Se adjunta un archivo `graficos.py` que permite realizar gráficos de los tiempos de ejecución. Al ejecutarlo se produce un gráfico con los tiempos de ejecución de las diferentes listas de subconjuntos. Para ejecutarlo se utiliza la siguiente línea de código:

```python
python3 graficos.py <flag_de_algoritmo>
```

Donde los algoritmos disponibles son:
  * *-p*: Programación Lineal
  * *-b*: Backtracking
  * *-g*: Greedy
  * *-q*: Programación Lineal Continua

Si se desea realizar un gráfico con listas de subconjuntos aleatorios, se debe ejecutar el archivo con la flag *-r*, seguida de la flag de algoritmo. Adicionalmente, si se desea modificar la cota máxima de días de entrenamiento, se puede agregar un entero luego de las flags. Asimismo, si se quiere modificar el paso entre lista y lista, se puede agregar otro entero más con el nuevo paso.
A continuación, un ejemplo completo de este modo de uso:

```python
python3 graficos.py -r <flag_de_algoritmo> <cota_maxima> <paso>
```

## Seguimiento Backtracking y Greedy

A continuación presentamos una representación visual de los algoritmos Greedy y Backtracking implementados.

<p align="center">
  <a href="https://youtu.be/ZCCkPOSbexQ">
    <img src="https://github.com/geronimo-palavecino/7529-2C2023/blob/main/TP3/portada_tp3.png" alt="Seguimiento del algoritmo" width="500">
  </a>
</p>
