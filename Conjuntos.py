#Conjuntos: coleccion de elementos pero que esta desordenado, no hay un indice para acceder a sus elementos.

conjunto_colores = {"rojo","verde", "amarillo"} #entre llaves sus elementos con comillas dobles y separados por comas

print(conjunto_colores)

for color in conjunto_colores:
	print(color)

#como esta desordenada y no posee indices, si queremos acceder a una posicion concreta del conjunto, dará un error.
#conjunto_colores[0] dará error porque no soporta la indexacion.

print(len(conjunto_colores))

#Podemos añadir elementos al conjunto mediante la funcion add:
conjunto_colores.add("negro")
print(conjunto_colores) #pero no lo añade al final, lo añade por el medio, ya que es un conjunto desordenado.

#tambien podemos borrar elementos:
conjunto_colores.remove("verde")
print(conjunto_colores)