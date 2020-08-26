 #PIP es un gestor de paquetes y modulos para python
#un modulo es una libreria de codigo python que podes incluir en tu proyecto.

#import nombredelmodulo si este modulo no existe en nuestro ordenador, tenemos que ir a la terminal,
#y desde ahi tenemos que instalarlo: pip --version nos dice si tenemos instalado el gestor de modulos y la version en la que esta.
#podemos ver los paquetes que hay instalados: pip list, llama a gestor de modulos y que nos diga todos los modulos que estan, nos dice el nombre y version

#Ejemplo, queremos importar el siguiente modulo: import camelcase y nos dice que no lo tenemos instalado, entonces vamos a cmd y ponemos:
#pip install nombredelmodulo, en este caso pip install camelcase

#una vez que ya esta instalado lo podemos usar.

import camelcase
camel = camelcase.CamelCase()
texto = "el nombre es mariana"
print(camel.hump(texto)) #El resultado es el siguiente: El Nombre Es Mariana

#si no lo queremos usar mas lo podemos desinstalar: pip unistall nombredelpaquete

