#Agregacion (operaciones que dan un valor, como la media)

import pandas as pd 
import numpy as np 

lista_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan, np.nan, np.nan]]
lista_columnas = list("abc")
dataframe = pd.DataFrame(lista_valores, columns = lista_columnas)

#Agregacion: vamos a agrupar para obtener un valor:
print(dataframe.agg(["sum", "min"])) #Obtenemos la suma y el minimo valor SIN TENER EN CUENTA EL VALOR NULO, LOS HA OBVIADO

#Podemos hacerlo en el otro eje: sumamos por filas:
print(dataframe.agg("sum", axis=1))