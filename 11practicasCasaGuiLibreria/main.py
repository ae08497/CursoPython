'''
Created on 30 mar. 2020
                        lIBRERIA
@author: goyo
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal, ventana_listado_libros, \
ventana_registrar_libro, ventana_list_libros, ventana_tabla_widget
import sys
from modelo.clases import Libro
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem



lista_resultado = None



def registrar_libro():
    libro = Libro()
    libro.titulo = ui_registrar_libro.entrada_titulo_libro.text()
    libro.paginas = ui_registrar_libro.entrada_paginas_libro.text() 
    libro.precio = ui_registrar_libro.entrada_precio_libro.text()
    operaciones_bd.registro_libro(libro)
    QMessageBox.about(MainWindow,"Info","Registro de Libro OK")

def mostrar_registro_libro():
    ui_registrar_libro.setupUi(MainWindow)
    ui_registrar_libro.entrada_registrar_libro.clicked.connect(registrar_libro)
    
    
def mostrar_listado_libros():
    ui_listar_libros.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_libros()
    texto = ""
    for l in lista_resultado:
        texto += "id : " + str(l[0]) + " titulo : " + str(l[1]) + " paginas : " + str(l[2]) + "precio : " + str(l[3])+ "\n"
    ui_listar_libros.ventana_listado_libros.SetText(texto)
    ui_ventana_list_libros.list_widget_libros.itemClicked.connect(mostrar_registro)# que aun no exixte pero ahora se crea
    
def mostrar_registro():
    indice_selecionado = ui_ventana_list_libros.list_widget_libros.currentRow()
    QMessageBox.about(MainWindow,"Info","mostrar la informacion del elemento : " + str(indice_selecionado))
    
def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_libros.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_libros()
    #voy a rellellenar el list 
    for l in lista_resultado:
        ui_ventana_list_libros.list_widget_libros.addItem(l[1] + "paginas: " + str(l[2]))  
    ui_ventana_list_libros.list_widget_libros.itemClicked.connect(mostrar_registros)
    
def mostrar_registros():
    indice_selecionado = ui_ventana_list_libros.list_widget_libros.currentRow()
    texto = ""
    texto = "titulo : " + lista_resultado[indice_selecionado][1]+"\n"
    texto = "pagina : " + str(lista_resultado[indice_selecionado][2]) + "\n"
    texto = "precio : " + str(lista_resultado[indice_selecionado][3])
    QMessageBox.about(MainWindow,"Info", texto)
    
def mostrar_tabla_widget():
    ui_ventana_tabla_widget.setupUi(MainWindow) 
    libros = operaciones_bd.obtener_libros()
    fila = 0
    for l in libros:
        ui_ventana_tabla_widget.tabla_libros.insertRow(fila)
        celda = QTableWidgetItem(str(l[0]))
        ui_ventana_tabla_widget.tabla_libros.setItem(fila,0,celda)
        celda = QTableWidgetItem(str(l[1]))
        ui_ventana_tabla_widget.tabla_libros.setItem(fila,1,celda)
        celda = QTableWidgetItem(str(l[2]))
        ui_ventana_tabla_widget.tabla_libros.setItem(fila,2,celda)
        celda = QTableWidgetItem(str(l[3]))
        ui_ventana_tabla_widget.tabla_libros.setItem(fila,3,celda)
        fila += 1
        
def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_insertar_libro.triggered.connect(mostrar_registro_libro)
    ui.submenu_listar_libros.triggered.connect(mostrar_listado_libros)
    ui.submenu_inicio.triggered.connect(mostrar_inicio)
    ui.submenu_list_widget_libros.triggered.connect(mostrar_list_widget)
    ui.submenu_table_widget_libros.triggered.connect(mostrar_tabla_widget)
    

    
    
#fin de def de funciones    

# lineas obigatorias en PyQt5
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_mainWindow() #creo el interface definido por ventana_principal
ui_registrar_libro = ventana_registrar_libro.Ui_MainWindow() # lo mismo para listar libro
ui_listar_libros = ventana_listado_libros.Ui_MainWindow() 
ui_ventana_list_libros = ventana_list_libros.Ui_MainWindow()
ui_ventana_tabla_widget = ventana_tabla_widget.Ui_MainWindow()
ui.setupUi(MainWindow) # todo lo que tiene el interface de la ventana principal se pone en el main
ui.submenu_insertar_libro.triggered.connect(mostrar_registro_libro)
ui.submenu_listar_libros.triggered.connect(mostrar_listado_libros)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget_libros.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_libros.triggered.connect(mostrar_tabla_widget)
MainWindow.show() # creara la ventana principal de PyQt5
sys.exit(app.exec_()) # para cerrar la ventana



