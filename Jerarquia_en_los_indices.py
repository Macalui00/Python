#Jerarquia en los indices:

#A una serie podemos añadirle varios indices que estarán jerarquizados,
#es decir, será un índice de otro índice.

import pandas as pd
import numpy as np 

lista_valores = np.random.rand(6)
print(lista_valores)

#En este caso la lista de indices será doble porqeu habrá doble indice:
lista_indices = [[1,1,1,2,2,2],["a","b","c","a","b","c"]]

series = pd.Series(lista_valores, index = lista_indices)
print(series)
#Indice superior e inferior: 1, 2 y a,b y c respectivamente
#Indice de primer nivel y de segundo nivel

#Si queremos, por ejemplo, todos los valores del indice 1:
print(series[1])

#Si quisieramos solo el b, del 1:
print(series[1]["b"])

#Podemos aprovechar este doble indice para crear un dataframe donde un indice sea el indice y el otro sea la columna:
dataframe = series.unstack() #Genera un dataframe y el indice principal, lo pone como dataframe y el indice secundario lo coloca como columnas
print(dataframe)

#Podemos hacer el proceso inverso, a partir de un dataframe, crear una serie con doble indice:
lista_valores = np.arange(16).reshape(4,4)
print(lista_valores)

lista_indices = list("1234")
print(lista_indices)

lista_columnas= list("abcd")

dataframe2 = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe2)

serie2 = dataframe2.stack()
print(serie2)