#Funciones con arrays

import numpy as np 

array = np.arange(5)

print(array)

#sobre este array queremos aplicar una funcion:
#raiz cuadrada: raiz cuadrada de cada uno de los elementos:
print(np.sqrt(array))

#Luego se pueden generar arrays con numeros random, de forma aleatoria:
print(np.random.rand(5)) #.rand(5) indica qeu seran 5 elementos aleatorios
#pueden ser positivos o negativos

lista = [5,6,7,8,9]
#a partir de una lista, creamos un array
array2 = np.array(lista)
print(array2)

#Vamos a sumar los dos arrays:
print(np.add(array, array2))

#si queremos saber cual es el maximo valor entre 2 arrays:
print(np.maximum(array,array2)) #retorna el segundo array