"""
Crear el diccionario frutas:
frutas = ("manzana": "apple", "naranja": "orange", "platano":"banana", "limon":"lemon")

Grabar esta estructura de datos "frutas" en un fichero binario "fichero.pckl"
Ya que en un fichero de texto, solo se guardan caracteres, pero no se pueden guardar estas estructura.

Recuperar esta estructura de datos del fichero "fichero.pckl"
Verificar que sigue siendo un diccionario, ejecutando el metodo .values()
"""

import pickle

frutas = {"manzana": "apple", "naranja": "orange", "platano":"banana", "limon":"lemon"}


fichero = open("fichero.pckl", "wb") #formato w write escritura, b binario

#grabo el diccionario frutas en fichero binario:
pickle.dump(frutas, fichero) 

#como siempre cierro fichero
fichero.close()

#para recuperar los datos del fichero:
#leer fichero binario:
fichero = open("fichero.pckl", "rb") #modo lectura binaria

#cargo el fichero:
diccionario_leido_fichero = pickle.load(fichero) #Esto lo que hace es devolver los datos que hay en el fichero.

#la podemos imprimir para verificar que la hemos leido correctamente.
print(diccionario_leido_fichero.values())

#.values() : Retorna una lista de elementos, que serán los valores de nuestro diccionario.
# https://devcode.la/tutoriales/diccionarios-en-python/