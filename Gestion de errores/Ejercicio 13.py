"""
Crear la funcion "operacion" que dados 3 numeros, divida el primer numero entre la resta de los otros dos numeros.

utilizar la funcion creada con los numeros 5,4,2
utilizar la funcion creada con los numeros 6,3,3

utilizar el bloque try... except para controlar cualquier posible error.
"""

def operacion(num1,num2,num3):
	num4 = num2 - num3
	print(f"La resta entre {num2} y {num3} es: {num4}.")
	try:
		division = num1 / num4
		print(f"EL resultado final es: {division}.")
	except ZeroDivisionError:
		print("Error, hubo una división por cero.")
	except: 
		print("Ups! Ha habido un error.")
	else:
		print("La operación se pudo realizar con exito.")
	finally:
		print("Fin del cálculo.")

def verificarRespuesta (respuesta):
	while (respuesta != 'S') and (respuesta != 'N'):
		print("Respuesta incorrecta. Ingrese S/N")
		respuesta = input ()
	return respuesta
def obtener_datos_y_actuar():
	print("Introduzca primer numero")
	num1 = int(input ())
	print("Introduzca segundo numero")
	num2 = int(input ())
	print("Introduzca tercer numero")
	num3 = int(input ())

	operacion(num1,num2,num3)

print("¿Desea realizar operación? S/N")
respuesta = input ()

respuesta = verificarRespuesta(respuesta)


if (respuesta == 'S'):

	obtener_datos_y_actuar()

	print("¿Desea realizar otra operación? S/N")
	respuesta = input ()

	respuesta = verificarRespuesta(respuesta)

	while (respuesta == 'S'):
		obtener_datos_y_actuar()

		print("¿Desea realizar otra operación? S/N")
		respuesta = input ()

		respuesta = verificarRespuesta(respuesta)