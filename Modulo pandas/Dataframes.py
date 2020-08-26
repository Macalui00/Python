#Dataframes

import pandas as pd 

import webbrowser

#Ruta de donde vamos a sacar los datos
website = 'https://es.wikipedia.org/wiki/Python'
#Le decimos que abra esta ruta:
webbrowser.open(website)

#Nos abrirá en nuestro navegador la pagina que le hemos indicado
#Copiamos parte de la informacion de la página y lo asignamos a un dataframe:
#Clipboard leer del portapapeles y lo asigna a una variable de tipo dataframe
dataframe_py = pd.read_clipboard()
print(dataframe_py) #ha creado este dataframe con los datos que ha sacado de la pagina de la wikipedia

#Como podemos navegar por ella? podemos ver primero las columnas que tiene
print(dataframe_py.columns) #devuelve una lista de los nombres de las columnas

#Si queremos saber los datos de una columna en particular podemos poner entre corchetes el nombre exacto de la columna:
print(dataframe_py['Clase']) #Nos devuelve un nuevo dataframe que esta indexado con los nombres de los campos de la columna

#si quiero un elemento en particular de la columna:
print(dataframe_py.loc[4])

#Podemos ver, si el dataframe es muy grande, los primeros elementos:
print(dataframe_py.head()) #Nos muestra las primeras 5 filas del dataframe.

#Si queremos ver menos o mas podemos indicarle con otro numero:
print(dataframe_py.head(3)) 
print(dataframe_py.head(6)) 

#Y si queremos ver pero por abajo:
print(dataframe_py.tail()) #Nos da los 5 ultimos

#lo mismo podemos pedir mas o menos numeros:
print(dataframe_py.tail(2))

#Esto fue crear dataframes con datos copiados de una pagina web pero tambien podemos crear un dataframe con datos de un diccionario.
#Vamos a crear un diccionario a traves de una lista
lista_asignaturas = ['matematicas','historia', 'fisica']
lista_notas = [8,7,9]
diccionario = {'Asignatuas':lista_asignaturas, 'Notas':lista_notas}
print(diccionario)

#A partir de esto podemos crear un dataframe, le llamamos:
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)
