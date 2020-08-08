#Fecha y Hora
#desde un modulo "nombreModulo" importar la clase "nombreClase"
from datetime import datetime

fechayhora = datetime.now() #te devuelve fecha y hora actual

print(fechayhora)

#Se puede acceder a cada uno de los elementos por separado
año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

#hora
hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print("La hora es {}:{}:{}".format(hora,minutos,segundos))