#Operadores lógicos

num1 = 10
num2 = 5
num3 = 7
num4 = 8

#10 > 5?
print(num1 > num2) #True

# 7 < 8?
print(num3 < num4) #True

#Cada una de las condiciones va entre parentesis.
print((num1 > num2) and (num3 < num4)) #Para que sea cierto tiene que ser verdadero la parte izquiera y la parte derecha

#7 > 8 ?
print(num3 > num4) #False

#Primera cond da True, la segunda da False
print((num1 > num2) and (num3 > num4)) #Da False

#operador or, que se de alguna de las dos condiciones, ya con que una sea verdadera, el resultado sera verdadero.
print((num1 > num2) and (num3 > num4)) # Da True

#operador not
print(not(num3 > num4)) #not(false) = true

