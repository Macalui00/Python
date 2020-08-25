#Ejercicio 20
"""Vamos a filtrar datos en un DataFrame.
Creamos una lista de 50 valors aleatorios enteros entre 0 y 100. Convertiremos esta lista en un dataframe con 5 filas y 10 columnas.
Filtraremos los datos del dataframe para visualizar solo los valores que sean mayores de 50"""

import numpy as np
import pandas as pd

lista_valores = np.random.randint(0,100,50)
print(lista_valores)
lista_valores.resize(5,10)
print(lista_valores)

dataframe = pd.DataFrame(lista_valores)
print(dataframe[dataframe > 50])

# def inicRangos():
#     rango =[]
#     print("Ingrese rango inf")
#     rango[0] = int(input())
#     print("Ingrese rango sup")
#     rango[1] = int(input())
#     print("Ingrese cantidad de valores que desea")
#     rango[3] = int(input())
#     while (rango[3] < rango[0] or rango[1] < rango[3]):
#         print(f"La cantidad debe estar entre {rango[0]} y {rango[1]}. Ingrese cantidad de valores que desea")
#         rango[3] = int(input())
#     return rango

# def generarDataframe(rango):
#     lista_valores = np.random.randint(rango[0],rango[1],rango[2])
#     lista_valores.resize(5,10)
#     print(lista_valores)

# rango = inicRangos()
