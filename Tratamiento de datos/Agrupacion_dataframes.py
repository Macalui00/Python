#Agrupacion en dataframes: como se pueden agrupar datos dentro de un dataframe

import pandas as pd 
import numpy as np

lista_valores = {"clave1": ["x", "x", "y", "y", "z"],"clave2": ["a","b","a", "b", "a"], "datos1": np.random.rand(5),"datos2": np.random.rand(5)}

dataframe = pd.DataFrame(lista_valores)

#Supongamos que los datos1 los queremos agrupar por la clave1
grupo = dataframe["datos1"].groupby(dataframe["clave1"])
print(grupo) #Nos dice que es una serie agrupada, para visualizar algun dato, por ejemplo, calculamos la media (mean)
print(grupo.mean()) 