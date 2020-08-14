#Seleccionando datos en las series

import pandas as pd #para los dataframes y series
import numpy as np #para los arrays

#Creamos una serie
#para eso una lista de valores
lista_valores = np.arange(3)
print(lista_valores)
lista_indices = ["i1", "i2", "i3"]

serie = pd.Series(lista_valores, index = lista_indices)
print(serie)

serie = serie * 2
print(serie)

#formas de acceder a los elementos:
print(serie["i2"])
print(serie[2])
print(serie[0:2])

#Podemos hacer lo mismo con los indices:
print(serie["i1":"i2"])

#Podemos hacer una condicion: seleccionar aquellas de la serie que cumplan una condicion:
print(serie[serie > 3])

#Podemos cambiarle el valor
serie[serie>3] = 6
print(serie)

