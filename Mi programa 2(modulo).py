#Para no importar todo el modulo sino solo lo que me interesa:
#from Modulos import despedirse

despedirse("Macarena")

#Podemos renombrar a la funcion despedirse:
from Modulos import despedirse as adios

#entonces en lugar de poner despedirse("Maca") pongo:

adios("Maca")