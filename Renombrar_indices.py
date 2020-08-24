#Renombrar índices de un dataframe:
import pandas as pd 
import numpy as np

lista_valores = np.arange(9).reshape(3,3)
lista_indices = list("abc")
dataframe = pd.DataFrame(lista_valores, index=lista_indices)
print(dataframe)

#Ahora supongamos que queremos cambiar los indices para que en vez de minusculas sean mayusculas:
nuevos_indices = dataframe.index.map(str.upper) #que agarre los indices del dataframe y que los mapee a mayusculas

dataframe.index = nuevos_indices
print(dataframe)

#Otra forma de hacerlo: con el metodo rename
dataframe = dataframe.rename(index=str.lower)
print(dataframe)

#si queremos cambiar el nombre por el otro.
nuevos_indices2 = {"a":"f", "b":"g", "c":"h"}
dataframe = dataframe.rename(index = nuevos_indices2)
print(dataframe)

#Supongamos que solo cambiamos un indice y en vez de hacer dataframe = ..., hago dataframe.rename(..) + un parametro más:
nuevos_indices2 = {"f":"j"}
dataframe.rename(index=nuevos_indices2, inplace=True) #que me lo cambie dentro de la variable
print(dataframe)