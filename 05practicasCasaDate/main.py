'''
Created on 23 mar. 2020
                        DATES
@author: goyo
'''
import time
import datetime

ahora = time.time()
print("ahora vale: " + str(ahora))

ahora = datetime.datetime.now()
print("año actual: " + str(ahora.year))

format_fecha = "%d/%m/%y" 
#preparo como quiero la fecha 
#en un string con la y da los 
#2 ultimos digitos del año
resultado = ahora.strftime(format_fecha)
print(resultado)

formato_fecha = "%d-%m-%Y %H:%M:%S"
resultado = ahora.strftime(formato_fecha)
print(resultado)

formato_fecha = "%d/%m/%Y %H:%M:%S"
resultado = ahora.strftime(formato_fecha)
print(resultado)