#Mapas de calor (heatmap)

import pandas as pd 
import numpy as np
import matplotlib as mpl 
import seaborn as sns

vuelos = sns.load_dataset("flights")
# print(vuelos.head())
#Año, mes y cantidad de pasajeros

vuelos = vuelos.pivot("month", "year","passengers")
# print(vuelos)
#se crea una matriz de datos que son el numero de pasajeros, y le pusimos como indices de filas los meses y como columnas los años.
#Esto nos ayuda luego para crera un mapa de calor
mpl.pyplot.figure() 

mpl.pyplot.subplot(2,2,1)
sns.heatmap(vuelos)

#si queremos ver los valores aparte del mapa de calor
mpl.pyplot.subplot(2,2,2)
sns.heatmap(vuelos,annot=True,fmt="d")

print(vuelos.loc["May"][1956])
valorCentral=vuelos.loc["May"][1956]
mpl.pyplot.subplot(2,2,3)
sns.heatmap(vuelos, center=valorCentral, annot=True, fmt="d")

#La barra de colores la puedo poner horizontal en vez de vertical:
mpl.pyplot.subplot(2,2,4)
sns.heatmap(vuelos, center=valorCentral, annot=True, fmt="d", cbar_kws={"orientation":"horizontal"})

mpl.pyplot.show()