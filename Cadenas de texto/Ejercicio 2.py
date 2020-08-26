#Ejercicio 2

#Crear una variable cadena que contiene: "Esto es un texto de ejemplo"
#crear una variable longitud que contiene la longitud / numero de caracteres de la variable cadena
#crear una variable mayuscula que contiene la variable "cadena" en mayusculas
#crear una variable resultado que contenga la variable mayusculas y la variable resultado convertida a string

cadena = "Esto es un texto de ejemplo"
def obtenerLongYMayusculas (cadenaDeseada):
	longitud = len(cadenaDeseada)
	mayuscula = cadenaDeseada.upper()
	return print(f"La cadena en mayuscula es {mayuscula} y la longitud es {longitud}")

obtenerLongYMayusculas(cadena)

