"""
Crear una base de datos "basededatos.db"
Crear una tabla productos con 3 campos
	id : identificador del producto de tipo numerico.
	nombre : nombre del producto del tipo texto
	precio : precio del producto del tipo numerico.

Insertar 3 productos en la tabla "productos"
	1,"Impresora",300
	2,"Raton",20
	3,"Ordenador",600

Consultar los productos de la tabla "productos"
Cerrar la base de datos.

"""
import sqlite3

def grabar_fichero(archivo,texto):
		fichero = open(archivo, "wt")
		fichero.write(texto)
		fichero.close()

def incluir_fichero(archivo,texto): 
	fichero = open(archivo, "at")
	fichero.write(texto)
	fichero.close()

conexion = sqlite3.connect("basededatos.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER, nombre TEXT, precio REAL)")

print("Ingrese nombre de archivo")
archivo = input ()

texto ="""-------------------------------------------------------------------
			Base antes de ingresar datos a la tabla
----------------------------------------------------------------------------"""

print(texto)
try:
	grabar_fichero(archivo,texto)
except:
	print("Error de grabar encabezado de archivo.")
else:
	print("Cabecera grabada correctamente.")

cursor.execute("SELECT * FROM PRODUCTOS ORDER BY id")
productos_ordenados = cursor.fetchall()

for producto in productos_ordenados:
	print(producto)
	try:
		incluir_fichero(archivo, "\r" + str(producto))
	except:
		print("Error al grabar los datos en el archivo.")
	finally:
		print("Fin del proceso de grabado")

lista_productos = [(1,"Impresora",300.00),
				  (2,"Raton",20.00),
				  (3,"Ordenador",600.00)]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_productos)

texto ="""\r-------------------------------------------------------------------
			Base despues de ingresar datos a la tabla
----------------------------------------------------------------------------"""

print(texto)
try:
	grabar_fichero(archivo,texto)
except:
	print("Error de grabar encabezado de archivo.")
else:
	print("Cabecera grabada correctamente.")

cursor.execute("SELECT * FROM PRODUCTOS ORDER BY id")
productos_ordenados = cursor.fetchall()

for producto in productos_ordenados:
	print(producto)
	try:
		incluir_fichero(archivo, "\r" + str(producto))
	except:
		print("Error al grabar los datos en el archivo.")
	finally:
		print("Fin del proceso de grabado")

conexion.commit()

conexion.close()


