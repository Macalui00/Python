#Histogramas: representacion grafica de una variable o de unos datos en forma de barras, donde la superficie de cada barra es proporcional a la frecuencia de los valores representados.

import pandas as pd 
import numpy as np 

import matplotlib as mpl 
import seaborn as sns

#Para que ponga los graficos dentro de estas pruebas:solo si usas jupyter
# %matplotlib inline

datos1 = np.random.randn(100)

#Para darle un titulo al gráfico:
mpl.pyplot.title('Distribución de los datos')

#Creo el histograma:
#puedo asignarlo a una variable o no:
# mpl.pyplot.hist(datos1)
# hist1 = mpl.pyplot.hist(datos1)
#Para darle mas formato al histograma, agregandole bordes de tal grosor y color:
# mpl.pyplot.hist(datos1, edgecolor = 'black',  linewidth=1)

#Para asignarle nombres a los ejes:
mpl.pyplot.xlabel('Datos')
mpl.pyplot.ylabel('Distibución')

#Para ver la grilla o cuadrícula:
mpl.pyplot.grid(True)

#clf() clears the entire current figure with all its axes, but leaves the window opened, such that it may be reused for other plots:
# mpl.pyplot.clf()

#Para poder ver el gráfico:
# mpl.pyplot.show()

"""Algunos links interesantes para esto:
https://www.it-swarm.dev/es/python/como-trazar-un-histograma-usando-matplotlib-en-python-con-una-lista-de-datos/1056859313/
https://es.stackoverflow.com/questions/77405/histogramas-con-matplotlib-python-l%C3%ADneas-de-separaci%C3%B3n
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
"""

#Ahora probaremos de utilizar el otro modulo:
#Esto tambien genera un histograma de los datos que hemos puesto
# hist3 = sns.distplot(datos1)

#Genero de la misma manera el titulo:
mpl.pyplot.title("Distribución de los datos")

#Genero de la misma manera el nombre de los ejes:
mpl.pyplot.xlabel("Datos")
mpl.pyplot.ylabel("Distribución")

#Muestro el gráfico:
# mpl.pyplot.show()

"""Links interesantes:
https://coderhook.github.io/learning%20seaborn
https://seaborn.pydata.org/tutorial/distributions.html
https://seaborn.pydata.org/generated/seaborn.distplot.html
https://seaborn.pydata.org/examples/distplot_options.html
https://www.analyticslane.com/2018/07/20/visualizacion-de-datos-con-seaborn/
"""
#Tanto a uno como a otro podemos cambiarle el color:
# sns.distplot(datos1, color = "green")
# mpl.pyplot.show()
# mpl.pyplot.hist(datos1, color = "grey")
# mpl.pyplot.show()

#Incluso puedo cambiar a que sea mas suave o mas oscuro mediante el parametro alpha
# sns.distplot(datos1, color = "green", hist_kws={"alpha":0.5}) #verde mas suave
# mpl.pyplot.show()

# mpl.pyplot.hist(datos1, color = "grey", alpha=0.5) #gris mas suave
# mpl.pyplot.show()

#Mientras alpha sea mas chico, más suave será el color.

#Creamos otros datos:
datos2 = np.random.randn(80)
# mpl.pyplot.hist(datos2, color="yellow", alpha=0.4)
# mpl.pyplot.show()

#Ahora juntemos los dos:
#Podemos indicar el numero de barras con el bin
# mpl.pyplot.hist(datos1, color="green", alpha=0.3, bins=20)
# mpl.pyplot.hist(datos2, color="azul", alpha=0.3, bins=20)
# mpl.pyplot.show()

#Así no se pueden comparar porque no tienen la misma densidad, uno tiene 100 elementos y el otro 80
#Para corregir esto podemos usar el density
mpl.pyplot.hist(datos1, color="green", alpha=0.3, bins=20, density=True)
mpl.pyplot.hist(datos2, color="blue", alpha=0.3, bins=20, density=True)
mpl.pyplot.show()

#Esto lo hemos hecho con la libreria maplotlib, ahora hagamoslo con el seaborn:
datos3 = np.random.randn(1000)
datos4 = np.random.randn(1000)
#Vamos a representarlos dentro de la misma grafica:
sns.jointplot(datos3,datos4)
mpl.pyplot.show()
#Datos3 esta arriba
#Datos4 a la derecha
#Y en el medio pone los puntos de coincidencia entre ambos

#Tambien podemos hacerlo para que se vea mas claro...
sns.jointplot(datos3,datos4, kind="hex") #kind hexadecimal
mpl.pyplot.show()