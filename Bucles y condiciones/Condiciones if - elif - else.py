#Condiciones If, elif, ese

a = 8
b = 4
c = 2
d = 6

print(a > b)
print(a < b)

if (a > b):
	print("a es mayor que b")

if(a < b):
	print("a es menor que b")

if (a > c) and (b < d):
	print("la expresión es correcta")

if (a > c) and (b > d): #segundo termino falso, tonces nunca se muestra por pantalla nada
	print("la expresión es correcta")
	#Pero si le agregamos un else
else:
	print("La primera expresión NO es correcta")

#ahora veremos el elif seria un else if:

if (a > b):
	print("a es mayor que b")
elif (a == b):
	print("a es igual a b")
else:
	print("a es menor que b")