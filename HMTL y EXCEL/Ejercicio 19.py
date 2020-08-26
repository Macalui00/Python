#Ejercicio

"""Leer un fichero adjunto "poblacion.xlsx" y cargar los datos en un dataframe. Con estos datos, visualizar cual es la poblacion mas poblada de américa.
Leer el fichero adjunto "poblacion.csv" y cargar los daros en un dataframe y hacer lo mismo"""
import pandas as pd
import os.path


def ingresoArch():
    print("Ingrese la ruta del archivo")
    archivo = str(input ())
    existeArch = os.path.isfile(archivo) 
    if (existeArch):
        return archivo
    else:
        ingresoArch()

def obtenerPoblacion(dataframe,continente):
    indice = -1
    for indice_fila, fila in dataframe.iterrows():
        if dataframe.iloc[indice_fila]["Continente"] == continente:
            print(indice_fila)
            print(fila)
            break
        if (indice != -1):
            print("Continente no encontrado")
    # if (indice != -1):
    #     print("El país más poblado de américa")
    #     print(dataframe.iloc[indice]["País más poblado"])
    #     print("Ciudad más poblada de américa")
    #     print(dataframe.iloc[indice]["Ciudad más poblada"])
    # else:
    #     print("Continente no encontrado")


def corroborarResp(resp):
    while (resp != 'S') and (resp != 'N'):
        print("Respuesta incorrecta. Ingrese S/N")
        resp = str(input())
    return resp

def mostrarHojaCompleta(dataframe):
    print("Desea ver todos los continentes? S/N")
    resp = str(input())
    resp = corroborarResp(resp)
    if (resp == "S"):
        print(dataframe)

def mostrarContinentes(dataframe):
    print("Desea ver un continente? S/N")
    resp = str(input())
    resp = corroborarResp(resp)
    if (resp == "S"):
        while (resp == "S"):
            print("Ingrese nombre del continente que le interese")
            continente = str(input())
            obtenerPoblacion(dataframe, continente)
            print("Desea ver otro continente? S/N")
            resp = str(input())
            resp = corroborarResp(resp)

def obtenerHoja(fichero_excel):
    print("Ingrese nombre de hoja")
    hoja = str(input())
    dataframe = fichero_excel.parse(hoja)
    return dataframe
   

archivo = ingresoArch()
fichero_excel = pd.ExcelFile(archivo)
print("Desea seleccionar hojas? S/N")
resp = str(input())
resp = corroborarResp(resp)
if (resp == "S"):
    while(resp == "S"):
        dataframe = obtenerHoja(fichero_excel)
        mostrarHojaCompleta(dataframe)
        mostrarContinentes(dataframe)
        print("Desea seleccionar hojas? S/N")
        resp = str(input())


        
