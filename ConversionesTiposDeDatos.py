#Conversiones de tipos de datos

numero = 5
cadena = str(numero) #casteamos ese numero en un string

print(cadena)
print(type(cadena))

cadena1 = '25'
numero1 = int(cadena1) #castear la cadena en entero.

print(numero1)
print(type(numero1))

suma = numero + numero1
print(suma)

#Ahora bien, si cadena1 en vez de 25 es 25.7 no lo podemos convertir a int
#tenemos que convertirlo a float:

cadena1 = '25.7'
numero1 = float(cadena1)

print(numero1)
print(type(numero1))