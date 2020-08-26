import re 

print("ingrese texto")
txt = str(input())

#x = txt.splitlines(True)
separador = "\r"
x = re.split("\r", txt)
print(re.split("\r", txt))

fichero = open("Fichero_prueba1.txt", "at")

for linea in x:
	fichero.write("\r" + linea)

fichero.close()

fichero = open("Fichero_prueba1.txt", "rt")

datos_fichero = fichero.read()

print(datos_fichero)

