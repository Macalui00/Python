#Combinando estilos

import pandas as pd 
import numpy as np
import matplotlib as mpl 
import seaborn as sns

datos = np.random.randn(100)

#Representamos los datos mediante un histograma:
# sns.distplot(datos, color="green")
# mpl.pyplot.show()

#Ahora quitemos el grafico de barras y dejemos solamente la curva:
# sns.distplot(datos, color="green", rug=False, hist=False)
# mpl.pyplot.show()

#Ahora probemos configurar el primero pero de un color la curva y de otro las barras:
#Creamos un diccionario para las caracteristicas (argumentos) de cada uno:

argumentos_curva = {"color": "black", "label":"Curva"} #label, etiqueta, nombre
argumentos_histograma = {"color": "grey", "label":"Histograma"} #label, etiqueta, nombre

# sns.distplot(datos, bins=25, kde_kws=argumentos_curva, hist_kws=argumentos_histograma)
# kde_kws: argumentos de la curva, hist_kws: argumentos del histograma
# bins: cantidad de barras

#Creando todos los graficos en una misma ventana:
#Se crea el objeto que contiene todos los graficos y donde se declara el tamaño de la figura:
mpl.pyplot.figure(figsize=(9, 3))

#subplot(numero de filas, numero de columnas, numero de area):
mpl.pyplot.subplot(131)
#Defino el grafico en esa posicion:
sns.distplot(datos, color="green")
mpl.pyplot.subplot(132)
#Defino el grafico en esa posicion:
sns.distplot(datos, color="green", rug=False, hist=False)
mpl.pyplot.subplot(133)
#Defino el grafico en esa posicion:
sns.distplot(datos, bins=25, kde_kws=argumentos_curva, hist_kws=argumentos_histograma)
mpl.pyplot.suptitle('Gráficos Distribuciones.py')

#Deberia estar definido un solo show en toda la hoja
# mpl.pyplot.show()

#Para ver más de esto de varias gráficas en una sola hoja mirar "Prueba de graficos.py"

#El seaborn se maneja muy bien con el pandas
serie = pd.Series(datos)
#representar todos estos datos dentro de un histograma:
sns.distplot(serie,bins=25, color="green")
mpl.pyplot.show()