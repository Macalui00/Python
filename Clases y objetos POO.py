#Clases y objetos. Programacion orientada a objetos. POO

#Clase es como un constructor de objetos.

#class NombreClase
class ClaseSilla:
	#atributos o propiedades:
	color = "blanco"
	precio = 100

#objetoSilla1 objeto fisico de la clase silla
objetoSilla1 = ClaseSilla()

print(objetoSilla1.color)

objetoSilla2 = ClaseSilla()
objetoSilla2.color = "verde"
objetoSilla2.precio = 120

print(objetoSilla2.color)
print(objetoSilla2.precio)

class Persona:
	#que va a tener un metodo
	def __init__(self,nombre,edad):
	#cada uno de los objetos de esta clase que van a tener unos atributos que son el nombre y la edad.
		self.nombre = nombre #y cuando creemos una instancia de esta clase asignaremos estos dos valores
		self.edad = edad

	def saludar(self): #self hace referencia a los atributos de la clase.
		print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Macarena",25)

print(persona1.edad)
print(persona1.nombre)

persona1.saludar()