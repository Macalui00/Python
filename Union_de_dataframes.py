#Union de dataframes

import pandas as pd 

#creo un dataframe a partir de un diccionario con dos columnas que tienen lista de valores
dataframe1 = pd.DataFrame({"c1": ["1","2","3"], "clave": ["a","b","c"]})
dataframe2 = pd.DataFrame({"c2": ["4","5", "6"], "clave": ["c", "b", "e"]})
print(f"""dataframe1
{dataframe1}""")
print(f"""dataframe2
{dataframe2}""")

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2)
print(f"""Union del dataframe1 y 2:
{dataframe3}""") #Lo que hizo fue unir por la columna clave, que es la unica que tiene en comun

#Si queremos que la union la haga por una determinada columna:
dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2, on="clave")
print(f"""Union del dataframe1 y 2 por la clave:
{dataframe4}""")

#En este caso selecciona parte que es comun a las 2
#Si quiero que prevalezca el dataframe 1 y le añada los valores del dataframe 2 comunes si existen:
dataframe5 = pd.DataFrame.merge(dataframe1, dataframe2, on="clave",how="left")
print(f"""Left-Union del dataframe1 y 2 por medio de la clave:
{dataframe5}""")

#Si quiero lo mismo pero para el dataframe 2:
dataframe6 = pd.DataFrame.merge(dataframe1, dataframe2, on="clave",how="right")
print(f"""Right-Union del dataframe1 y 2 por medio de la clave:
{dataframe6}""")

#Si queremos que aparezca que ponga todos los elementos aunque no sean comunes:
dataframe7 = pd.DataFrame.merge(dataframe1, dataframe2, on="clave", how="outer")
print(f"""Outer-Union del dataframe1 y 2 por medio de la clave:
{dataframe7}""") #Pone valores nulos donde no existe la clave