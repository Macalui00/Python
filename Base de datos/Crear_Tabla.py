#Vamos a crear una nueva tabla en nuestra base de datos:

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

#utilizaremos un metodo cursor, este metodo se utiliza para crear un 
#objeto poder ejecutar luego sentencias sql dentro de la base de datos
cursor = conexion.cursor()

#Mediante el metodo execute nos permite ejecutar cualquier sentencia sql:
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

#UNA VEZ CREADA UNA TABLA, TENEMOS QUE HACER UN COMMIT
conexion.commit()

#por ultimo cerramos la conexion a nuestra base de datos.
conexion.close()