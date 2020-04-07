'''
Created on 3 abr. 2020
                        CONSTANTES SQL
@author: goyo
'''
SQL_INSERCION_LIBRO = "INSERT INTO `tabala_libros` (`id`, `titulo`, `paginas`, `precio`) VALUES (NULL, %s, %s, %s);"
SQL_SELECT_LIBRO = "SELECT * FROM `tabala_libros`"