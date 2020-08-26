#Filter - es una funcion para filtrar resultados según una condicion. A partir de una lista y una funcion condicional
#Y el resultado será otra lista con los elementos que cumplen esa condicion.

#Definimos la funcion condicional que nos filtrará los resultados
def positivo(numero):
	if (numero > 0):
		return True
	else:
		return False

positivo(5)
positivo(-3)

#Creamos una lista de numeros:
numeros = [4,-2,8,-3,-5,-7,1,9]

positivos = filter(positivo, numeros)
resultado = list(positivos)
print(resultado)