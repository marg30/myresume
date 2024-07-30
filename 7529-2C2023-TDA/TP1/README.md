# Teoría de Algoritmos I - TP 1 - Algoritmos Greedy

## Dependencias

* Matplotlib

## Estructura de los archivos

Todos los archivos se deben encontrar en el mismo directorio.

## Modo de ejecución

Para ejecutar el programa se debe utilizar la siguiente linea de código:
```python
python3 main.py <path_al_archivo_con_los_elementos>
```
El archivo con los elementos debe ser un archivo CSV, en el cual, la primera columna debe contener los tiempos de análisis de Scaloni, y la segunda columna debe contener los tiempos de análisis de los ayudantes. Asimismo, la primera fila debe contener los labels, *S_i* para los tiempos de Scaloni, y *A_i* para los tiempos de los ayudantes (Mismo formato que los archivos provistos por la cátedra).

Asimismo, se puede ejecutar el archivo de la siguiente forma para obtener el orden en el que se deben mirar los videos para obtener el tiempo mínimo:
```python
python3 main.py <path_al_archivo_con_los_elementos> -o
```

### Uso alternativo
Si se desea utilizar solamente la función de solución greedy desarrollada, se puede importar la función del archivo, y se le debe pasar por parámetros una lista de tuplas. Cada una de las tuplas representa el tiempo de análisis de un video, y deben tener el siguiente formato:

```python
(tiempo_analisis_scaloni, tiempo_analisis_ayudante)
```

## Testing

Se adjunta un archivo `test.py` que contiene pruebas para el algoritmo desarrollado. Asimismo posee una lista que posee diferentes ejemplos de listas de elementos que se pueden utilizar para realizar pruebas individuales con el algoritmo desarrollado.

## Gráficos

Se adjunta un archivo `graficos.py` que permite realizar gráficos de los tiempos de ejecución. Al ejecutarlo se produce un gráfico con los tiempos de ejecución de las diferentes listas de elementos de ejemplo. Para ejecutarlo se utiliza la siguiente línea de código:

```python
python3 graficos.py
```

Si se desea realizar un gráfico con volumen de elementos, se debe ejecutar el archivo con la flag *-v*.
