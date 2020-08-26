''' Creamos una variable nota que tenga el valor 4.5
Creamos una variable "trabajo_realizado" que tenga el valor "si"
Calcular el valor de la variable "nota_final", teniendo en cuenta que, si la nota es mayor o igual a 4,
y el valor de la variable "trabajo_realizado" es igual a "si", entonces nota_final sera igual a aprobado, en caso contrario
sera igual a suspendido

'''

print("¿Desea determinar la nota de un alumno? S/N")
respuesta1 = input ()

while (respuesta1 != 'S') and (respuesta1 != 'N'):
	print("Respuesta incorrecta. ¿Desea determinar la nota de un alumno? S/N")
	respuesta1 = input ()

if (respuesta1 == 'S'):

	print("Introduzca el nombre del alumno")
	nombre = input ()
	print("Introduzca la nota")
	nota = input ()
	print("¿El trabajo ha sido realizado? si/no")
	trabajo_realizado = input ()

	while (trabajo_realizado != 'si') and (trabajo_realizado != 'no'):
		print("Respuesta incorrecta. ¿El trabajo ha sido realizado? si/no")
		trabajo_realizado = input ()

	if (float(nota) >= 4) and (trabajo_realizado == 'si'):
		nota_final = "aprobado"
	else:
		nota_final = "desaprobado"

	print(f"{nombre} ha {nota_final}")

	print("¿Desea determinar la nota de otro alumno? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Desea determinar la nota de otro alumno? S/N")
		respuesta1 = input ()

while (respuesta1 == 'S'):

	print("Introduzca el nombre del alumno")
	nombre = input ()
	print("Introduzca la nota")
	nota = input ()
	print("¿El trabajo ha sido realizado? si/no")
	trabajo_realizado = input ()

	while (trabajo_realizado != 'si') and (trabajo_realizado != 'no'):
		print("Respuesta incorrecta. ¿El trabajo ha sido realizado? si/no")
		trabajo_realizado = input ()

	if (float(nota) >= 4) and (trabajo_realizado == 'si'):
		nota_final = "aprobado"
	else:
		nota_final = "desaprobado"

	print(f"{nombre} ha {nota_final}")

	print("¿Desea determinar la nota de otro alumno? S/N")
	respuesta1 = input ()

	while (respuesta1 != 'S') and (respuesta1 != 'N'):
		print("Respuesta incorrecta. ¿Desea determinar la nota de otro alumno? S/N")
		respuesta1 = input ()
