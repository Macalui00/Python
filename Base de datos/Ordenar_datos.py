#SQLite3 = Consultar datos y ordenarlos por alguna columna

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

#Que nos devuelva las personas ordenadas por edad:
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
#Lo que hacemos ahora mediante el cursor es que recogemos todos los registros con el fetchall:
personas_ordenadas = cursor.fetchall()
#Recogemos todas las filas y columnas de la tabla ordenados por edad y lo asignamos a una variable llamada personas_ordenadas

for persona in personas_ordenadas:
	print(persona)

#En este caso no hemos hecho cambios, por ende no es necesario realizar commit

conexion.close()