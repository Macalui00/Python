# tkinter - Componente text (campo de texto largo, de varias lineas, para introducir texto por teclado)
#Por ejemplo, para un campo comentarios.

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos nuestro componente text (Texto largo de varias lineas)

entrada = tkinter.Text(raiz)
entrada.config(width = 20,height = 10, font = ("Verdana", 15), padx=10, pady=10, fg = "green", selectbackground = "lightgrey")
#Numero de letras que va a tener de ancho va a ser 20
#Espaciado, desde que empieza el campo, hasta que empiezan las letras de contenido. Padx y Pady de Padding
#Podemos tambien configurar el color si seleccionamos el texto para copiarlo o lo que sea, pordemos cambiarle el color de fondo
entrada.pack()

raiz.mainloop()