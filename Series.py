#Series

import pandas as pd 

serie1 = pd.Series([3,5,7])

print(serie1)

#El objeto serie con sus tres valores y los ha indexado. Es una lista de valores que esta indexada.

print(serie1[1])

#Tambien podemos crear nosotros los indices
asignaturas = ["matematicas", "historia", "fisica", "literatura"]
notas = [8,6,9,7]
#Creamos un objeto del tipo serie que tendra como valores las notas y como indices las asignaturas
serie_notas_maca = pd.Series(notas, index= asignaturas)

print(serie_notas_maca)

#Si queremos saber la nota de fisica
print(serie_notas_maca["fisica"])

#que notas de daniel son >= 8
print(serie_notas_maca[serie_notas_maca >= 8])

#Tambien podemos ponerle un nombre a la serie
serie_notas_maca.name ="Notas de Maca"

print(serie_notas_maca)

#Incluso a los indices les podemos poner tambien un nombre
serie_notas_maca.index.name = "Asignaturas de Maca"
print(serie_notas_maca)

#Podemos convertir una serie en un diccionario:
diccionario = serie_notas_maca.to_dict()
print(diccionario)

#Podemos hacer el proceso inverso, de un diccionario a una serie
serie = pd.Series(diccionario)
#En este caso pierde el nombre de la serie y del indice
print(serie)

#Luego las series se pueden sumar y realizar operaciones entre ellas:
notas_ana = [7,5,8,7]
serie_notas_ana = pd.Series(notas_ana, index=asignaturas)
print(serie_notas_ana)

#media de las notas de la clase:
serie_notas_clase = (serie_notas_ana + serie_notas_maca) / 2
print(serie_notas_clase)