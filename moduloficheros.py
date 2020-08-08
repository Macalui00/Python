"""
Crear el modulo "moduloficheros.py"
	Crear una clase "Fichero"
	Crear la funcion "leer_fichero" para leer un fichero de texto
	Crear la funcion "grabar_fichero" para crear un fichero de texto
	Crear la funcion "incluir_fichero" para incluir datos al final de un fichero de texto
"""

class Fichero:
	#que va a tener un metodo
	def __init__(self, nombre):
		self.nombreFichero = nombre 

	def leer_fichero(self): 
		fichero = open(self.nombreFichero, "rt")
		datos_fichero = fichero.read()
		return datos_fichero

	def grabar_fichero(self, texto):
		fichero = open(self.nombreFichero, "wt")
		fichero.write(texto)
		fichero.close()


	def incluir_fichero(self,linea): 
		fichero = open(self.nombreFichero, "at")
		fichero.write(linea)
		fichero.close()
		