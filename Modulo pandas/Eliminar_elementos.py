#Eliminar elementos en series y dataframes

#Series
import pandas as pd 
import numpy as np 

#creamos una serie:
serie = pd.Series(np.arange(4), index=["a", "b","c", "d"])
#Debe haber tantos indices como elementos hay.

print(serie)

#Si quisieramos por ejemplo, eliminar el elemento c:
serie.drop("c") #Esto nos permite eliminar el elemento deseado.
print(serie)

#Dataframe
lista_valores = np.arange(9).reshape(3,3) #Lista de 9 elementos formateado con 3 filas y 3 columnas

#como hay 3 filas necesitamos 3 indices
lista_indices = ["a", "b","c"]

lista_columnas = ["c1", "c2", "c3"]

dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas )
print(dataframe)

print(dataframe.drop("b"))


#Si quisieramos eliminar la columna c2, por ejemplo:
print(dataframe.drop("c2", axis=1)) #Axis, eje donde se supone que esta la columna
#podemos notar que regreso el "b" esto se debe a que los cambios no se guardan permanentes

#para que sean permanentes:
dataframe = dataframe.drop("b")
print(dataframe)

dataframe = dataframe.drop("c2", axis=1)
print(dataframe)