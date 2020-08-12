#Arrays o matrices transpuestas (cambiar ordenadamente las filas por las columnas)

import numpy as np

#Creamos un array que va de 0 a 14  y la forma que le vamos a dar va a ser de 3 y 5
#osea que 3 filas y 5 columnas.
array = np.arange(15).reshape((3,5))

print(array)

print(array[1][1])

#Si queremos hacer la transpuesta de este array, osea cambiar filas por columnas, tendriamos que hacer lo siguiente:
array_trans = array.T 
print(array_trans)