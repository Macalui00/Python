#Diagrama de caja
#Sirve para representar graficamente una serie de datos numericos a traves de sus cuadriles

import pandas as pd 
import numpy as np
import matplotlib as mpl 
import seaborn as sns

datos = np.random.randn(100)

sns.boxplot(datos)
mpl.pyplot.show()