#Crear una funcion lambda que calcule la media de 3 notas

resultado = lambda nota1, nota2, nota3 : (nota1+nota2+nota3)/3

print("¿Desea calcular el promedio de 3 notas? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Desea calcular el promedio de 3 notas? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):

	print("Introduzca nota 1")
	nota1 = input ()
	print("Introduzca nota 2")
	nota2 = input ()
	print("Introduzca nota 3")
	nota3 = input ()

	print(f"El promedio es {resultado(int(nota1),int(nota2),int(nota3))}")

	print("¿Desea calcular otro promedio? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Desea calcular otro promedio? S/N")
		respuesta1 = input ()

while (respuesta1 == 'S'):

	print("Introduzca nota 1")
	nota1 = input ()
	print("Introduzca nota 2")
	nota2 = input ()
	print("Introduzca nota 3")
	nota3 = input ()

	print(f"El promedio es {resultado(int(nota1),int(nota2),int(nota3))}")

	print("¿Desea calcular otro promedio? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Desea calcular otro promedio? S/N")
		respuesta1 = input ()
