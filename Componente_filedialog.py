# tkinter - Componente filedialog para abrir un fichero

import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componente filedialog

def abrirFichero():
	#En ese caso pregunta por el nombre de un fichero y devolverá la ruta del fichero.
	rutaFichero = filedialog.askopenfilename(title="Abrir un fichero")
	print(rutaFichero)

#creamos primero un boton
boton = tkinter.Button(raiz, text="Pulsar para empezar", command=abrirFichero)
boton.pack()

raiz.mainloop()