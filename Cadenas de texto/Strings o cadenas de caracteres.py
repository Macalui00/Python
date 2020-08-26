#Strings: representa una serie de caracteres y va entre comillas dobles o simples

cadena = "Hola mundo"
print(cadena)

#Esta cadena de caracteres esta ordenada, osea: el primer elemento es la H, el segundo es el 0, etc.

#si queremos que nos retorne la m (los espacios tambien cuentan):
print(cadena[5])

#tambien podemos acceder a la ultima posicion de la cadena.
print(cadena[-1]) #accedemos a la o (es un recorrido inverso).

#tambien podemos acceder a partes de una cadena indicando posicion inicial y posicion final.
print(cadena[2:7]) #va de la 2 a la 7, no estaria incluida la 7, osea, desde la posicion inicial hasta la posicion final -1.

#Tambien podemos omitir alguno de ellos:
print(cadena[2:]) #si no ponemos limite final, va de la posicion inicial indicada hasta el final de la cadena.

#los canales de caracteres son inmutables, es decir, no podemos acceder a una posicion concreta y cambiarle su valor a otro,
#ejemplo en la posicion 5 en vez de una m que sea una p

#osea se puede consultar pero no modificar.

#FUNCIONES DE CADENAS:

#Queremos saber cuantos caracteres tiene nuestra cadena
print(len(cadena))

#convertir una cadena a mayusculas
print(cadena.upper()) #Pero nuestra cadena sigue valiendo lo mismo que antes, es decir, haciendo esto solo mostramos la cadena en mayusculas.

#para que nos quede definitivamente en mayusculas tenemos que hacer:
cadena = cadena.upper()

#MOSTRAR LA CADENA EN MINUSCULAS:
print(cadena.lower()) 

#dividir la cadena en palabras:
print(cadena.split()) 

#queremos saber todas las frutas que hay en el siguiente string
cadena2 = "uva,pera,manzana,naranja"

#hacemos el split con el caracter coma (,)
print(cadena2.split(',')) 

#IMPRIMIR VARIABLES EN UNA CADENA:

nombre = "Macarena"
print("Buenas noches " + nombre)

#otra forma de hacerlo: con el .format:
edad = 23
print("Buenas noches {}, feliz {} cumpleaños".format(nombre,edad))

#Dos variables, queremos imprimir por pantalla, el texto de arriba,
#las llaves se van a sustituir por las variables marcadas como parametros del format.
#Importa el orden de las variables en el format.

#Si tenemos un numero con muchos decimales y queremos imprimirlo formateado con menos decimales:
resultado = 10 / 3
print(resultado)
print("El resultado es {r}".format(r=resultado))

#para que nos retorne un resultado con menos decimales, le colocamos despues de la r lo siguiente:
print("El resultado es {r:1.3f}".format(r=resultado)) #esto significa 1 de 1 entero y 3f de tres decimales.

#podemos buscar otra forma de imprimir una variable dentro de una cadena que es la funcion:
#f-strings:

print(f"Buenas noches {nombre}, feliz {edad} cumpleaños") #Con la f le indicamos que esta formateando, diciendole que los corchetes se sustituyen por las variables.
#Esto se hace con el f-strings que esta disponible a partir del python 3.6