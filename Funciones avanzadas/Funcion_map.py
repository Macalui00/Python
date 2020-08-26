#Funcion Map - aplicar una funcion a cada elemento de una lista

def multiplicar(numero):
	return numero * 2

print(multiplicar(2))

numeros = [2,4,6,8]
print("Resultado final:")
mapeo = map(multiplicar, numeros)
print("Sin castear el resultado:")
print(mapeo)
#Para poder visualizarlo correctamente lo tenemos que convertir a Lista
resultado = list(mapeo)
print("\r" +"Casteando el resultado:")
print(resultado)

print("\r" +"-----------ALTERNATIVAS---------------------------------"+ "\r")
print("Calculos en una sola linea:")
#otra manera mas sencilla y rapida de hacerlo:
lista_resultado = list(map(multiplicar,numeros))
print(lista_resultado)

#Se utiliza tambien algunas veces la funcion map con la funcion lambda ya que a veces
#no queremos definir la funcion multiplicar que hemos definido arriba, simplemente
#queremos ejecutar
print("\r" + "Con funcion lambda:")
lista_lambda = list(map(lambda numero : numero * 2, numeros))
print(lista_lambda)