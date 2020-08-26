#Regresiones

#En estadistica el analisis de regresion es un proceso estadistico para estimar las relaciones entre variables. Como varia el valor de una variable en funcion de otras variables.

#En este caso veremos Regresion Lineal o Ajuste Lineal:

import pandas as pd 
import numpy as np
import matplotlib as mpl 
import seaborn as sns

#Dentro del seaborn ya vienen datasets o conjuntos de datos para hacer nuestras pruebas
#Dataset de propinas en este caso

propinas = sns.load_dataset("tips")
# print(propinas.head())
# print(propinas.head(10))

sns.lmplot("total_bill","tip", propinas)

#Esto genera una grafica de regresion lineal que compara el total de las facturas con las propinas
#Podemos si queremos cambiarlo y ponerle una serie de marcadores y colores diferentes a estos puntos y lineas:
sns.lmplot("total_bill","tip", propinas, scatter_kws={"marker":"o", "color":"green"}, line_kws={"color":"blue"})

#Si solo queremos poner los puntos y quitar la linea:
sns.lmplot("total_bill","tip",propinas, fit_reg=False)

#Luego tambien podemos crear una columna más que sea el porcentaje, que porcentaje de propina sea con respecto del total pagado:
propinas["porcentaje"] = 100 * propinas["tip"] /propinas["total_bill"]

#Ahora voy a crear una grafica de regresion lineal de esos porcentajes
sns.lmplot("size","porcentaje",propinas)

#Tambien podemos establecer otras comparaciones entre otras variables:
sns.lmplot("total_bill", "porcentaje", propinas, hue="sex", markers=["x", "o"]) #compara por sexo masculino y femenino

#Tambien podemos hacerlo por dias de la semana
sns.lmplot("total_bill", "porcentaje", propinas, hue="day") #compara por sexo masculino y femenino

mpl.pyplot.show()