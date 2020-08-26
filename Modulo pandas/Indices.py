#Indices

import pandas as pd 

lista_valores = [1,2,3]
lista_indices = ['a','b', 'c']
serie = pd.Series(lista_valores, index=lista_indices)


#Si queremos saber los nombres de los indices
print(serie.index)

#Obtener el valor que esta en tal index:
print(serie.index[0])

#No podemos cambiar el valor de los indices:
#serie.index[0] = 'x' esto dará error.
#Error: el indice no soporta cambios.
#Tendria que hacer una nueva serie... si puedo cambiar los valores pero no los indices.

#Otra forma de ver los indices, a traves de un dataframe
notas = [[6,7,8], [8,9,5], [6,9,7]]
asignaturas = ["matematicas", "historia", "fisica"]
nombres = ["Juan", "Macarena", "Aldana"]

datafame = pd.DataFrame(lista_valores, index= asignaturas, columns=nombres)
print(dataframe)

#Cuales serían los indices aca?
print(dataframe.index) #asignaturas

#Podemos recuperar un indice en particular.
print(datafame.index[1])



