#Doctest - Generar pruebas dentro de la documentación que estamos generando

def sumar(num1, num2):
	"""
	Esto es la documentación de esta funcion.
	Recibe 2 numeros como parámetros y devuelve su suma.

	>>> sumar(4,3)
	7

	>>> Sumar(5,4)
	9

	>>> Sumar(1,3)
	7
	"""
	return num1 + num2

resultado = sumar(2,4)
print(resultado)

#Queremos generar mediante el doctest una prueba, dentro del comentario ponemos nuestras pruebas con >>>
#para que la ejecute tenemos que poner las siguientes dos lineas al final del documento:

""" 
Comando a correr: python "Doctest.py" -v
Y retorna lo siguiente:

6
Trying:
    sumar(4,3)
Expecting:
    7
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.sumar
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
"""

import doctest
doctest.testmod()

"""Entonces dentro de la documentacion, generamos pruebas para validar que los cambios que hemos hecho
sean correctos."""