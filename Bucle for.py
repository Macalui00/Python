#bucle for usado para iterar sobre una secuencia de elementos.

colores = ["rojo", "verde", "azul"]

for color in colores:
	print(color)

cadena = "Hola mundo"

for caracter in cadena:
	print(caracter)

#tambien podemos iterar sobre un rango de valores
range(0,8) #rango de valores que va del 0 al 7
for numero in range(8):
	print(numero)

#Si queremos que vaya de 2 en 2
for numero in range(3,8,2): #en el rango de 3 a 7 que recorra de 2 en 2
	print(numero)

#tambien funciona el break = para parar el bucle, por ejemplo:
for numero in range(10):
	if (numero == 5): #imprimirá solo hasta el 4
		break
	print(numero)

#Tambien sirve el continue = para parar solo la interacion actual
for numero in range(10):
	if (numero == 6):
		continue #para el numero 6 quiero que no continues y vayas directo al 7, osea se saltea el 6
	print(numero)

#for doble o doble for
for numero1 in range(4): #numero1 de 0 al 3
	for numero2 in range(3): #numero2 de 0 al 2
		print(numero1,numero2)