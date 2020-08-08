#SQLite3 = Actualizar datos en nuestra tabla PERSONAS

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

print("""-------------------------------------------------------------------
			Antes de actualizar datos
-------------------------------------------------------------------""")

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
personas_ordenadas = cursor.fetchall()

for persona in personas_ordenadas:
	print(persona)

#Actualizamos los años de pedro de 26 a 22
cursor.execute("UPDATE PERSONAS SET edad = 22 WHERE nombre = 'Pedro'")

print("""-------------------------------------------------------------------
			Después de actualizar datos
-------------------------------------------------------------------""")

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
personas_ordenadas = cursor.fetchall()

for persona in personas_ordenadas:
	print(persona)

conexion.commit()

conexion.close()