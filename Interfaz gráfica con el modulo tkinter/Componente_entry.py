# tkinter - Componente entry: es un campo de texto corto para la entrada de datos por teclado

import tkinter


raiz = tkinter.Tk()
raiz.title("Mi programa")

"""Creamos nuestro componente entry (entrada de datos) """
entrada = tkinter.Entry(raiz)
entrada.config(justify= "center", show="*")
entrada.pack()

#es un campo de entrada de datos de una unica linea, por ejemplo, para un formulario para introducir datos. 
#Si este campo en vez de ser texto quisieramos que fuese tipo password para que no se viese el valor que
#estamos introduciendo, pues tendriamos que ponerle en la configuracion que siempre que ingresamos los datos
#muestre(show) siempre el valor *

raiz.mainloop()