#Eliminar duplicados en DataFrames

import pandas as pd

lista_valores = [[1,2],[1,2],[5,6],[5,8]]
lista_indices = list("mnop")
lista_columnas = ["valor1","valor2"]

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
#Como podemos ver la fila m y n tienen los mismos valores, si queremos eliminar los duplicados dentro de un dataframe:
dataframe1 = dataframe.drop_duplicates()
print(dataframe1)

#ahora supongamos que el valor1 siempre tenga valores diferentes:
#Eliminar duplicados de las columnas:
dataframe2 = dataframe1.drop_duplicates(["valor1"]) #se queda con el primer valor
print(dataframe2)

#Para quedarse con el ultimo valor:
dataframe3 = dataframe1.drop_duplicates(["valor1"], keep="last") 
print(dataframe3)