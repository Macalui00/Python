#Agrupar datos en categorias

import pandas as pd 
import numpy as np

precios = [42,55,48, 23, 5,21,88,34,26]
#Rango de precios:
rango = [10,20,30,40,50,60,70,80,90,100]

#Que me agrupe los precios dentro de los rangos
preciosAgrupados = pd.cut(precios, rango)
print(preciosAgrupados)
#El 5 no tiene ningun rango, para que lo tenga:
rango = [0,10,20,30,40,50,60,70,80,90,100]
preciosAgrupados = pd.cut(precios, rango)
print(preciosAgrupados)

#Value counts: contar cuantos hay en cada categoria:
print(pd.value_counts(preciosAgrupados))