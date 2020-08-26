'''Crear un modulo modulo1.py
Añadir la clase "coche" creada en un ejercicio anterior al modulo1
añadir la funcion lambda media creada en otro ejercicio al modulo1

Crear un programa programa1.py
Importar el modulo1.py
Crear un objeto coche1 al instanciar la clase coche
Mediante print mostrar las caracteristicas del coche
calcular la media de 3 notas y mostrar el resultado con un print

Ejecutar el programa programa1.py y ver el resultado
'''
import Modulo1

coche1 = Modulo1.Auto("Peugeot","Rojo","Gasoil",4.3)
coche1.mostrar_caracteristicas()

resultadofinal = Modulo1.resultado(5,6,7)
print(resultadofinal)