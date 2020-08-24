#Ficheros formato excel
"""Veremos como abrir un fichero excel desde python y crear un dataframe para poder trabajar con los datos que tiene ese fichero de Excel."""
"""IMPORTANTE:
    - Primer error que me salto: yo coloque la siguiente ruta: C:\Users\qx822xl\Documents\GitHub\mundialFutbol.xlsx, me salto lo siguiente:
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
    Investigando la solucion era lo siguiente:
    Necesita duplicar todas las barras invertidas:
    "C:\\Users\\qx822xl\\Documents\\GitHub\\mundialFutbol.xlsx"
    O prefija la cadena con r(para producir una cadena sin procesar):
    r"C:\Users\qx822xl\Documents\GitHub\mundialFutbol.xlsx"
    (esto fue sacado de: https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file)
    - Me pidio que instalara un modulo: ImportError: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.
    """
import pandas as pd 

#El excel puede tener varias hojas y podemos seleccionar que hoja queremos
fichero_excel = pd.ExcelFile("C:\\Users\\qx822xl\\Documents\\GitHub\\mundialFutbol.xlsx")
dataframe = fichero_excel.parse("Sheet1") #Yo quiero la hoja 1 y lo almacenamos en un dataframe

print(dataframe)

#Ha leido correctamente los datos del excel y los colocó correctamente en el dataframe.