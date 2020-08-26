#Operaciones sobre series y dataframes

import pandas as pd 
import numpy as np 

#Series

serie1 = pd.Series([0,1,2], index=["a", "b","c"])
serie2 = pd.Series([3,4,5,6], index=["a", "b","c","d"])

print(serie1 + serie2)

#Como la serie1 no tiene indice d retorna en el caso del d un NaN

#DataFrames
lista_valores = np.arange(4).reshape(2,2)
#otra forma de crear listas
lista_indices = list("ab")
print(lista_indices)
lista_columnas = list("12")
print(lista_indices)

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns= lista_columnas)
print(dataframe)

lista_valores_2 = np.arange(9).reshape(3,3)
print(lista_valores_2)

lista_indices_2 = list("abc")
lista_columnas_2 = list("123")
print(lista_indices_2)
print(lista_columnas_2)

dataframe2 = pd.DataFrame(lista_valores_2, index = lista_indices_2, columns=lista_columnas_2)
print(dataframe2)

#Sumar dataframes: suma los elementos que coinciden y los que no, los coloca como NaN
dataframe3 = dataframe + dataframe2
print(dataframe3)

#Podemos seleccionar del dataframe3 solo los elementos que existen:
print(dataframe3[dataframe3 >= 0])
#Pero me sigue poniendo los NaN
#Esto se soluciona con el metodo add:
dataframe3 = dataframe.add(dataframe2,fill_value = 0)
print(dataframe3)