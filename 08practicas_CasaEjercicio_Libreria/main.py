'''
Created on 1 abr. 2020
                        REVISTAS
@author: goyo
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, ventana_registro_revistas, ventana_listado_revistas
    
import sys


def mostrar_registro_revista():
    ui_registrar_revistas.setupUi(MainWindow)

def mostrar_listado_revistas():
    ui_listar_revistas.setupUi(MainWindow)
        
def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_registrar_revistas.triggered.connect(mostrar_registro_revista)
    ui.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)
    ui.submenu_inicio.triggered.connect(mostrar_inicio)
#end de funciones
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_ventana_principal()
ui_registrar_revistas = ventana_registro_revistas.Ui_MainWindow()
ui_listar_revistas = ventana_listado_revistas.Ui_ventana_listado_revistas()
ui.setupUi(MainWindow)
ui.submenu_registrar_revistas.triggered.connect(mostrar_registro_revista)
ui.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
MainWindow .show()
sys.exit(app.exec_())


    #app = QtWidgets.QApplication(sys.argv)
    #ventana_principal = QtWidgets.QMainWindow()
    #ui = Ui_ventana_principal()
    #ui.setupUi(ventana_principal)
    #ventana_principal.show()
    #sys.exit(app.exec_())
