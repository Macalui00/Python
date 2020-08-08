#SQLite3 = consultar datos que cumplen con determinada condicion

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

#Que nos devuelva aquellas personas de 36 años para arriba:
cursor.execute("SELECT nombre, apellido1 FROM PERSONAS WHERE edad >= 36")
#Lo que hacemos ahora mediante el cursor es que recogemos todos los resultados con el fetchall:
personas_seleccionadas = cursor.fetchall()
#Recogemos todas las filas y columnas del resultado y lo asignamos a una variable llamada personas_seleccionadas

for persona in personas_seleccionadas:
	print(persona)

#En este caso no hemos hecho cambios, por ende no es necesario realizar commit

conexion.close()