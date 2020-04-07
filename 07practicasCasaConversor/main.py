'''
Created on 27 mar. 2020
                    Conversor
@author: goyo
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventana import ventana_principal

#crear una nueva aplicacion que permita la conversion de euros  a un 
# tipo de moneda a elegir
#agregar 2 botones mas para 2 tipos mas de monedas
#agregar un icono a cada boton para el tipo de monedas, buscando en uinternet

def boton_convertira_euros():
    print("boton pulsado")
    introducido = ui.introduce_pesos.text().replace(",",".")
    introducido_float = float(introducido)
    euros = introducido_float * 0.014
    ui.label_resultado.setText("en Euros : " + "{:.2f}".format(euros))

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

#antes de mostrar ventana principal asigno el codigo a ejecutar cuando
#se haga click el boton

ui.boton_convertira_euros.clicked.connect(boton_convertira_euros)
MainWindow.show()

sys.exit(app.exec_())