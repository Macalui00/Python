# tkinter - Componente checkbutton (boton de verificación)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el checkbutton
"""Texto que mostrara = opcion 1
   Variable donde se almacenará su valor
   En caso de que este activo valdra 1
   En caso de que este desactivado valdra 0
   Cuando lo pulsamos queremos ejecutar una acción que le vamos a llamar verificar"""
def verificar():
	valor = check1.get()
	if (valor == 1):
		print("El check está activado")
	else:
		print("El check está desactivado")

check1 = tkinter.IntVar()

boton1= tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
boton1.pack()

raiz.mainloop()