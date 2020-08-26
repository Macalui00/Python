#Dada la siguiente lista de numeros: lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
#Mostrar mediante el metodo print y el operador in si el numero 21 esta en la lista:

import os
import sys

print("Introduzca la lista")
lista = input()
print("Introduzca el numero que desea buscar")
numero = int(input ())

#Convierto el string en una lista de char
lista2 =lista.replace('[','').replace(']','').split(',')
print(lista2)

#convierto la lista de char en lista de ints
lista3 = [int(a) for a in lista2] 
print(lista3)

def perteneceALista(lista,numero):
	for elemento in lista:
		if (elemento == numero):
			return "pertenece"
	return "no pertenece"

print(f"El numero {numero} {perteneceALista(lista3,numero)} a la lista")

# https://www.it-swarm.dev/es/python/como-hacer-una-lista-desde-un-raw-input-en-python/1046218648/
# https://kite.com/python/answers/how-to-split-a-string-into-a-list-of-integers-in-python#:~:text=Use%20str.,split%20a%20string%20into%20integers&text=Use%20map(func%2C%20list),by%20map%20to%20a%20list

# print(map(int, "[1,2,3]".replace('[', '').replace(']', '').split(',')))
# Quitamos los "[" y "]"
# Hacemos un split() por la , para obtener una lista
# Solo falta convertir cada elemento en un int, lo hacemos con map(lista, int)
# sacado de: https://es.stackoverflow.com/questions/202356/string-to-list-en-python
