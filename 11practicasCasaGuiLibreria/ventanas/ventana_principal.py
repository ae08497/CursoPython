# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pantalla_inicio = QtWidgets.QLabel(self.centralwidget)
        self.pantalla_inicio.setGeometry(QtCore.QRect(260, 150, 321, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pantalla_inicio.setFont(font)
        self.pantalla_inicio.setObjectName("pantalla_inicio")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuLibros = QtWidgets.QMenu(self.menubar)
        self.menuLibros.setObjectName("menuLibros")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.submenu_listar_libros = QtWidgets.QAction(mainWindow)
        self.submenu_listar_libros.setObjectName("submenu_listar_libros")
        self.submenu_insertar_libro = QtWidgets.QAction(mainWindow)
        self.submenu_insertar_libro.setObjectName("submenu_insertar_libro")
        self.submenu_inicio = QtWidgets.QAction(mainWindow)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_list_widget_libros = QtWidgets.QAction(mainWindow)
        self.submenu_list_widget_libros.setObjectName("submenu_list_widget_libros")
        self.submenu_table_widget_libros = QtWidgets.QAction(mainWindow)
        self.submenu_table_widget_libros.setObjectName("submenu_table_widget_libros")
        self.menuLibros.addAction(self.submenu_listar_libros)
        self.menuLibros.addAction(self.submenu_insertar_libro)
        self.menuLibros.addAction(self.submenu_inicio)
        self.menuLibros.addAction(self.submenu_list_widget_libros)
        self.menuLibros.addAction(self.submenu_table_widget_libros)
        self.menubar.addAction(self.menuLibros.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.pantalla_inicio.setText(_translate("mainWindow", "Bienvenido a mi Aplicacion \n"
" de libreria"))
        self.menuLibros.setTitle(_translate("mainWindow", "Libros"))
        self.submenu_listar_libros.setText(_translate("mainWindow", "Listar Libros"))
        self.submenu_insertar_libro.setText(_translate("mainWindow", "Insertar Libros"))
        self.submenu_inicio.setText(_translate("mainWindow", "inicio"))
        self.submenu_list_widget_libros.setText(_translate("mainWindow", "listar libros usando list widget"))
        self.submenu_table_widget_libros.setText(_translate("mainWindow", "listar libros usando tabla widget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
