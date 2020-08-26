# tkinter - Componente messagebox (mostrar información): serian pop-ups, ventanas con mensajes, información.

import tkinter
#Para usar el messagebox es importante importarlo
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
	#generamos el messagebox que muestra info: dos parametros:
	#El titulo de la ventana
	#Y el mensaje que aparecera en la ventana
	tkinter.messagebox.showinfo("Titulo", "Mensaje con la información")

#Creamos el componente messagebox
boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()

raiz.mainloop()