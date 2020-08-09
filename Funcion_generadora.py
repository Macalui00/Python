#Funcion generadora: aquella que genera valores sobre la marcha
print("------- Range -------")
range(0,11)

for numero in range(0,11):
	print(numero)

#Range seria una funcion generadora
print("------- Pares -------")
#Pero ahora vamos a generar una funcion generadora propia y la vamos a llamar pares.
def pares(maximo):
	for numero in range(0,maximo):
		if (numero % 2 == 0):
			yield numero #devolver un numero: yield, en vez de un return, la funcion generadora utiliza el yield

maximo = 11
for numero in pares(maximo):
	print(numero)