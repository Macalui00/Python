#La funcion Lambda es una funcion pequeña y anonima, osea sin nombre

#creamos una funcion lambda que dado un numero, le sumará 30 a ese numero y nos lo devolverá como resultado.
resultado = lambda numero : numero + 30
print(resultado(10))

resultado2 = lambda numero1, numero2 : numero1 + numero2
print(resultado2(5,8))