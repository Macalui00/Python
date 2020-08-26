# tkinter - Componente button (botón)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")
"""
Creamos el componente button, para ejecutar una acción cuando se pulsa.
text, lo vamos a llamar ejecutar. El comando que tiene que ejecutar, que en nuestro
caso será una funcion que le vamos a llamar accion (la tenemos que definir por encima del boton)"""

#Definimos la funcion accion
def accion():
	print("Hola Mundo")

boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()


raiz.mainloop()