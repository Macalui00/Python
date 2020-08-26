#Leer el fichero de texto

#para leer el fichero ponemos open, y como parametros:
#nombre del fichero, el modo en el que lo abrimos, en este caso: r de lectura y una t de texto
fichero = open("fichero_ejemplo.txt", "rt")
#esta funcion open devuelve un puntero al fichero, y eso lo almacenamos en una variable

#para acceder a los datos del fichero:
datos_fichero = fichero.read()
#metodo del fichero: read() lo que hace es leer todo el contenido que esta dentro del fichero y guardarlo en la variable del fichero: datos_fichero

#para visualizar los datos del fichero:
print(datos_fichero)