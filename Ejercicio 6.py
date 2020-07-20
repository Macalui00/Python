''' Crear un diccionario con los siguientes pares de valores:
	manzana, apple
	naranja, orange
	platano, banana
	limon, lemon

Mostrar la traduccion para la palabra naranja
Añade un elemento nuevo con "piña" y "pineapple"
Haz un bucle para mostrar todos los elementos del diccionario
'''
print("¿Crearemos un diccionario? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):
	print("Introduzca la clave")
	clave = input ()
	print("Introduzca el valor")
	valor = input ()

	dic_frutas={clave:valor}

	print("¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()

while (respuesta1 == 'S'):

	print("Introduzca la clave")
	clave = input ()
	print("Introduzca el valor")
	valor = input ()

	dic_frutas[clave] = valor

	print("¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()

print("¿Desea introducir un nuevo elemento al diccionario? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):
	print("Introduzca la clave")
	clave = input ()
	print("Introduzca el valor")
	valor = input ()

	dic_frutas[clave] = valor

	print("¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()

while (respuesta1 == 'S'):

	print("Introduzca la clave")
	clave = input ()
	print("Introduzca el valor")
	valor = input ()

	dic_frutas[clave] = valor

	print("¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()

print("¿Mostraremos la traduccion de algun elemento? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):
	print("Introduzca la clave")
	clave = input ()
	print(f"La traduccion de {clave} es {dic_frutas[clave]}")

	print("¿Mostraremos la traduccion de algun otro elemento? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()

while (respuesta1 == 'S'):

	print("Introduzca la clave")
	clave = input ()
	print(dic_frutas[clave])

	print("¿Mostraremos la traduccion de algun otro elemento? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()

print("¿Desea mostrar todos los elementos del diccionario? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):
	for clave, valor in dic_frutas.items():
		print(f"La palabra {clave} se traduce como {valor}")

print("¿Desea volver a mostrar todos los elementos? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
	respuesta1 = input ()

while (respuesta1 == 'S'):

	for clave, valor in dic_frutas:
		print(f"La palabra {clave} se traduce como {valor}")

	print("¿Desea volver a mostrar todos los elementos? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Insertaremos otro valor al diccionario? S/N")
		respuesta1 = input ()