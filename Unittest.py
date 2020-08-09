#Unittest - Sirve para crear pruebas dentro del propio código

def multiplicar(num1, num2):
	return num1 * num2

resultado = multiplicar(2,4)
print(resultado)

import unittest

class pruebas(unittest.TestCase): #hemos implementado una clase
	def test(self): #que tiene un metodo test que va a probar si hacer equal es igual a 8 y si es correcto, ha pasado la prueba
		self.assertEqual(multiplicar(2,4),8)
		#self.assertEqual(multiplicar(2,4),9)

#por ultimo agregamos el codigo para que ejecute el unittest.main()
if  __name__ == '__main__':
	unittest.main()

"""
8
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


Segunda prueba:
8
F
======================================================================
FAIL: test (__main__.pruebas)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Unittest.py", line 14, in test
    self.assertEqual(multiplicar(2,4),9)
AssertionError: 8 != 9

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

"""