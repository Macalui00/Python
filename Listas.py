#listas: proyeccion de elementos ordenados y que se puede modificar.

colores = ["rojo","amarillo","verde"]
print(colores) #comillas dobles y simples equivalentes

#modificar un elemento de la lista:
print(colores[0])

#modificar amarillo
print(colores[1])
colores[1] = "azul"
print(colores)

#len tamaño de una lista:
print(f"tamaño de la lista es de: {len(colores)}")

#append agregar un elemento al final de la lista:
print(colores)
colores.append("naranja")
print(colores)

#borrar valores.
colores.remove("rojo")
print(colores)

#si queremos recorrer una lista, lo podemos hacer con el bucle for.
for color in colores:
	print(color)

#borrar todos los elementos de la lista
colores.clear[]

#existen muchas mas funciones obviamente.