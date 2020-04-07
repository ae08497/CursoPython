'''
Created on 1 abr. 2020
                    LIBRERIA 1
@author: goyo
'''
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "bd_libros"
)
print("conexion Ok")

sql = "INSERT INTO `tabala_libros` (`id`, `titulo`, `paginas`, `precio`) VALUES (NULL, 'BlaBlaBla', '100', '2.20');"

cursor = mydb.cursor()
cursor.execute(sql)

mydb.commit()

print("registro Ok")

