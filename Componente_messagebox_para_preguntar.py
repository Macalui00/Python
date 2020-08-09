# tkinter - Componente messagebox para realizar una pregunta
#Lo vamos a usar para hacer una pregunta de si o no.

import tkinter
#Para usar el messagebox es importante importarlo
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def preguntar():
	#generamos el messagebox que hará una pregunta (se genera una ventana): dos parametros:
	#El titulo de la pregunta
	#Y la pregunta
	resultado = tkinter.messagebox.askquestion("Titulo de la pregunta", "¿Quiere borrar este fichero?")
	if (resultado == "yes"):
		print("Si, quiero borrar el fichero")
	else:
		print("No, no quiero borrar el fichero")

#Creamos una ventana para preguntar o confirmar algo
boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
boton.pack()

raiz.mainloop()