#filtrar datos en dataframes

import pandas as pd 
import numpy as np

#Lista de valores de 10 elementos random de 3 en 3 - 10 filas 3 columnas:
lista_valores = np.random.rand(10,3)
print(lista_valores)

#Creamos el dataframe
dataframe = pd.DataFrame(lista_valores)
#No le hemos indicados columnas ni indices al dataframe

#Queremos seleccionar la columna 0:
columna0 = dataframe[0]
print(columna0)

#Desde aqui podemos hacer mas selecciones:
print(columna0[columna0 >0.40])

#Esto tambien lo podemos hacer a nivel de dataframe:
print(dataframe[dataframe > 0.40]) #Los que no cumplen con la condicion los coloca como NaN
