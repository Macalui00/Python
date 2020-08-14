#NaN - Not a Number

import pandas as pd 
import numpy as np 

#Le agregamos un valor NaN a una lista
lista_valores = ["1","2", np.nan, "4"]
print(lista_valores)

serie = pd.Series(lista_valores, index = list("abcd"))
print(serie)

#Podemos verificar si hay algun valor numero aplicando el siguiente metodo:
print(serie.isnull())
#elemento c tiene una valor nulo

#Borrar valores nulos:
print(serie.dropna())

#Para que se borre de manera permanente:
serie = serie.dropna()
print(serie)

#Ahora con dataframes:
lista_valores = [[1,2,3],[4,np.nan,5], [6,7,np.nan]]
print(lista_valores)

lista_indices = list("123")
print(lista_indices)

lista_columnas = list("abc")
print(lista_columnas)

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns= lista_columnas)
print(dataframe)

#Ver cuales valores son nulos y cuales no
print(dataframe.isnull)

#Borrar los nulos, borra todas las filas que tengan algun nulo
print(dataframe.dropna())

#Otra opcion es rellenar este nulo con algun valor.
print(dataframe.fillna(0))
#y de esta manera podemos realizar operaciones sobre el dataframe