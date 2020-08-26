# tkinter - Componente label/etiqueta: sirve para poner etiquetas de texto dentro de nuestro componente gráfico

""" """

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

#Creamos el componente label(etiqueta)
""" Primero creamos una variables de tipo texto, que va a ser el texto que va a mostrar nuestra etiqueta
"""
texto = "¡Hola mundo!"
""" .label tiene dos parametros, el primero, el componente sobre el que se va a crear, nuestro elemento raiz,
y segundo el texto que va a mostrar la etiqueta, que en este caso es la variable texto"""
etiqueta = tkinter.Label(raiz, text=texto) #esto devuelve un label, una etiqueta label que llamaremos etiqueta

"""Esta etiqueta se puede configurar con el config """
etiqueta.config(fg = "green", bg = "lightgrey", font=("Cortana",30))
#fg color de las letras, bg background color.

#por ultimo, mostramos la etiqueta con pack
etiqueta.pack()

raiz.mainloop()