# -------------------------------------------------------------------------------------------------------------
# Una version de crear una ventana con varios gráficos:
# -------------------------------------------------------------------------------------------------------------

# import random
# import matplotlib.pyplot as plt

#Defino los valores de los ejes x e y:
# p = list(range(14))
# q = [random.randint(0, 20) for _ in range(14)]

# def filtro(p, q):
#     q = [random.randint(0, 20) for _ in range(14)]
#     return p, q

#Creo la figura
# fig1 = plt.figure("Filtro")
# fig1.subplots_adjust(hspace=0.5, wspace=0.5)

#El range me sirve para indicar la cantidad de graficas que quiero crear, ejemplo si quiero crear 4 es: range(1,5
# for i in range(1, 5): )
#     p, q = filtro(p, q)

#     ax = fig1.add_subplot(2, 2, i) #ax para acomodar el elemento, para que se acomoden de un orden decente en el ultimo le coloco i
#     ax.plot(p,q,"g--") #A ese acomodo le asigno una grafica, p = x, q = y, tercer parametro es el nombre de la grafica
#     ax.set_xlabel("z") #nombre del eje x
#     ax.set_ylabel("w") #nombre del eje y
#     ax.set_title("cordenadas xy") #titulo del grafico
#     ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4) #Configuracion de la grilla
#     # Pintar los ejes pasando por (0,0)
#     ax.axhline(0, color='black', linewidth=0.5)

# def npotencia(array, exp):
#     return [n ** exp for n in array]

# # Creamos otra figura para mostrar
# fig2 = plt.figure("n ** i")
# fig2.subplots_adjust(hspace=0.5, wspace=0.5)

# x = list(range(1, 10))
# for i in range(2, 6):
#     y = npotencia(x, i)
#     ax = fig2.add_subplot(2, 2, i-1)
#     ax.plot(x, y, "r-.")
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.set_title("n ** {}".format(i))
#     ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
#     ax.axhline(0, color='black', linewidth=0.5)
# plt.show()

"""Links que sirvieron mucho: 
https://www.youtube.com/watch?v=m_no9B42878
https://es.stackoverflow.com/questions/178735/c%C3%B3mo-mostrar-un-conjunto-de-gr%C3%A1ficas-en-una-misma-ventana-o-en-varias-usando-ma
https://www.it-swarm.dev/es/python/como-hacer-varias-graficas-en-una-sola-pagina-usando-matplotlib/967061549/
"""

# -------------------------------------------------------------------------------------------------------------
# Otra version de crear una ventana con varios gráficos
# -------------------------------------------------------------------------------------------------------------

# import pandas as pd 
# import numpy as np
# import matplotlib as mpl 
# import seaborn as sns

# mpl.pyplot.figure(figsize=(9, 3)) #figsize: alto y ancho
# # Dividir la ventana en 1 fila x 2 columnas y dibujar primer gráfico

# mpl.pyplot.subplot(1,2,1)
# mpl.pyplot.plot((1,2,3,4,5))

# # Dividir la ventana en 1 fila x 2 columnas y dibujar segundo gráfico

# mpl.pyplot.subplot(1,2,2)
# mpl.pyplot.plot((5,4,3,2,1))
# mpl.pyplot.show()

# -------------------------------------------------------------------------------------------------------------
# Otra version de crear una ventana con varios gráficos
# -------------------------------------------------------------------------------------------------------------

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]

# mpl.pyplot.figure(figsize=(9, 3))

# mpl.pyplot.subplot(131)
# mpl.pyplot.bar(names, values)
# mpl.pyplot.subplot(132)
# mpl.pyplot.scatter(names, values)
# mpl.pyplot.subplot(133)
# mpl.pyplot.plot(names, values)
# mpl.pyplot.suptitle('Categorical Plotting')
# mpl.pyplot.show()

"""Links que sirvieron mucho:
https://python-para-impacientes.blogspot.com/2014/08/graficos-en-ipython.html
https://campusvirtual.ull.es/ocw/pluginfile.php/8878/mod_imscp/content/5/mltiples_grficas.html
"""