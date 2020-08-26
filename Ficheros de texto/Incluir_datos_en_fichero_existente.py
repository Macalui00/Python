#ahora vamos a grabar información en un fichero de texto ya existente
#Imaginemos que al archivo de texto de ejemplo le queremos agregar una tercera linea.

fichero = open("fichero_ejemplo.txt", "at") #modo de abrir: a de append y t de texto

#cadena_para_incluir = "Esta es la tercera fila del fichero"
"""Si esto lo dejamos asi tal cual, lo va a incluir inmediatamente al lado de la segunda linea del fichero
y, si lo que quiero es que quede en la tercera linea, tenemos incluir un retorno de carro, osea un enter: /r"""
cadena_para_incluir = "\rEsta es la tercera fila del fichero"
fichero.write(cadena_para_incluir)

fichero.close()