# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_registrar_libro.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 30, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 170, 47, 13))
        self.label_2.setObjectName("label_2")
        self.entrada_titulo_libro = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_titulo_libro.setGeometry(QtCore.QRect(280, 170, 113, 20))
        self.entrada_titulo_libro.setObjectName("entrada_titulo_libro")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 230, 47, 13))
        self.label_3.setObjectName("label_3")
        self.entrada_paginas_libro = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_paginas_libro.setGeometry(QtCore.QRect(280, 230, 113, 20))
        self.entrada_paginas_libro.setObjectName("entrada_paginas_libro")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 290, 47, 13))
        self.label_4.setObjectName("label_4")
        self.entrada_precio_libro = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_precio_libro.setGeometry(QtCore.QRect(280, 290, 113, 20))
        self.entrada_precio_libro.setObjectName("entrada_precio_libro")
        self.entrada_registrar_libro = QtWidgets.QPushButton(self.centralwidget)
        self.entrada_registrar_libro.setGeometry(QtCore.QRect(234, 342, 291, 71))
        self.entrada_registrar_libro.setObjectName("entrada_registrar_libro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Introduce los Datos del Libro"))
        self.label_2.setText(_translate("MainWindow", "Titulo:"))
        self.label_3.setText(_translate("MainWindow", "Paginas:"))
        self.label_4.setText(_translate("MainWindow", "Precio:"))
        self.entrada_registrar_libro.setText(_translate("MainWindow", "Registrar Libro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
