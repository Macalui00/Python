#Ordenar y clasificar series

import pandas as pd 
import numpy as np 

#Rango de valores del 0 al 4
print(range(4))

lista_valores = range(4)
lista_indices = list("CABD")

serie = pd.Series(lista_valores, index=lista_indices)
print(serie)

#Podemos ordenarlos por los indices:
print(serie.sort_index())

#Para poder volver a ordenarlos por los valores:
print(serie.sort_values())

#ahora tambien podemos hacer un ranking por los valores que tiene:
print(serie.rank())
#Lo que hace es decirte que la C esta en la posicion 1
#A en la posicion 2, B en la posicion 3 y D en la posicion 4

serie2 = pd.Series(np.random.randn(10))
#creamos una serie con valores random positivos y negativos.

#Ordenar de menor a mayor los valores
print(serie2.rank()) #aca se ve mejor como segun los indices los ordena de menor a mayor

print(serie2.sort_values())
