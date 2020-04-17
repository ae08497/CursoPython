'''
Created on 3 abr. 2020
                        CONSTANTES PARA EJ REVISTAS
@author: GOYO
'''

SQL_INSERCION_REVISTA = "INSERT INTO `tabla_revistas` (`id`, `titulo`, `precio`, `distribuidora`, `numero de revista`, `fecha de entrega`, `fecha de devolucion`, dascatalogado , extra, periodicidad) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
SQL_SELECT_REVISTA = "SELECT * FROM tabla_revistas "
SQL_SELECT_BORRAR = "DELETE FROM tabla_revistas WHERE id = %s ;"
SQL_OBTENER_REVISTA_POR_ID = "SELECT * FROM tabla_revistas WHERE id = %s;"
SQL_GUARDAR_CAMBIOS_REVISTA = "UPDATE tabla_revistas set titulo = %s, precio = %s, distribuidora = %s, `numero de revista` = %s, `fecha de entrega` = %s, `fecha de devolucion` = %s WHERE id = %s ;"