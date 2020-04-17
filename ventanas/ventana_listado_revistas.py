# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listado_revistas.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventana_listado_revistas(object):
    def setupUi(self, ventana_listado_revistas):
        ventana_listado_revistas.setObjectName("ventana_listado_revistas")
        ventana_listado_revistas.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ventana_listado_revistas)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 80, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(150, 180, 491, 351))
        self.textEdit.setStyleSheet("background-color: rgb(243, 255, 160);")
        self.textEdit.setObjectName("textEdit")
        ventana_listado_revistas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ventana_listado_revistas)
        self.statusbar.setObjectName("statusbar")
        ventana_listado_revistas.setStatusBar(self.statusbar)

        self.retranslateUi(ventana_listado_revistas)
        QtCore.QMetaObject.connectSlotsByName(ventana_listado_revistas)

    def retranslateUi(self, ventana_listado_revistas):
        _translate = QtCore.QCoreApplication.translate
        ventana_listado_revistas.setWindowTitle(_translate("ventana_listado_revistas", "MainWindow"))
        self.label.setText(_translate("ventana_listado_revistas", "   LISTADO DE REVISTAS"))
        self.textEdit.setHtml(_translate("ventana_listado_revistas", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_listado_revistas = QtWidgets.QMainWindow()
    ui = Ui_ventana_listado_revistas()
    ui.setupUi(ventana_listado_revistas)
    ventana_listado_revistas.show()
    sys.exit(app.exec_())
