# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setStyleSheet("color: rgb(38, 19, 255);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"selection-color: rgb(16, 28, 255);\n"
"border-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 6, 51);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"font: 8pt \"Ravie\";\n"
"font: 20pt \"MS PMincho\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.introduce_cantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.introduce_cantidad.setGeometry(QtCore.QRect(430, 220, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.introduce_cantidad.setFont(font)
        self.introduce_cantidad.setObjectName("introduce_cantidad")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 231, 71))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 350, 231, 71))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 470, 231, 71))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.coversor_euros = QtWidgets.QLabel(self.centralwidget)
        self.coversor_euros.setGeometry(QtCore.QRect(190, 10, 391, 81))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.coversor_euros.setFont(font)
        self.coversor_euros.setObjectName("coversor_euros")
        self.boton_dolares_euros = QtWidgets.QPushButton(self.centralwidget)
        self.boton_dolares_euros.setGeometry(QtCore.QRect(300, 130, 75, 71))
        self.boton_dolares_euros.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.boton_dolares_euros.setObjectName("boton_dolares_euros")
        self.boton_libras_euros = QtWidgets.QPushButton(self.centralwidget)
        self.boton_libras_euros.setGeometry(QtCore.QRect(300, 250, 75, 71))
        self.boton_libras_euros.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.boton_libras_euros.setObjectName("boton_libras_euros")
        self.boton_yenes_euros = QtWidgets.QPushButton(self.centralwidget)
        self.boton_yenes_euros.setGeometry(QtCore.QRect(300, 370, 75, 71))
        self.boton_yenes_euros.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.boton_yenes_euros.setObjectName("boton_yenes_euros")
        self.boton_pesetas_euros = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pesetas_euros.setGeometry(QtCore.QRect(300, 470, 75, 71))
        self.boton_pesetas_euros.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.boton_pesetas_euros.setObjectName("boton_pesetas_euros")
        self.label_resultados = QtWidgets.QLineEdit(self.centralwidget)
        self.label_resultados.setGeometry(QtCore.QRect(430, 390, 211, 111))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_resultados.setFont(font)
        self.label_resultados.setText("")
        self.label_resultados.setObjectName("label_resultados")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 130, 251, 71))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 330, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 140, 191, 71))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>DOLARES</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Libras a Euros"))
        self.label_3.setText(_translate("MainWindow", "Yenes a Euros"))
        self.label_4.setText(_translate("MainWindow", "Pesetas a Euros"))
        self.coversor_euros.setText(_translate("MainWindow", "Conversor de monedas \n"
"        a euros"))
        self.boton_dolares_euros.setText(_translate("MainWindow", "Push"))
        self.boton_libras_euros.setText(_translate("MainWindow", "Push"))
        self.boton_yenes_euros.setText(_translate("MainWindow", "Push"))
        self.boton_pesetas_euros.setText(_translate("MainWindow", "Push"))
        self.label.setText(_translate("MainWindow", "Introduce Cantidad"))
        self.label_5.setText(_translate("MainWindow", "Euros"))
        self.label_6.setText(_translate("MainWindow", "Dolares a Euros"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
