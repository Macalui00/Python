#Reemplazar datos en Series

import pandas as pd

serie = pd.Series([1,2,3,4,5], index=list("abcde"))
print(serie)

#cambiar permanentemente un valor de una serie
serie = serie.replace(1,6)
print(serie)

#Tambien puedo hacerlo a traves de un diccionario en vez de pasar valores
serie = serie.replace({2:8, 3:9})
print(serie)