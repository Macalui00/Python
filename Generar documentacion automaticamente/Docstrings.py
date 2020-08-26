#Docstrings - cadenas para documentación
#Cadenas para generar automaticamente documentación de nuestros programas en Python

def saludar(nombre):
	""" 
	Esto será un comentario de la funcion saludar.
	Esta funcion recibirá como parametro de una cadena con el nombre
	e imprimirá por pantalla un salido con el nombre concatenado.
	"""

	print("Buenos días" + nombre)

saludar("Macarena")
#Para ver la documentación de la funcion:
help(saludar)

class Saludos:
	"""
	Esta clase tendrá dos funciones: que serán buenos_dias y adios.
	Ambas funciones recibiran como parámetro un nombre.
	"""
	def buenos_dias(self, nombre):
		""" Esta función sirve para decir Buenos Días a una persona."""
		print(f"Buenos dias {nombre}")

	def adios(self, nombre):
		""" Esta función dice Adios a una persona."""
		print(f"Adios {nombre}")

saludo = Saludos()
saludo.buenos_dias("Macarena")
saludo.adios("Macarena")
help(Saludos)
help(Saludos.buenos_dias)
help(Saludos.adios)

#Este help se puede usar tambien para funciones predefinidas dentro de python:
help(print)
help(len)