#Indexacion con arrays

import numpy as np 

#Creamos un array con elementos que van del 0 al 10
array = np.arange(0,11)

print(array)

#Podemos hacer un subconjunto de este array
#0 posicion final, 3 posicion final-1
print(array[0:3]) #[0,1,2]

#si quisieramos del 2 al 4:
print(array[2:5]) #[2,3,4]

#Si queremos hacer referencia a todo el array completo:
print(array[:])

#Tambien podemos crear una copia de un array
array_copia = array.copy()
print(f"{array_copia} y {array} son exactamente iguales")

array_copia[0:3] = 20
print(f"Hemos modificado array_copia: {array_copia}")

#Ahora vamos a trabajar con arrays de varias dimensiones:
array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2)

#Si quisieramos acceder a la primera lista del array, le pondríamos un indice que seria en este caso el indice 0
print(array2[0])

#Si quisieras acceder por ejemplo, al objeto 4 drento del segundo array del array:
print(array2[1][0])