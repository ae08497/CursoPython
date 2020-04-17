# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_principal(object):
    def setupUi(self, ventana_principal):
        ventana_principal.setObjectName("ventana_principal")
        ventana_principal.resize(800, 600)
        ventana_principal.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ventana_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 120, 411, 291))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        ventana_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ventana_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuRevistas = QtWidgets.QMenu(self.menubar)
        self.menuRevistas.setObjectName("menuRevistas")
        ventana_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ventana_principal)
        self.statusbar.setObjectName("statusbar")
        ventana_principal.setStatusBar(self.statusbar)
        self.submenu_inicio = QtWidgets.QAction(ventana_principal)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_registrar_revistas = QtWidgets.QAction(ventana_principal)
        self.submenu_registrar_revistas.setObjectName("submenu_registrar_revistas")
        self.submenu_listar_revistas = QtWidgets.QAction(ventana_principal)
        self.submenu_listar_revistas.setObjectName("submenu_listar_revistas")
        self.submenu_list_widget = QtWidgets.QAction(ventana_principal)
        self.submenu_list_widget.setObjectName("submenu_list_widget")
        self.submenu_table_widget = QtWidgets.QAction(ventana_principal)
        self.submenu_table_widget.setObjectName("submenu_table_widget")
        self.menuRevistas.addSeparator()
        self.menuRevistas.addAction(self.submenu_inicio)
        self.menuRevistas.addAction(self.submenu_registrar_revistas)
        self.menuRevistas.addAction(self.submenu_listar_revistas)
        self.menuRevistas.addAction(self.submenu_list_widget)
        self.menuRevistas.addAction(self.submenu_table_widget)
        self.menubar.addAction(self.menuRevistas.menuAction())

        self.retranslateUi(ventana_principal)
        QtCore.QMetaObject.connectSlotsByName(ventana_principal)

    def retranslateUi(self, ventana_principal):
        _translate = QtCore.QCoreApplication.translate
        ventana_principal.setWindowTitle(_translate("ventana_principal", "MainWindow"))
        self.label.setText(_translate("ventana_principal", "ESTA ES MI APP\n"
"PARA APLICACION \n"
"DE REVISTAS"))
        self.menuRevistas.setTitle(_translate("ventana_principal", "Revistas"))
        self.submenu_inicio.setText(_translate("ventana_principal", "Inicio"))
        self.submenu_registrar_revistas.setText(_translate("ventana_principal", "Insertar Revistas"))
        self.submenu_listar_revistas.setText(_translate("ventana_principal", "Listar Revistas"))
        self.submenu_list_widget.setText(_translate("ventana_principal", "Listado con list widget"))
        self.submenu_table_widget.setText(_translate("ventana_principal", "Listado con Table widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_principal = QtWidgets.QMainWindow()
    ui = Ui_ventana_principal()
    ui.setupUi(ventana_principal)
    ventana_principal.show()
    sys.exit(app.exec_())
