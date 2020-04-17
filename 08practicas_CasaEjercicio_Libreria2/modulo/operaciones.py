'''
Created on 3 abr. 2020
                        OPERACIONES PARA EJ REVISTAS
@author: GOYO
'''
import mysql.connector 
from modulo import constantes, clases
from mysql.connector import cursor


def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "bd_revistas"        
        )
    return conexion

def registro_revistas(revista):
    sql = constantes.SQL_INSERCION_REVISTA
    conexion = conectar()
    cursor = conexion.cursor()
    valores_a_insertar = (revista.titulo, revista.precio, revista.distribuidora, revista.numero_revista, revista.date_entrega, revista.date_devolucion, revista.descatalogado, revista.extra, revista.periodicidad)
    cursor.execute(sql, valores_a_insertar)
    conexion.commit()
    conexion.disconnect()
    
def obtener_revista():
    sql = constantes.SQL_SELECT_REVISTA
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql)
    lista_resultado = cursor.fetchall()
    conexion.disconnect()
    return lista_resultado
    
def borrar_revista(id_revista):
    sql = constantes.SQL_SELECT_BORRAR
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id_revista,)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
    
def obtener_revista_por_id(id):
    sql = constantes.SQL_OBTENER_REVISTA_POR_ID
    conexion = conectar()
    cursor = conexion.cursor()
    val = (id,)
    cursor.execute(sql,val)
    resultado = cursor.fetchone()
    print(resultado)
    conexion.disconnect()
    revista = clases.Revista()
    revista.id = resultado[0]
    revista.titulo = resultado[1]
    revista.precio = resultado[2]
    revista.distribuidora = resultado[3]
    revista.numero_revista = resultado[4]
    revista.date_entrega = resultado[5]
    revista.date_devolucion = resultado[6]
    
    return revista

def guardar_cambios_revista(revista_a_guardar_cambios):
    sql = constantes.SQL_GUARDAR_CAMBIOS_REVISTA
    conexion = conectar()
    cursor = conexion.cursor()    
    val = (revista_a_guardar_cambios.titulo, revista_a_guardar_cambios.precio, 
           revista_a_guardar_cambios.distribuidora, revista_a_guardar_cambios.numero_revista ,
           revista_a_guardar_cambios.date_entrega, revista_a_guardar_cambios.date_devolucion, revista_a_guardar_cambios.id)
    cursor.execute(sql,val)
    conexion.commit()
    conexion.disconnect()
    
    