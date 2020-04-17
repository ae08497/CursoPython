# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_menu_revistas.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 441, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabla_revistas = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_revistas.setGeometry(QtCore.QRect(-5, 110, 941, 441))
        self.tabla_revistas.setObjectName("tabla_revistas")
        self.tabla_revistas.setColumnCount(9)
        self.tabla_revistas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_revistas.setHorizontalHeaderItem(8, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Listado con Tablewidge de revistas"))
        item = self.tabla_revistas.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tabla_revistas.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "titulo"))
        item = self.tabla_revistas.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "precio"))
        item = self.tabla_revistas.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "distribidora"))
        item = self.tabla_revistas.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "numero de revista"))
        item = self.tabla_revistas.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fecha de entrega"))
        item = self.tabla_revistas.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Fecha de devolucion"))
        item = self.tabla_revistas.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "borrar"))
        item = self.tabla_revistas.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "editar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
