# tkinter - compónente frame

import tkinter

#Y lo primero es crear nuestro componente raiz como hjcimos la clase anterior, que es la base de todos los componentes.
raiz = tkinter.Tk()
raiz.title("Mi programa")


#Creamos el componente frame: el cual es un componente que permite incluir otros componentes dentro de él.
frame = tkinter.Frame(raiz) #y le debemos decir sobre que raiz debe crearlo, en este caso sobre la raiz de nuestro componente grafico.
#Este componente frame devuelve un elemento tipo frame

#y el componente lo podemos configurar mediante el metodo "config" y le podemos dar una configuracion por ejemplo, que el fondo sea azul
frame.config(bg = "blue", width = 400, height = 300)
#bg background, podemos darle tamaño tambien: ancho y alto.

#Y mediante el pack, lo mostramos por pantalla. Es decir, importamos el modulo, creamos la raiz sobre el que se apoyan los demas 
#componentes, no olvidarse poner el mainloop y creamos el componente frame
frame.pack()

#Cuando le damos a build, nos aparece la ventana y vamos a ver que si agrandamos la pantalla del programa, el framre es un cuadrado azul
#y dentro del frame pueden haber otros componentes

raiz.mainloop()
