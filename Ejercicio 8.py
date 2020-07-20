''' Crear una clase "Coche" que tenga estos atributos:
	marca, color, combustibles y cilindrada

	Crear la funcion "__init__" que asigna los parametros de la clase a los atributos de la clase

	crear ptra funcion "mostrar_caracteristicas" que mediante print muestre por pantalla las caracteristicas del coche

	Crear un objeto coche1 de la clase Coche con los atributos "Ope1" "rojo" "gasolina" "1.5"

	Ejecutar la funcion mostrar_caracteristicas del objeto coche1
'''

class Auto:
	
	def __init__(self,marca,color, combustible, cilindrada):
		self.marca = marca
		self.color = color
		self.combustible = combustible
		self.cilindrada = cilindrada

	def mostrar_caracteristicas(self): 
		print(f"El auto es de marca {self.marca} y color {self.color}, utiliza {self.combustible} con una cilindrada de {self.cilindrada}")

print("¿Desea introducir información de un auto? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Desea introducir información de un auto? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):

	print("Introduzca marca")
	marca = input ()
	print("Introduzca color")
	color = input ()
	print("Introduzca combustible")
	combustible = input ()
	print("Introduzca cilindrada")
	cilindrada = input ()

	auto1 = Auto(marca,color,combustible, float(cilindrada))

	print("¿Desea mostrar sus caracteristicas? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Desea determinar la nota de otro alumno? S/N")
		respuesta1 = input ()

	if (respuesta1 == 'S'):
		auto1.mostrar_caracteristicas()

