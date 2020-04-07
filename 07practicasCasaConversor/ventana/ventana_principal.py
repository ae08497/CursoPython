# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
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
        self.entrada_pesos = QtWidgets.QLabel(self.centralwidget)
        self.entrada_pesos.setGeometry(QtCore.QRect(50, 110, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.entrada_pesos.setFont(font)
        self.entrada_pesos.setObjectName("entrada_pesos")
        self.introduce_pesos = QtWidgets.QLineEdit(self.centralwidget)
        self.introduce_pesos.setGeometry(QtCore.QRect(372, 130, 201, 51))
        self.introduce_pesos.setObjectName("introduce_pesos")
        self.boton_convertira_euros = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertira_euros.setGeometry(QtCore.QRect(340, 222, 161, 91))
        self.boton_convertira_euros.setObjectName("boton_convertira_euros")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(240, 370, 311, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.entrada_pesos.setText(_translate("MainWindow", "introduce una cantidad en Pesos"))
        self.boton_convertira_euros.setText(_translate("MainWindow", "CONVERTIR A EUROS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
