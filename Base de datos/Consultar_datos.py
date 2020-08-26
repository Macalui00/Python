#SQLite = consultar datos de nuestra tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")
#Lo que hacemos ahora mediante el cursor es que recogemos todo con el fetchall:
personas = cursor.fetchall()
#Recogemos todas las filas y columnas de la tabla y lo asignamos a una variable llamada personas

for persona in personas:
	print(persona)

#En este caso no hemos hecho cambios, por ende no es necesario realizar commit

conexion.close()