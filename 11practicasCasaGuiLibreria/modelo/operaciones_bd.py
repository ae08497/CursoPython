'''
Created on 3 abr. 2020
                    Operaciones BD
@author: Goyo
'''
# el procedimiento con bd es conectar
# 1 conectar 2 operar y 3 desconectar
import mysql.connector
from modelo import constantes_sql


def conectar():
    conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "bd_libros"
        )
    return conexion

def registro_libro(libro):
    sql = constantes_sql.SQL_INSERCION_LIBRO
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (libro.titulo, libro.paginas, libro.precio)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_libros():
    #sql = constantes_sql.SQL_SELECT_LIBRO
    #conexion = conectar()
    #cursor = conectar()
    #cursor.execute(sql)
    #lista_resultado = cursor.fetchall()
    #SQL_SELECT_LIBRO = "SELECT * FROM tabala_libros"
    
    # codigo correcto
    sql = constantes_sql.SQL_SELECT_LIBRO
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado
    
    
    