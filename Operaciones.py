#Operaciones con arrays (+, - , *, /, **)

import numpy as np 

#Crear un array
array1 = np.array([1,2,3,4,5,6])
print(array1)

#Esto sirve para mostrar el resultado de la operacion
print(f"Multiplicar el array por 2: {array1*2}")
print(f"Dividir el array por 2: {array1/2}")
print(f"Sumarle a cada elemento del arrya 4: {array1+4}")

#Le hacemos esas operaciones sobre el array pero el array sigue manteniendose igual, es decir:
print(f"El array sigue siendo el mismo: {array1}")

#Para asignarlo realmente al array1 tenemos que cambiarlo:
array1 = array1 + 4

#Entonces ahora si el array1 cambió su valor:
print(f"El array cambió su valor: {array1}")

#Estas operaciones tambien se pueden hacer sobre arrays de dos dimensiones o matrices:
lista1 = [1,2,3,4]
lsita2 = [5,6,7,8]
lista_doble = (lista1,lsita2)
array_doble = np.array(lista_doble)

#ahora tiene dos filas.
print(array_doble)

#Tipos de datos que tiene el array:
print(array_doble.dtype)

#2 filas y 4 columnas:
print(array_doble.shape)

#Sobre este array tambien podemos hacer operaciones aritmeticas:
print(array_doble + 5)
print(array_doble / 3)
print(array_doble ** 2) #** exponenciacion, puedo elevar cada uno de los elementos.

#El array doble, sigue valiendo lo mismo hasta que se lo asignemos:
array_doble = array_doble + 4
print(array_doble)