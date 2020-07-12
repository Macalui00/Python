#Ejercicio 3

#Crear una variable numero1 que contiene el valor 5
#Crear una variable numero2 que contiene el valor 6
#Crear una variable uma que contiene la suma de las dos variables anteriores
#imprimir por pantalla el resultado

def sumaDeEnteros(x,y):
	return int(x)+int(y)

print("Introduzca numero 1")
numero1 = input ()
print("Introduzca numero 2")
numero2 = input()

print(f"La suma de los numeros {numero1} y {numero2} es: {sumaDeEnteros(numero1,numero2)}")