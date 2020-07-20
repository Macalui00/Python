#Funciones: bloque de codigo que se ejecuta cuando es llamado.

def saludar():
	print("Buenos días")

saludar()

def saludar(nombre):
	print("Buenos días " + nombre)

nombre = "Macarena"

saludar(nombre)

#Una funcion tambien puede devolver un valor.

def sumar (numero1, numero2):
	suma = numero1 + numero2
	return suma

numero1 = 5
numero2 = 7
resultado = sumar(numero1, numero2)
print(resultado)

#Pasar dos valores como parametros y uno de ellos sera un paso de valor por referencia:
numeros = [1,2,3,4,5]
print(numeros)

def incluirNumero(numeros, num): #como es una coleccion de numero que pasamos como referencia, la funcion la puede modificar
	numeros.append(num)

numero = 18
incluirNumero(numeros, numero)
print(numeros)

