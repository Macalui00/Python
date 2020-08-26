# tkinter - componente raiz: este es el componente principal de la interfaz grafica tkinter.

import tkinter

#ahora mediante el modulo tkinter llamamos al metodo TK que devuelve el elemento raiz.
raiz = tkinter.Tk() #devuelve el elemento raiz

#Con el elemento raiz, podemos darle, por ejemplo, un titulo:
raiz.title("Mi programa")

#Y por ultimo mainloop, para que este todo el rato ejecutandose.
raiz.mainloop()