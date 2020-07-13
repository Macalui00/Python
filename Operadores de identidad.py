#operadores de identidad: intenta identificar si dos objetos son realmente el mismo objeto si son distintos objetos.

frutas1 = ["manzana","pera"]
frutas2 = ["manzana","pera"]
frutas3 = frutas1 #a frutas3 le asigne frutas1, al hacer esta asignacion, pasa a ser exactamente el mismo objeto pero con dos nombres diferentes.
#es decir, si cambiamos en frutas3, le añadimos un elemento mas a la lista (ver más abajo), ahora frutas3 tiene 3 elementos.
#entonces frutas1 tiene tambien tres elementos.

print(frutas3 is frutas1) #frutas3 es el mismo objeto que frutas1? True

frutas3.append("naranja")
print(f"Frutas 1: {frutas1} y frutas 3: {frutas3}")

#en cambio el isnot es el caso contrario al is.
print(frutas3 is not frutas1)