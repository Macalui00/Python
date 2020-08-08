#pickle - modulo para grabar ficheros binarios

import pickle

lista_colores = ["azul", "verde", "rojo", "amarillo"]

fichero = open("fichero_colores.pckl", "wb") #formato w write escritura, b binario

#para grabar en el archivo usamos lo siguiente:
pickle.dump(lista_colores, fichero) #graba la lista de colores en formato binario en el fichero.

fichero.close()