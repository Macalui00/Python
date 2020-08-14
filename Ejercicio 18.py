"""Ejercicio 18:
Tenemos 3 clases: "clase1", "clase2", "clase3"
Vamos a generar un número aleatorio de alumnos por clase
Para obtener un numero aleatorio utilizar:
	np.random.randint(minimo, maximo, numero): obtener un numero de enteros dentro del rango minimo y maximo.

Crear una serie de clases y alumnos.
Utilizar el indice de la serie creada para saber el numero de alumnos de la clase2
"""
import pandas as pd 
import numpy as np 

def mostrarClases(serie):
	print("¿Desea obtener la cantidad de alumnos de todas las clases? S/N")
	respuesta = str(input())
	while (respuesta != 'S') and (respuesta != 'N'):
		print("Respuesta incorrecta. Ingrese S/N")
		respuesta = str(input())
	if (respuesta == 'S'):
		print(serie)
		print("¿Desea ver una clase? S/N")
		respuesta = str(input())
		while (respuesta != 'S') and (respuesta != 'N'):
			print("Respuesta incorrecta. Ingrese S/N")
			respuesta = str(input())
		if (respuesta == 'S'):
			mostrarClase(serie)
	else:
		mostrarClase(serie)

def mostrarClase(serie):
		try: 
			print("¿Que clase desea ver?")
			num = int(input())
			print(serie["clase"+str(num)])
		except:
			print("Ups! ha ocurrido un error")
			mostrarClase(serie)
		else:
			print("Desea ver otra clase?")
			respuesta = str(input())
			while (respuesta != 'S') and (respuesta != 'N'):
				print("Respuesta incorrecta. Ingrese S/N")
				respuesta = str(input())
			if respuesta == 'S' :
				mostrarClase(serie)

def crearAlumnos(cantClases):
	lista_alumnos = []
	lista_alumnos = np.random.randint(0, 40, cantClases)
	return lista_alumnos

def crearClases(cantClases):
	lista_clases = []
	while (cantClases > 0):
		elemento = "clase" + str(cantClases)
		lista_clases.append(elemento)
		cantClases = cantClases - 1
	return lista_clases

print("¿Cuantas clases hay?")
cantClases = int(input())
lista_clases = crearClases(cantClases)
lista_alumnos = crearAlumnos(cantClases)
serie = pd.Series(lista_alumnos, index= lista_clases)
mostrarClases(serie)





