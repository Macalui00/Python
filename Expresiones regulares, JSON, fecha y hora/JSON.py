#JSON: es una forma de almacenar e intercambiar datos que estan en formato texto.
"""Muy utilizado entre las empresas para intercambiar datos entre ellas.
veamos algunos ejemplos:"""

#convertir datos de un diccionario Python a una estructura JSON.
producto1 = {"nombre": "silla", "color":"blanco", "precio":80}

#Para esto utilizamos una libreria en Python que se llama JSON
import json

estructura_json = json.dumps(producto1) #este metodo dumps nos devuelve una estructura json

print(estructura_json)
#Como se puede apreciar, es muy similar al diccionario, pero no podemos acceder a los elementos,
#porque no es un diccionario realmente.

#estructura_json["nombre"] da error

#Es como una cadena de caracteres y en este caso si podemos acceder por posicion.
#es una cadena de caracteres que tiene un formato especial.
print(estructura_json[0])

#Ahora vamos a hacer lo contrario: vamos a convertir una estructura JSON que nos envian en un diccionario en python.
producto2 = json.loads(estructura_json) #permite cargar una estructura json en python y devuelve una estructura en python

print(producto2)

#podemos ver que nos volvio a generar una estructura diccionario donde efectivamente si podemos acceder a sus variables
print(producto2["precio"])