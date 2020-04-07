'''
Created on 1 abr. 2020

@author: nico
'''
from PyQt5.Qt import QDialog, QApplication
from ventana_principal import Ui_Ejemplo_Recetas
import sys

class Explicacion_Aplicacion(QDialog):
    def __init__(self):
        super().__init__()
        print("aqui preparo todo en el constructor")
        self.ventana = Ui_Ejemplo_Recetas()
        self.ventana.setupUi(self)
        self.ventana.btn_pulsame.clicked.connect(self.agradecer)
        self.show()
        
    def agradecer(self):
        self.ventana.lbl_etiqueta_ventana.setText("Gracias por pulsar")
        
        
        
if __name__ == "__main__":
    print("se ejecuta el main")
    
    app = QApplication(sys.argv)
    
    explicacion = Explicacion_Aplicacion()
    
    sys.exit(app.exec_())