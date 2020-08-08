"""	Crear un programa "programa1.py"
		Crear el objeto "fichero" de la clase "Fichero" del modulo "moduloficheros.py"
		Utilizar el metodo "grabar_fichero" del objeto "fichero" para crear un nuevo fichero
		Utilizar el metodo "incluir_fichero" para incorporar más datos al final del fichero
		Utilizar el metodo "leer_fichero" para ver el contenido del mismo
"""
import moduloficheros

def verificarRespuesta (respuesta):
	while (respuesta != 'S') and (respuesta != 'N'):
		print("Respuesta incorrecta. Ingrese S/N")
		respuesta = input ()
	return respuesta

def incluirEnFichero():
	print("Ingrese mensaje a incluir en fichero")
	mensaje = input()

	print("¿Con salto de línea? S/N")
	respuesta = input ()

	respuesta = verificarRespuesta(respuesta)

	if (respuesta == 'S'):
		fichero1.incluir_fichero("\r" + mensaje)
	else:
		fichero1.incluir_fichero(mensaje)

print("¿Desea crer un fichero? S/N")
respuesta = input ()

respuesta = verificarRespuesta(respuesta)



if (respuesta == 'S'):

	print("Ingrese nombre fichero")
	nombre_fichero = input ()	

	fichero1 = moduloficheros.Fichero(nombre_fichero)
	print("Ingrese mensaje a grabar en fichero")
	mensaje = input()
	fichero1.grabar_fichero(mensaje)

	print("¿Desea leer el fichero? S/N")
	respuesta = input ()

	respuesta = verificarRespuesta(respuesta)

	if (respuesta == 'S'):
		texto = fichero1.leer_fichero()
		print(texto)

	print("¿Desea incorporar más datos al fichero? S/N")
	respuesta = input ()

	respuesta = verificarRespuesta(respuesta)

	if (respuesta == 'S'):
		incluirEnFichero()

		print("¿Desea incorporar más datos al fichero? S/N")
		respuesta = input ()

		respuesta = verificarRespuesta(respuesta)

		while (respuesta == 'S'):
			incluirEnFichero()
			print("¿Desea incorporar más datos al fichero? S/N")
			respuesta = input ()

			respuesta = verificarRespuesta(respuesta)

print("¿Desea leer el fichero final? S/N")
respuesta = input ()

respuesta = verificarRespuesta(respuesta)

if (respuesta == 'S'):
	texto = fichero1.leer_fichero()
	print(texto)