#SQLite3 = Borrar datos en nuestra tabla PERSONAS

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

print("Antes de borrar datos")

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
personas_ordenadas = cursor.fetchall()

for persona in personas_ordenadas:
	print(persona)

#BORRAR AQUELLA LINEA QUE TENGA EL NOMBRE IGUAL A PAULA:
cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Paula'")

print("Despues de borrar datos")
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
personas_ordenadas = cursor.fetchall()

for persona in personas_ordenadas:
	print(persona)

conexion.commit()
conexion.close()