#SQLite3 = Insertar datos en nuestra tabla

import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()
#Como las sentencias a ejecutar van entre "" lo que haya dentro de ellas, si queremos utilizar comillas, tienen que ser ''
cursor.execute("INSERT INTO PERSONAS VALUES ('Antonio', 'Perez', 'Gomez', 18)")

#Para guardar definitivamente el cambio:
conexion.commit()

conexion.close()