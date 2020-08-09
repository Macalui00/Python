#Creando arrays: vamos a crear arrays y para eso vamos a utilizar un modulo llamado numpy
#importamos este modulo y lo guardamos como np
import numpy as np
#Recordar que si hay que instalar un modulo: pip install nombremodulo

print(np.zeros(4))
print(np.ones(4))

print(np.arange(5))

#Supongamos que no quiero que empiece en 0 sino en 2 y que vaya saltando de 3 en 3
print(np.arange(2,20,3)) #hasta un numero menor que 20.

#Tambien podemos hacer un array a partir de una lista
lista1 = [1,2,3,4]
print(lista1)
array1 = np.array(lista1)
print(array1)

lista2 = [5,6,7,8]
lista_doble = (lista1, lista2)

print(f"Veremos que es una tupla esta compuesto por dos elementos que son las listas: {lista_doble}")

array_doble = np.array(lista_doble)

print(f"Array doble: {array_doble}")

#podemos ver la forma que tiene el array: shape: nos dice las filas y las columnas que tiene:
print(array_doble.shape)

#tambien podemos ver el tipo de dato que tiene el array
print(array_doble.dtype)