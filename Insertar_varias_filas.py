#SQLite3 = Insertar varios registros a la vez en nuestra tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()

#Vamos a crear una lista de usuarios / personas que queremos añadir:
lista_personas = [('Pedro', 'Rodriguez', 'Perez', 26),
				  ('Evangelina', 'Anderson', 'Gimenez', 36),
				  ('Josefina', 'Ramirez', 'Altamirano', 44),
				  ('Paula', 'Pareto', 'Rocca', 36)]

#Vamos a ejecutar una sentencia que se repetirá varias veces
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

conexion.commit()

conexion.close()