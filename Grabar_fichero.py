#Vamos a grabar un fichero de texto que no existe

#Mediante el metodo open, le damos el nombre del fichero que queramos que tenga nuestros datos.
fichero = open("fichero_para_grabar.txt", "wt") #y el metodo W de escribir y T de texto
#devuelve un puntero o acceso al fichero que ha creado.

#Luego con la variable fichero, mediante el metodo write, escribimos el texto que queramos.
#ejemplo una cadena de texto:

texto_de_fichero = "Hola, esta es la línea que vamos a grabar en el fichero de texto"

fichero.write(texto_de_fichero)

fichero.close() #lo ultimo que queda es cerrar el fichero para que no quede abierto.

