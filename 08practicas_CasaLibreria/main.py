'''
Created on 30 mar. 2020
                        lIBRERIA
@author: nico
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, ventana_listado_libros, ventana_registrar_libro 
import sys



def mostrar_registro_libro():
    ui_registrar_libro.setupUi(MainWindow)

def mostrar_listado_libros():
    ui_listar_libro.setupUi(MainWindow)
    
def mostrar_inicio():
    ui.setupUi(MainWindow)
    
#fin de def de funciones    

# lineas obigatorias en PyQt5
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_mainWindow() #creo el interface definido por ventana_principal
ui_registrar_libro = ventana_registrar_libro.Ui_MainWindow() # lo mismo para listar libro
ui_listar_libro = ventana_listado_libros.Ui_MainWindow() 
ui.setupUi(MainWindow) # todo lo que tiene el interface de la ventana principal se pone en el main
ui.submenu_insertar_libro.triggered.connect(mostrar_registro_libro)
ui.submenu_listar_libros.triggered.connect(mostrar_listado_libros)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
MainWindow.show() # creara la ventana principal de PyQt5
sys.exit(app.exec_()) # para cerrar la ventana


