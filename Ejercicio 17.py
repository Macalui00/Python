#Ejercicio
""" Crear la funcion pares que devuelva un array de numeros pares entre
dos valores pasados como parametros a la funcion (inicio y fin)

utilizar la funcion pares con los numeros 1 y 30
utilizar la funcion pares con los numeros 2 y 40
"""

import numpy as np 

def pares(inicio, fin):
	if (inicio % 2 != 0):
		inicio += 1		
	array = np.arange(inicio,fin,2)
	return array

def ingresoInicio():
	try: 
		print("Ingrese inicio del array")
		inicio = int(input ())
	except ValueError:
		print("Dato erroneo ingresado")
		ingresoInicio()
	except:
		print("Ups! ha ocurrido un error")
		ingresoInicio()
	else:
		return inicio

def ingresoFin():
	try: 
		print("Ingrese fin del array")
		fin = int(input ())
	except ValueError:
		print("Dato erroneo ingresado")
		ingresoFin()
	except:
		print("Ups! ha ocurrido un error")
		ingresoFin()
	else:
		return fin

def continuar():
	print("¿Desea obtener otro array de pares? S/N")
	respuesta = str(input())
	while (respuesta != 'S') and (respuesta != 'N'):
		print("Respuesta incorrecta. Ingrese S/N")
		respuesta = str(input())
	return respuesta

def procesoPares():
	inicio = ingresoInicio()
	fin = ingresoFin()
	arrayPares = pares(inicio,fin)
	print(f"Su array de pares es el siguiente: {arrayPares}")


procesoPares()
cont = continuar()
while (cont == 'S'):
	procesoPares()
	cont = continuar()
