#Combinaciones de elementos: combinar un dataframe de diferentes formas.

import pandas as pd 
import numpy as np 

lista_valores = np.arange(25).reshape(5,5)
dataframe = pd.DataFrame(lista_valores)

#Creamos combinacion aleatoria:
combinacAleat = np.random.permutation(5) #Genera un array de elementos del 5-1 al 0 pero de manera aleatoria.

#vamos a utilizar el orden de elementos ya sea para ordenarlos o desordenarlos:
print(dataframe.take(combinacAleat))