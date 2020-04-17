'''
Created on 1 abr. 2020
                        REVISTAS
@author: goyo
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_list_revistas, ventana_listado_revistas, ventana_menu_revistas, ventana_principal, ventana_registro_revistas , ventana_editar_revistas
    
from modulo.clases import Revista
from modulo import operaciones
from PyQt5.Qt import QMessageBox, QTableWidgetItem, QPushButton
import sys
from _functools import partial





lista_resultado = None

def registrar_revistas():
    revista = Revista()
    revista.titulo = ui_registrar_revistas.entrada_titulo_revista.text()
    revista.precio = ui_registrar_revistas.entrada_precio_revista.text()
    revista.distribuidora = ui_registrar_revistas.entrada_ditribuidor_revista.text()
    revista.numero_revista = ui_registrar_revistas.entrada_numero_revista.text()
    revista.date_entrega = ui_registrar_revistas.entrada_date_entrega.text()
    revista.date_devolucion = ui_registrar_revistas.entrada_date_devolucion.text()
    #revista.dascatalogado = ui_registrar_revistas.checbox_descatalogado.text()
    if ui_registrar_revistas.checbox_descatalogado.isChecked():
        revista.dascatalogado = True
    
    indice_selecionado = ui_registrar_revistas.combo_extra.currentIndex()
    revista.extra = ui_registrar_revistas.combo_extra.itemText(indice_selecionado)
    
    #revista.periodicidad = ui_registrar_revistas.radio_semanal.text()
    #revista.periodicidad = ui_registrar_revistas.radio_mensual.text()
    #revista.periodicidad = ui_registrar_revistas.radio_anual.text()
    
    if ui_registrar_revistas.radio_semanal.isChecked():
        revista.periodicidad = "semanal"

    if ui_registrar_revistas.radio_mensual.isChecked():
        revista.periodicidad = "mensual"
        
    if ui_registrar_revistas.radio_anual.isChecked():
        revista.periodicidad = "anual"

    try:
        operaciones.registro_revistas(revista)
    except Exception as e:
        print(e)

    QMessageBox.about(MainWindow,"Info","Registro de Revista OK")

def mostrar_registro_revistas():
    ui_registrar_revistas.setupUi(MainWindow)
    ui_registrar_revistas.entrada_registrar_revista.clicked.connect(registrar_revistas)    

def mostrar_listado_revistas():
    ui_listar_revistas.setupUi(MainWindow)
    lista_resultados = operaciones.obtener_revista()
    texto = ""
    for l in lista_resultados:
        texto +=("id :" + str(l[0]) + "titulo : " + l[1] 
                 + "precio : " + str(l[2]) + "distribidora : " 
                 + l[3] +  "numero de revista : " + str(l[4]) 
                 + "Fecha de entrega : " + str(l[5]) + "Fecha de devolucion :" 
                 + str(l[6]) + " Descatalogada : " + l[7] + " Extra : " + l[8] 
                 + " Periodicidad : " + l[9]+"\n") 
    ui_listar_revistas.listado_revistas.setText(texto)
    ui_ventana_list_revistas.listWidget.itemClicked(mostrar_registro)

def mostrar_registro():
    indice_selecionado = ui_ventana_list_revistas.listWidget.currentRow()
    QMessageBox.about(MainWindow,"Info","mostrar la informacion del elemento : " + str(indice_selecionado))
    
def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_revistas.setupUi(MainWindow)
    lista_resultado = operaciones.obtener_revista()
    for l in lista_resultado:
        ui_ventana_list_revistas.listWidget.addItem(" titulo : " + l[1] + " precio : " 
        + str(l[2]) + " distribidora : " + l[3] +  " numero de revista : " 
        + str(l[4]) + " Fecha de entrega : " + str(l[5]) + " Fecha de devolucion : " + str(l[6]) +
        " Descatalogada : " + l[7] + " Extra : " + l[8] + " Periodicidad : " + l[9])
    ui_ventana_list_revistas.listWidget.itemClicked.connect(mostrar_registros)
       
def mostrar_registros():
    indice_selecionado = ui_ventana_list_revistas.listWidget.currentRow()
    texto = ""
    texto += "titulo : " + lista_resultado[indice_selecionado][1]+"\n"
    texto += "precio : " + str(lista_resultado[indice_selecionado][2])+"\n"
    texto += "distribuidora : " + lista_resultado[indice_selecionado][3]+"\n"
    texto += "numero de revista : " + str(lista_resultado[indice_selecionado][4])+"\n"
    texto += "Fecha de entrega : " + str(lista_resultado[indice_selecionado][5])+"\n"
    texto += "Fecha de devolucion : " + str(lista_resultado[indice_selecionado][6])+"\n"
    texto += "Descatalogada : " + lista_resultado[indice_selecionado][7]+"\n"
    texto += "Extra : " + lista_resultado[indice_selecionado][8]+"\n"
    texto += "Periodicidad : " + lista_resultado[indice_selecionado][9]
    QMessageBox.about(MainWindow,"Info",texto)
    
def mostrar_menu_revistas():
    ui_ventana_menu_revistas.setupUi(MainWindow)
    revistas = operaciones.obtener_revista()
    fila = 0
    for l in revistas:
        ui_ventana_menu_revistas.tabla_revistas.insertRow(fila)
        columna_indice = 0
        for valor in l:
            celda = QTableWidgetItem(str(valor))
            ui_ventana_menu_revistas.tabla_revistas.setItem(fila,columna_indice,celda)
            columna_indice += 1
        boton_borrar = QPushButton("borrar")
        boton_borrar.clicked.connect(partial(borrar_revista,l[0]))
        ui_ventana_menu_revistas.tabla_revistas.setCellWidget(fila,7,boton_borrar)
        boton_editar = QPushButton("editar")
        boton_editar.clicked.connect(partial(editar_revistas,l[0],l[1]))
        ui_ventana_menu_revistas.tabla_revistas.setCellWidget(fila,8,boton_editar)
        fila +=1
        
def editar_revistas(id,titulo):
    QMessageBox.about(MainWindow,"info","vas a editar el registro con id : " + str(id) + " titulo : " + titulo)
    ui_ventana_editar_revistas.setupUi(MainWindow)
    revista_a_editar = operaciones.obtener_revista_por_id(id)
    ui_ventana_editar_revistas.entrada_titulo_revista.setText(revista_a_editar.titulo)
    ui_ventana_editar_revistas.entrada_precio_revista.setText(str(revista_a_editar.precio))
    ui_ventana_editar_revistas.entrada_ditribuidor_revista.setText(str(revista_a_editar.distribuidora))
    ui_ventana_editar_revistas.entrada_numero_revista.setText(str(revista_a_editar.numero_revista))
    ui_ventana_editar_revistas.entrada_date_entrega.setText(revista_a_editar.date_entrega)
    ui_ventana_editar_revistas.entrada_date_devolucion.setText(revista_a_editar.date_devolucion)
    ui_ventana_editar_revistas.boton_guardar_cambios_revista.clicked.connect(partial(guardar_cambios_revista,revista_a_editar.id))
    
def guardar_cambios_revista(id):
    QMessageBox.about(MainWindow,"Info","guardar cambios sobre el registro de id :" + str(id))
    revista_guardar_cambios = Revista()
    revista_guardar_cambios.titulo = ui_ventana_editar_revistas.entrada_titulo_revista.text()
    revista_guardar_cambios.precio = ui_ventana_editar_revistas.entrada_precio_revista.text()
    revista_guardar_cambios.distribuidora = ui_ventana_editar_revistas.entrada_ditribuidor_revista.text()
    revista_guardar_cambios.numero_revista = ui_ventana_editar_revistas.entrada_numero_revista.text()
    revista_guardar_cambios.date_entrega = ui_ventana_editar_revistas.entrada_date_entrega.text()
    revista_guardar_cambios.date_devolucion = ui_ventana_editar_revistas.entrada_date_devolucion.text()
    revista_guardar_cambios.id = id
    
    try:
        operaciones.guardar_cambios_revista(revista_guardar_cambios)
    except Exception as e:
        print(e)
    
    
    mostrar_menu_revistas()
    
        
def borrar_revista(id):
    QMessageBox.about(MainWindow,"Info","vas a borrar un registro " + str(id))
    operaciones.borrar_revista(id)
    mostrar_menu_revistas()
            

def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_registrar_revistas.triggered.connect(mostrar_registro_revistas)
    ui.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)
    ui.submenu_inicio.triggered.connect(mostrar_inicio)
    ui.submenu_list_widget.triggered.connect(mostrar_list_widget)
    ui.submenu_table_widget.triggered.connect(mostrar_menu_revistas)
#end de funciones
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ventana_principal.Ui_ventana_principal()
ui_registrar_revistas = ventana_registro_revistas.Ui_MainWindow()
ui_listar_revistas = ventana_listado_revistas.Ui_ventana_listado_revistas()
ui_ventana_list_revistas = ventana_list_revistas.Ui_MainWindow()
ui_ventana_menu_revistas = ventana_menu_revistas.Ui_MainWindow()
ui_ventana_editar_revistas = ventana_editar_revistas.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.submenu_registrar_revistas.triggered.connect(mostrar_registro_revistas)
ui.submenu_listar_revistas.triggered.connect(mostrar_listado_revistas)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget.triggered.connect(mostrar_menu_revistas)

MainWindow.show()
sys.exit(app.exec_())



