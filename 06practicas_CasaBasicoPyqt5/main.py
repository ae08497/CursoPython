'''
Created on 25 mar. 2020
                            PYQT5
@author: goyo


ejemplo que carga un archivo de diseño del qtDesigner

pasos para la instalacion de pyqt5 y qt designer en windows:

instalar PyQt5:

con liclipse y cualquier aplicacion de python cerrada*

pip install PyQt5

pip install PyQt5-tools


ir a inicio y escribir exactamente -> designer 

para arrancar designer.exe


para mac:

python -m pip install PyQt5

descargar qtdesigner de https://build-system.fman.io/qt-designer-download
trar los modulos de PyQt5
# importando sys
'''




from PyQt5 import QtWidgets, uic
import sys

def funcion_boton_pulsado():
    win.label_etiqueta.setText("Gracias por pulsar el Boton")

# linea obligatoria para usar PyQt5
app = QtWidgets.QApplication([])


#win es un objeto que representa una ventana que representa lo expuesto en el archivo .ui
win = uic.loadUi("ventana.ui") #specify the location of your .ui file

win.boton_ventana.clicked.connect(funcion_boton_pulsado)
#mostramos la ventana
win.show()


#la aplicacion se sale cuando acabe la aplicacion de ventana
sys.exit(app.exec())