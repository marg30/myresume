# Teoría de Algoritmos I - TP 2 - Programación Dinámica

## Dependencias

* Matplotlib

## Estructura de los archivos

Todos los archivos se deben encontrar en el mismo directorio.

## Modo de ejecución

Para ejecutar el programa se debe utilizar la siguiente linea de código:

```python
python3 main.py <path_al_archivo_con_los_elementos>
```

El archivo con los elementos debe ser un archivo .txt, en el cual, la primera línea debe contener la cantidad de días a considerar (n), en las siguientes n líneas, los esfuerzos/ganancias de dichos días, y en las subsiguientes n líneas, las energías que poseen los jugadores, si entrenasen sin descansar ningún día (Mismo formato que los archivos provistos por la cátedra).

Asimismo, se puede ejecutar el archivo de la siguiente forma para obtener la secuencia de entrenamientos y descansos, para lograr la máxima ganancia posible:

```python
python3 main.py <path_al_archivo_con_los_elementos> -s
```

### Uso alternativo

Si se desea utilizar solamente la función de solución por programación dinámica, se puede importar la función del archivo, y se le debe pasar por parámetros:

* Un entero, que representa la cantidad de días de entrenamiento a considerar
* Una lista con los esfuerzos/ganancias de cada uno de los n días
* Una lista con las energías de los jugadores si entrenan i días seguidos (Siendo i la posición en la que se encuentran en la lista)

## Testing

Se adjunta un archivo `test.py` que contiene pruebas para el algoritmo desarrollado. Asimismo posee listas de días, esfuerzos y energías, con sus respectivas ganancias máximas, que pueden ser utilizadas para realizar pruebas individuales con el algoritmo desarrollado.

## Gráficos

Se adjunta un archivo `graficos.py` que permite realizar gráficos de los tiempos de ejecución. Al ejecutarlo se produce un gráfico con los tiempos de ejecución de las diferentes listas de esfuerzos y energías de ejemplo. Para ejecutarlo se utiliza la siguiente línea de código:

```python
python3 graficos.py
```

Si se desea realizar un gráfico con listas de elementos aleatorios, se debe ejecutar el archivo con la flag *-r*. Adicionalmente, si se desea modificar la cota máxima de días de entrenamiento, se puede agregar un entero luego de la flag *-r* la nueva cota. Asimismo, si se quiere modificar el paso entre lista y lista, se puede agregar otro entero más con el nuevo paso.
A continuación, un ejemplo completo de este modo de uso:

```python
python3 graficos.py -r <cota_maxima> <paso>
```

# Seguimiento visual
A continuación presentamos una representación visual del algoritmo.

<p align="center">
  <a href="https://youtu.be/Bha90WuijNs">
    <img src="https://github.com/geronimo-palavecino/7529-2C2023-TP1/blob/main/TP2/preview.png?raw=true" alt="Seguimiento del algoritmo" width="500">
  </a>
</p>


