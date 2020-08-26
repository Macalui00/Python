#Concatenacion de arrays, series y dataframes:
import pandas as pd #Series y DataFrames
import numpy as np #Arrays

#Concatenar arrays:
array1 = np.arange(9).reshape(3,3)
arrayR1 = np.concatenate([array1,array1])
print(arrayR1)

#Si quiero concatenarlo hacia la derecha y no hacia abajo:
#Le decimos que lo haga en el eje nro 1
arrayR2 = np.concatenate([array1,array1], axis = 1)
print(arrayR2)

#Concatenar series:
serie1 = pd.Series([1,2,3],index=["a","b","c"])
serie2 = pd.Series([4,5,6],index=["d","e","f"])

#Me concatena hacia abajo las dos series
serieConc = pd.concat([serie1,serie2])
print(serieConc)

#Concatenar y poner adelante el tipo de indice que tiene, ejemplo:
serieConc2 = pd.concat([serie1, serie2], keys=["serie1","serie2"]) #concatenamos y le agrego una clave mas que seria serie1 y serie2
print(serieConc2)

#Concatenar DataFrames:
dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=["a","b","c"])
dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=["a", "b", "c"])
dataframeConc = pd.concat([dataframe1,dataframe2])
print(dataframeConc)

#Si queremos reorganizar los indices para que salgan todos seguidos:
dataframeConc2 = pd.concat([dataframe1,dataframe2], ignore_index=True)
print(dataframeConc2)