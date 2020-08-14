#Estadisticas en dataframes

#Algunos metodos estadisticos para utilizarlos en dataframes:
import pandas as pd 
import numpy as np 

array = np.array([[1,8,3],[5,6,7]])
print(array)

dataframe = pd.DataFrame(array, index=["a", "b"], columns = list("123"))
print(dataframe)

#Ahora vamos a ver algunas funciones:

#Sumar por columnas:
print(dataframe.sum())

#Sumar por filas:
print(dataframe.sum(axis=1))

#El minimo valor por columnas:
print(dataframe.min())

#El maximo valor por columnas:
print(dataframe.max())

#El maximo valor por filas:
print(dataframe.max(axis=1))

#Que me retorne el valor del indice del minimo valor por columna:
print(dataframe.idxmin())

#Describe:
print(dataframe.describe())
#Me retorna una serie de valores estadisticos como:
#La cantidad de valores que tiene cada columna, la media (mean), desviacion tipica (std),
#Minimo valor de cada columna (min), e 25% del total, el 50% del total, .....

