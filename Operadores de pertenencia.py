#Operadores de pertenencia

frutas1 = ["manzana","pera","naranja"]
frutas2 = "pera"
#Entonces, frutas1 es una variable que tiene una lista de valores
#mientras que, frutas2 es una variable que representa una cadena de texto con la palabra pera

#entonces si queremos verificar si la palabra pera esta dentro de esta lista, es muy sencillo

print(frutas2 in frutas1)

#not in es lo contrario

print(frutas2 not in frutas1) # frutas2 fuera una palabra que no esta en la lista, esto dara falso

frutas2 = "durazno"
print(frutas2 not in frutas1)