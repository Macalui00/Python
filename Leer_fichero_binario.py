#Vamos a utilizar pickle para leer datos de un fichero binario.

import pickle

#leer fichero binario:
fichero = open("fichero_colores.pckl", "rb") #modo lectura binaria

#Mediante pickle y el modulo load, cargamos el fichero:
lista_leida_fichero = pickle.load(fichero) #Esto lo que hace es devolver los datos que hay en el fichero.

#la podemos imprimir para verificar que la hemos leido correctamente.
print(lista_leida_fichero)

