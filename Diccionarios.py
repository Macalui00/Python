#Diccionarios: un diccionario es una coleccion de elementos que estan indexados, no estan ordenados, y se pueden modificar.
#Son escritos entre {} y estan formados por pares de elementos clave valor. A continuación, algunos ejemeplos:

diccionario_colores = {"red":"rojo","blue":"azul","yellow":"amarillo"}
print(diccionario_colores)

#Muestra por pantalla el valor que tiene este diccionario para la clave red.
print(diccionario_colores["red"]) 

valor = diccionario_colores["yellow"]
print(valor)

#Podemos añadir tambien elementos a un diccionario de la siguiente manera
diccionario_colores["black"] = "negro" #Para la clave black le asignamos el color negro.
print(diccionario_colores)

#Tambien podemos borrar valores, para lo cual hacemos lo siguiente:
diccionario_colores.pop("yellow")
print(diccionario_colores)

#Existe otra forma de borrar valores con el metodo del:
del(diccionario_colores["black"])
print(diccionario_colores)

for color in diccionario_colores:
	print (color) #muestra las claves del diccionario.

#para mostrar clave y valor necesito dos variables en el for:
for clave, valor in diccionario_colores.items():
	print(clave,valor)