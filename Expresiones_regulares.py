"""EXPRESIONES REGULARES: es una secuencia de caracteres que forman una busqueda por patron, sirve para verficar si una cadena de texto contiene el patron buscado.

"""
import re #Importar el modulo de expresiones regulares.

texto = "Hola, mi nombre es Macarena"

#permite buscar la cadena de texto que queramos dentro del texto
print(re.search("nombre", texto))
#Busca esa serie de caracteres y si lo encuentra, devuelve un objeto de tipo match diciendo que lo ha encontrado
#Si no ha encontrado nada, no devuelve nada.

#Si esto lo asignamos a una variable:
resultado = re.search("nombre", texto)
#y preguntamos si resultado existe, es decir que lo ha encontrado
if (resultado):
	print("Cadena encontrada.")
else:
	print("Cadena no encontrada.")
#Con el search tambien podemos utilizar una serie de comodines o caracteres especiales para buscar cosas mas particulares.
print(re.search("Macarena$", texto))
#Buscar la palabra Macarena pero al final, con el signo dollar, busca en la cadena texto si hay alguna frase
#que termine con la palabra Macarena.

#Tambien le podemos decir que empiece por Hola
print(re.search("^Hola", texto))
#^ con ese simbolo al principio indicamos que busque en texto alguna oracion que empiece con Hola.

#Tambien podemos buscar preguntando por varias partes.
#Ejemplo: que tenga mi y es
print(re.search("mi.*es", texto))
#entre medio de mi y es puede haber varios caracteres, por ende pongo . que es cualquier cosa y * para indicar que
#puede haber mas de un caracter cualqueira en el medio.

#Segundo caso: Findall: busca todas las ocurrencias en una cadena.
#Escribimos un texto en varias lineas, y le ponemos triple comillas para que nos deje escribir en mas de una linea sin que nos de error.
texto = """
El coche de luis es rojo,
el coche de Antonio es blanco,
y el coche de Mariia es rojo"""

print(re.findall("coche.*rojo", texto)) #devuelve una lista con todas las ocurrencias que encuentra.

#El split devuelve una cadena a partir de un patron.

texto = "La silla es blanca y vale 80"
re.split("\s") #\s significa espacio en blanco, y lo vamos a utilizar como patron

#Por ultimo tenemos el sub: substituye todas las coincidencias de una cadena
re.sub("blanca", "roja", texto)
#indico lo que quiero cambiar, por que cosa lo quiero cambiar y la cadena de caracteres.