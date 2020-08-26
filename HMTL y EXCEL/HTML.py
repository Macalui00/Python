#HTML con python
#Como obtener datos de una pagina HTML y cargarlo a un dataframe

import pandas as pd 

url = "https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol"

#leer los datos como html de la url indicada
dataframe = pd.io.html.read_html(url)

print("""----------DataFrame tal cual lo obtenemos de la url---------\r""")
print(f"{dataframe}\r")
#Vemos que ya estan los resultados de la tabla pero nos los devuelve de una forma rara.

print("""----------DataFrame Futbol mejor formato:---------\r""")
dataframe_futbol = dataframe[0]
print(f"{dataframe_futbol}\r")
""" lo siguiente es para el caso de que estes utilizando jupiter 
#Y para que esto quede correctamente bien, vemos que los datos de la primera fila son los datos que deberian estar como nombres de las columnas:
print(dataframe_futbol.loc(0))

#mediante el metodo dic podemos convertir esos datos en un dicionario:
dict(dataframe_futbol.loc(0))

dataframe_futbol = dataframe_futbol.rename(columna = dict(dataframe_futbol.loc(0)))
"""
#print("""----------DataFrame Futbol V2:---------\r""")
#print(f"{dataframe_futbol}\r")
#Y para quitar la primera linea del dataframe que tiene los nombres de las columnas:
#dataframe_futbol = dataframe_futbol.drop(0)
#print("""----------DataFrame Futbol V3:---------\r""")
#print(f"{dataframe_futbol}\r")

#Si quisieramos borrar una columna, como por ejemplo, notas:
dataframe_futbol = dataframe_futbol.drop("Notas", axis=1)
print(dataframe_futbol)
