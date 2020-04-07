# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ejemplo_Recetas(object):
    def setupUi(self, Ejemplo_Recetas):
        Ejemplo_Recetas.setObjectName("Ejemplo_Recetas")
        Ejemplo_Recetas.resize(646, 416)
        self.lbl_etiqueta_ventana = QtWidgets.QLabel(Ejemplo_Recetas)
        self.lbl_etiqueta_ventana.setGeometry(QtCore.QRect(220, 80, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_etiqueta_ventana.setFont(font)
        self.lbl_etiqueta_ventana.setObjectName("lbl_etiqueta_ventana")
        self.btn_pulsame = QtWidgets.QPushButton(Ejemplo_Recetas)
        self.btn_pulsame.setGeometry(QtCore.QRect(230, 160, 161, 61))
        self.btn_pulsame.setObjectName("btn_pulsame")

        self.retranslateUi(Ejemplo_Recetas)
        QtCore.QMetaObject.connectSlotsByName(Ejemplo_Recetas)

    def retranslateUi(self, Ejemplo_Recetas):
        _translate = QtCore.QCoreApplication.translate
        Ejemplo_Recetas.setWindowTitle(_translate("Ejemplo_Recetas", "Dialog"))
        self.lbl_etiqueta_ventana.setText(_translate("Ejemplo_Recetas", "PULSA EN EL BOTON"))
        self.btn_pulsame.setText(_translate("Ejemplo_Recetas", "PULSAME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ejemplo_Recetas = QtWidgets.QDialog()
    ui = Ui_Ejemplo_Recetas()
    ui.setupUi(Ejemplo_Recetas)
    Ejemplo_Recetas.show()
    sys.exit(app.exec_())
