"""
Crear una funcion "buscar" que mediante una expresion regular indique
si una palabra esta en la frase.

Probar la funcion buscar con estas frases:
texto= "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = "frase"

En caso de encontrar la palabra en la frase indicar en que posicion empieza y en que posicion termina.

"""

import re

def verificarRespuesta (respuesta):
	while (respuesta != 'S') and (respuesta != 'N'):
		print("Respuesta incorrecta. Ingrese S/N")
		respuesta = input ()
	return respuesta

def obtener_datos_y_buscar():
	print("Introduzca texto")
	texto = str(input ())
	print("Introduzca palabra a buscar")
	palabra_a_buscar = str(input ())
	buscar(texto, palabra_a_buscar)

def buscar(texto, palabra):
	resultado = re.search(palabra, texto)
	if (resultado):
		print(f"Palabra {palabra} encontrada.")
		#Para obtener la posicion inicial y final
		inicial = resultado.start()
		final = resultado.end()
		print(f"La palabra {palabra} empieza en la posicion: {inicial} y finaliza en la posicion: {final}")
	else:
		print(f"Palabra {palabra} no encontrada.")

print("¿Desea buscar una palabra en el texto? S/N")
respuesta = input ()

respuesta = verificarRespuesta(respuesta)


if (respuesta == 'S'):

	obtener_datos_y_buscar()

	print("¿Desea buscar una palabra en el texto? S/N")
	respuesta = input ()

	respuesta = verificarRespuesta(respuesta)

	while (respuesta == 'S'):
		obtener_datos_y_buscar()

		print("¿Desea buscar una palabra en el texto? S/N")
		respuesta = input ()

		respuesta = verificarRespuesta(respuesta)