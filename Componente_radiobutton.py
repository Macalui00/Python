# tkinter - Componente radiobutton (boton de seleccion múltiple)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos los radiobutton
"""Le pasamos como parametro:
	- Raiz
	- Texto que queremos que aparezca
	- Que asignará el valor 1 a la variable opcion.
	- y cuando pulsemos sobre esta opcion ejecutará tambien una funcion que se llama seleccionar."""
def seleccionar():
	print("La opción seleccionada es {}". format(opcion.get()))

opcion = tkinter.IntVar()

botonradio1 = tkinter.Radiobutton(raiz, text="Opción 1", variable=opcion, value=1, command = seleccionar)
botonradio1.pack()

botonradio2 = tkinter.Radiobutton(raiz, text="Opción 2", variable=opcion, value=2, command = seleccionar)
botonradio2.pack()

botonradio3 = tkinter.Radiobutton(raiz, text="Opción 3", variable=opcion, value=3, command = seleccionar)
botonradio3.pack()

raiz.mainloop()