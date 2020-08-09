"""	Crear la funcion Primos que sera una funcion generadora de numeros primos entre 0 y 100
Esta es la lista de numeros primos entre 0 y 100:
no la voy a pasar...
Utilizar la funcion generadora para mostrar por pantalla numeros primos menores de 50
"""
def primo(numero):
	divisor = numero
	contador = 1
	if (numero < 1):
		return False
	elif (numero == 2):
		return True
	else:
		while (divisor > 1):
			if ((numero%divisor) == 0):
				contador = contador + 1
			divisor = divisor - 1
		if(divisor == 1):
			if (contador > 2):
				return False
			else:
				return True


#resultado = primo(4)
#print(resultado)

def primos(numero):
	for i in range(0,numero):
		if (primo(i)):
			yield i 

#lista = list(primos(50))
#print(lista)

def ingresoDatos():
	
	try:
		print("Ingrese tope")
		tope = int(input ())
	except ValueError:
		print("Dato erroneo ingresado")
		ingresoDatos()
	except:
		print("Ups! ha ocurrido un error")
		ingresoDatos()
	else:
		lista = list(primos(tope))
		print(lista)

def continuar():
	print("¿Desea realizar otra operacion? S/N")
	respuesta = input ()
	while (respuesta != 'S') and (respuesta != 'N'):
		print("Respuesta incorrecta. Ingrese S/N")
		respuesta = input ()
	return respuesta

#Ejecucion
ingresoDatos()

respuesta = continuar()
while (respuesta == "S"):
	ingresoDatos()
	respuesta = continuar()
print("""-------------------------------------------------------------
		FIN DEL PROCESO
-------------------------------------------------------------""")
