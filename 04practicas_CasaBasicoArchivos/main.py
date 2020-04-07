'''
Created on 23 mar. 2020
                    ARCCHIVOS BASICO
@author: goyo
'''
f = open("datos.txt","w")
# -> w ->write # abrir el archivo para crarlo y escribir en el
# -> r ->read # abrir el archivo leer de el
# -> x ->#para solo crear el archivo
# -> a ->

f.write("Primera linea de informacion")
f.write("\nSegunda Linea")
f.close()
print("escritura correcta")



f = open("datos.txt","r")
#print("primera linea : ")
#print(f.readline())
print("lectura de todas las lineas del archivo")
for linea in f:
    print(linea,end="") #pongo el end para evitar el salto de linea extra
f.close