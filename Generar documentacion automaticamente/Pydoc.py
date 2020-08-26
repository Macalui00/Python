#Pydoc - Geerar documentación automática desde la consola o Terminal de comandos

class Saludos:
	"""
	Esta clase tendrá dos funciones: que serán buenos_dias y adios.
	Ambas funciones recibiran como parámetro un nombre.
	"""
	def buenos_dias(self, nombre):
		""" Esta función sirve para decir Buenos Días a una persona."""
		print(f"Buenos dias {nombre}")

	def adios(self, nombre):
		""" Esta función dice Adios a una persona."""
		print(f"Adios {nombre}")

#Abrimos la terminal de comandos o consola. Buscamos nuestro archivo Pydoc.py
#Si queremos ejecutar la documentacion en el comando escribimos:
#pydoc (ruta del archivo)/nombrearchivo en este caso pydoc C:\Users\Macarena\Documents\Python\Python\Pydoc.py


""" EL COMANDO POSTA PARA EJECUTAR PYDOC: python -m pydoc Pydoc

Y OBTENGO LO SIGUIENTE POR CMD:

Help on module Pydoc:

NAME
    Pydoc - #Pydoc - Geerar documentaci¾n automßtica desde la consola o Terminal de comandos

CLASSES
    builtins.object
        Saludos

    class Saludos(builtins.object)
     |  Esta clase tendrß dos funciones: que serßn buenos_dias y adios.
     |  Ambas funciones recibiran como parßmetro un nombre.
     |
     |  Methods defined here:
     |
     |  adios(self, nombre)
     |      Esta funci¾n dice Adios a una persona.
     |
     |  buenos_dias(self, nombre)
     |      Esta funci¾n sirve para decir Buenos DÝas a una persona.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

PARA VER LOS COMENTARIOS EN LA PAGINA HTML ESCRIBIENDO EL COMANDO Y EXPORTANDOLO A HTML:
python -m pydoc <dir>

---------------------------------------------
El módulo Pydoc en Python se puede usar para generar documentación en forma de páginas html o incluso en la consola

python -m pydoc 
Este comando ofrece opciones como ver el archivo pydoc para un archivo, -k buscar diferentes bibliotecas, -p permite abrir una página en el navegador web para ver python paquetes, -g proporciona una interfaz gráfica para buscando documentación, -w escribe una salida html. A continuación se muestran los comandos de ejemplo que puede activar para probar.

python -m pydoc yourpythonfile
python -m pydoc -k ftplib
python -m pydoc -p 314
python -m pydoc -w file
He creado dos archivos de muestra en un directorio file1.py y file2.py que tiene un código simple con una sola línea de comentario.

def f2m(ft):
   	Return the number of meters eq to feet #Esto iba en triple comillas, por razones obvias las saque
    return 0.30 * ft
Una forma de ver el comentario de los archivos es simplemente escribir a continuación en el mismo archivo y puede ejecutar python file.py y se mostrarán los comentarios).

help(f2m)
Otra forma de ver esto es escribir el comando

python -m pydoc file1
Una forma más de ver los comentarios en una página html escribiendo este comando y exportándolo a html

python -m pydoc -w <dir>
Si tiene varios archivos python y desea generar HTML en una carpeta separada, entonces los comandos simples de Shell pueden hacer el trabajo. El siguiente código genera una carpeta 'htmldocs' y luego genera html y los mueve a esta nueva carpeta. Si abre cualquiera en la esquina superior derecha, puede ver la opción de índice a través de la cual puede navegar a través de otras páginas.

mkdir -p htmldocs
pydoc -w `find . -name '*.py'`
mv *.html htmldocs


https://www-it--swarm-dev.cdn.ampproject.org/v/s/www.it-swarm.dev/es/python/en-python-que-hace-pydoc/1043739672/amp/?usqp=mq331AQFKAGwASA%3D&amp_js_v=0.1#aoh=15969992312479&referrer=https%3A%2F%2Fwww.google.com&amp_tf=De%20%251%24s&ampshare=https%3A%2F%2Fwww.it-swarm.dev%2Fes%2Fpython%2Fen-python-que-hace-pydoc%2F1043739672%2F
"""