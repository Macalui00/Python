class Auto:
	
	def __init__(self,marca,color, combustible, cilindrada):
		self.marca = marca
		self.color = color
		self.combustible = combustible
		self.cilindrada = cilindrada

	def mostrar_caracteristicas(self): 
		print(f"El auto es de marca {self.marca} y color {self.color}, utiliza {self.combustible} con una cilindrada de {self.cilindrada}")

resultado = lambda nota1, nota2, nota3 : (nota1+nota2+nota3)/3
