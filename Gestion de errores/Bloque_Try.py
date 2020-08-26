"""
TRATAMIENTO DE ERRORES: BLOQUE TRY
permite verificar si un bloque de codigo tiene errores.

En nuestro programa no podemos permitir que nos salgan errores, entonces, para controlarlo y que no salga el error
utilizaremos el bloque try

"""
"""
numero1 = 5
numero2 = 0
division = numero1 / numero2
"""
#ESTO NOS DARÁ UN ERROR: DIVISION POR 0.
"""
try: #Prueba
	#acá metemos las intrucciones que queremos verificar.
	numero1 = 5
	numero2 = 2
	division = numero1 / numero2
	print(division)
except: #Y si encuentras algun error:
	print("Ha habido un error")
"""
"""esto lo podemos especificar aun más"""

# ZeroDivisionError

try: #Prueba
	#acá metemos las intrucciones que queremos verificar.
	numero1 = 5
	numero2 = 3
	division = numero1 / numero2
	print(division)
except ZeroDivisionError: #En caso de que el error sea de este tipo imprimeme un mensaje especial:
	print("Error, división entre cero.")
except: #Y si encuentras algun otro error diferente:
	print("Ha habido un error.")
#tambien podemos poner un else
else: #en caso de que no haya error:
	print("La división funcionó correctamente.")
#Y por ultimo tenemos el modulo finally: permite ejecutar algun codigo independientemente del resultado del try y del except
finally:
	print("Esta prueba se ha acabado.")