#SQLite - Sistema de gestion de bases de datos relacionales.

#la vamos a usar desde python
#crearemos una base de datos desde python

import sqlite3

#Entre parentesis tenemos que poner el nombre de la base de datos
#si ya existe, o, el nombre de la base de datos nueva que queremos crear
conexion = sqlite3.connect("basededatos1.db") #conecta a una base de datos si existe, o la crea si no existe
#va a devolver el enlace a la base de datos

#Y esta variable conexion, nos servira para luego cerrar la base de datos y
#que no quede abierta, ya que sino puede generar problemas al abrir nuevamente.
conexion.close()

#Para abrir y manejar los archivos generados podemos utilizar el programa DB Browser for SQLite