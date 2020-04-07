'''
Created on 31 mar. 2020
                        EJERCICIO CONVERSOR
@author: Goyo
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import conversor


def boton_dolares_euros():
        print("boton pulsado")
        introducido = ui.introduce_cantidad.text().replace(",",".")
        introducido_float = float(introducido)
        euros = introducido_float / 1.11
        ui.label_resultados.setText("en Euros : " + "{:.2f}".format(euros))
def boton_libras_euros():
        print("boton pulsado")
        introducido = ui.introduce_cantidad.text().replace(",",".")
        introducido_float = float(introducido)
        euros = introducido_float * 1.1248 
        ui.label_resultados.setText("en Euros : " + "{:.2f}".format(euros))
def boton_yenes_euros():
        print("boton pulsado")
        introducido = ui.introduce_cantidad.text().replace(",",".")
        introducido_float = float(introducido)
        euros = introducido_float * 0.0084
        ui.label_resultados.setText("en Euros : " + "{:.2f}".format(euros))
def boton_pesetas_euros():        
        print("boton pulsado")
        introducido = ui.introduce_cantidad.text().replace(",",".")
        introducido_float = float(introducido)
        euros = introducido_float /166.386
        ui.label_resultados.setText("en Euros : " + "{:.2f}".format(euros))
   

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = conversor.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.boton_dolares_euros.clicked.connect(boton_dolares_euros)
ui.boton_libras_euros.clicked.connect(boton_libras_euros)
ui.boton_yenes_euros.clicked.connect(boton_yenes_euros)
ui.boton_pesetas_euros.clicked.connect(boton_pesetas_euros)
MainWindow.show()
sys.exit(app.exec_())