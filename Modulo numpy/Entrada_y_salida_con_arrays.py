#Entrada y salida con arrays

import numpy as np 

array1 = np.arange(6)
print(array1)

#Vamos a salvar este array mediante la funcion de numpy para luego poder recuperarlo
np.save('array1s', array1)

#¿Como lo recuperamos ahora? mediante el modulo numpy load
print(np.load('array1s.npy'))


array2 = np.arange(8)
print(array2)

#si queremos salvar los dos arrays a la vez con la misma variable:
np.savez('arrays', x=array1, y=array2)

#Para recuperarlo:
array_recuperado = np.load('arrays.npz')
print(array_recuperado)

#si queremos recuperar el array1 que estaba en la x:
print(array_recuperado['x'])

#si queremos recuperar el otro array
print(array_recuperado['y'])

#tambien se puede guardar el array dentro de un fichero de texto:
np.savetxt('mificheroarray.txt', array2, delimiter=',') #cada elemento separado por una coma
print(np.loadtxt('mificheroarray.txt', delimiter= ','))

