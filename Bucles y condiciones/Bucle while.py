#Con el bucle while podemos ejecutar un conjunto de acciones mientras la condicion sea verdadera

valor = 1
fin = 10
while (valor < fin):
	print(valor)
	valor = valor + 1

#breack
while (valor < fin):
	print(valor)
	valor = valor + 1
	if (valor == 5):
		break #detiene el bucle

#continue
while (valor < fin):
	valor = valor + 1
	if (valor == 6):
		continue
	print(valor) #caso contrario a 6, se imprime por pantalla


