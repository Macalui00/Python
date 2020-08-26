#Ejercicio 21

"""Crear una lista de 100 valores aleatorios que sigan una distribucion normal.
Crear un histograma mediante matplotlib con la lista de valores.
Crear un diagrama de caja (donde se acumula el 50% de los valores) mediante seaborn"""

import pandas as pd 
import numpy as np
import matplotlib as mpl 
import seaborn as sns

datos = np.random.randn(1000)
mpl.pyplot.figure() 

mpl.pyplot.subplot(1,2,1)
mpl.pyplot.hist(datos, color = "grey")
#Para asignarle nombres a los ejes:
mpl.pyplot.xlabel('Datos')
mpl.pyplot.ylabel('Distibución')
#Para ver la grilla o cuadrícula:
mpl.pyplot.grid(True)
mpl.pyplot.subplot(1,2,2)
sns.boxplot(datos)

mpl.pyplot.show()