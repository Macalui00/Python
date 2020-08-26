#Seleccionar entradas para dataframes

import pandas as pd 
import numpy as np 

lista_valores = np.arange(25).reshape(5,5)
lista_indices = ["i1","i2","i3" "i4", "i5"]
lista_columnas = ["c1", "c2", "c3", "c4", "c5"]

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

#acceder a una columna
print(dataframe["c2"])

#acceder a un elemento que esta en una columna y una fila determinada
print(dataframe["c2"]["i2"])

#Seleccionar varias columnas
print(dataframe[["c3","c4"]])

#Seleccionar por valor: valor cumpliendo determinada condicion:
#valores de la columnas 2 mayores de 5
print(dataframe["c2"] > 15) #retorna las dos filas de abajo

#¿Que elementos del dataframe son mayores que 20?
print(dataframe >20) #retorna una tabla con verdaderos y falsos indicando si cumplen o no la condicion.

#Podemos buscar tambien por indice:
print(dataframe.loc("i3"))

#Obtener el valor de tal celda:
print(dataframe.loc["i3"]["c4"])

