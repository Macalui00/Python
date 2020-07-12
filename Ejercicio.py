#Ejercicio

#Crear una variable cadena que contiene el texto: "Esto es un texto de ejemplo"
#Segun la posicion de cada letra en la cadena, calcular que valores (x,y) se necesitan para obtener solo la palabra "texto"

cadena = "Esto es un texto de ejemplo"
palabra = "texto"
x=0
y = len(cadena)
def calcular(x,y):
	if (cadena[x:y] == palabra):
		return print("¡exito!, retorno: " + cadena[x:y] + f" la posicion era x={x}, y={y}")
	if (cadena[x:y] != palabra):
		calcular(x+1,y-1)


calcular(0,len(cadena))