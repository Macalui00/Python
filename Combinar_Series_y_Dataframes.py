#Combinar series y dataframes

import pandas as pd
import numpy as np

#Combinar Series:
serie1 = pd.Series([1,2,np.nan])
serie2 = pd.Series([4,5,6])

#agarra la serie 1 y si encuentra un valor nulo, lo cambia por el valor de la serie 2 en esa misma posicion.
serie3 = serie1.combine_first(serie2)

#Combinar DataFrames:
lista_valores = [1,2,np.nan]
dataframe1 = pd.DataFrame(lista_valores)
lista_valores_2 = [4,5,6]
dataframe2 = pd.DataFrame(lista_valores_2)

#agarra el dataframe1 y donde hay un valor nulo lo cambia por el valor del dataframe2
dataframe3 = dataframe1.combine_first(dataframe2)