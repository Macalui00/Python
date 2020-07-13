#Ejercicio 4

#nota1 = 6
#nota2 = 4
#nota3 = 7
#nota_media: el promedio de las 3 notas
#nota_final: "Aprobado" si nota_media >= 5

print("Introduzca nota 1")
nota1 = input ()
print("Introduzca nota 2")
nota2 = input ()
print("Introduzca nota 3")
nota3 = input ()

def obtenerNotaFinal(n1,n2,n3):
	nota_media = (int(n1)+int(n2)+int(n3)) / 3
	if (nota_media >= 5):
		return "Aprobado"
	else:
		return "Desaprobado"

print(f"Usted esta: {obtenerNotaFinal(nota1,nota2,nota3)}")