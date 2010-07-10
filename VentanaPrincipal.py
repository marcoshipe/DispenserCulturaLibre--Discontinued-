# -*- coding: utf-8 -*-

#Copyright (C) 2010 Hipedinger Marcos <marcoshipe@gmail.com>
#
#This file is part of the program "Dispenser de Cultura Libre".
#
#Dispenser de Cultura Libre is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 2 of the License, or
#(at your option) any later version.
#
#Dispenser de Cultura Libre is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Dispenser de Cultura Libre.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
from ui.Ui_VentanaPrincipal import Ui_MainWindow
from ui.Ui_PanelIzquierdo import Ui_panelIzquierdo
from ui.Ui_PanelBienvenido import Ui_panelBienvenido
from ui.Ui_PanelDonde import Ui_panelDonde
from ui.Ui_PanelQue import Ui_panelQue
from ui.Ui_PanelAhora import Ui_panelAhora
from QTreeWidgetItemModificado import QTreeWidgetItemModificado

class MainWindow(QMainWindow):
    """
    CLASE PRINCIPAL, POSIBLEMENTE DEBE DESGLOBARSE EN DISTINTAS CLASES (REVEER ESTO)
    """
    
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        
        #creo y configuro la ventana principal y los paneles dentro de esta.
        self.UiVentanaPrincipal=Ui_MainWindow()
        self.UiVentanaPrincipal.setupUi(self)
        self.panelIzquierdo = QtGui.QWidget()
        self.UiPanelIzquierdo = Ui_panelIzquierdo()
        self.UiPanelIzquierdo.setupUi(self.panelIzquierdo)
        self.panelBienvenido = QtGui.QWidget()
        self.UiPanelBienvenido = Ui_panelBienvenido()
        self.UiPanelBienvenido.setupUi(self.panelBienvenido)
        self.panelDonde = QtGui.QWidget()
        self.UiPanelDonde = Ui_panelDonde()
        self.UiPanelDonde.setupUi(self.panelDonde)
        self.panelQue = QtGui.QWidget()
        self.UiPanelQue = Ui_panelQue()
        self.UiPanelQue.setupUi(self.panelQue)
        self.panelAhora = QtGui.QWidget()
        self.UiPanelAhora = Ui_panelAhora()
        self.UiPanelAhora.setupUi(self.panelAhora)
        
        #creo una linea para separar el panelIzquierdo de los demas
        self.line = QtGui.QFrame()
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        
        #agrego los paneles y la linea divisoria a la ventana principal
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelIzquierdo)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.line)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelBienvenido)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelDonde)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelQue)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelAhora)
        
        #oculto los paneles Donde, Que y Ahora, dejando solamente el Izquierdo (que se va a ver siempre) 
        #y el Bienvenido, que despues va a ser reemplazado por los otros (Donde, Que y Ahora)
        self.panelDonde.setVisible(0)
        self.panelQue.setVisible(0)
        self.panelAhora.setVisible(0)
        
        #configuro los botones "anterior" y "siguiente" para que cambien los paneles como deben
        QtCore.QObject.connect(self.UiPanelBienvenido.botonSiguiente, QtCore.SIGNAL("pressed()"), self.panelDonde.show)
        QtCore.QObject.connect(self.UiPanelBienvenido.botonSiguiente, QtCore.SIGNAL("pressed()"), self.panelBienvenido.hide)
        QtCore.QObject.connect(self.UiPanelDonde.anteriorBoton, QtCore.SIGNAL("pressed()"), self.panelBienvenido.show)
        QtCore.QObject.connect(self.UiPanelDonde.anteriorBoton, QtCore.SIGNAL("pressed()"), self.panelDonde.hide)
        QtCore.QObject.connect(self.UiPanelDonde.siguienteBoton, QtCore.SIGNAL("pressed()"), self.panelQue.show)
        QtCore.QObject.connect(self.UiPanelDonde.siguienteBoton, QtCore.SIGNAL("pressed()"), self.panelDonde.hide)
        QtCore.QObject.connect(self.UiPanelQue.anteriorBoton, QtCore.SIGNAL("pressed()"), self.panelDonde.show)
        QtCore.QObject.connect(self.UiPanelQue.anteriorBoton, QtCore.SIGNAL("pressed()"), self.panelQue.hide)
        QtCore.QObject.connect(self.UiPanelQue.siguienteBoton, QtCore.SIGNAL("pressed()"), self.panelAhora.show)
        QtCore.QObject.connect(self.UiPanelQue.siguienteBoton, QtCore.SIGNAL("pressed()"), self.panelQue.hide)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        #creamos los items del arbol QTreeWidget del panel panelQue
        dirRoot=os.getcwd()+'/Root' #ACA SE DEBE ESPECIFICAR BIEN EL DIRECTORIO DEFINITIVO, EL ACTUAL ES SOLO DE PRUEBA
        for nombreArchivo in os.listdir(dirRoot):
            itemArchivo=self.crearItem(self.UiPanelQue.treeWidget,  dirRoot+'/'+nombreArchivo)
            if (os.path.isdir(dirRoot)):
                self.recorrerDirectorio(dirRoot+'/'+nombreArchivo,  itemArchivo)

    #Metodo Auxiliar para crear los items del arbol. 
    #Recorre el directorio dado, junto con su QTreeWidgetItem y crea los items de todos sus archivos y subdirectorios
    def recorrerDirectorio(self,  dirDirectorio,  itemDirectorio):
        for nombreArchivo in os.listdir(dirDirectorio):
            itemArchivo=self.crearItem(itemDirectorio,  dirDirectorio+'/'+nombreArchivo)
            if  os.path.isdir(dirDirectorio+'/'+nombreArchivo):
                self.recorrerDirectorio(dirDirectorio+'/'+nombreArchivo, itemArchivo)

    #Metodo Auxiliar para crear los items del arbol.
    #crea un QTreeWidgetItemModificado (que extiende a QTreeWidgetItem)
    #con un QTreeWidgetItemModificado (o el QTreeWidget en el caso de los elementos del arbol que no tienen padre) y direccion pasados como parametro
    def crearItem(self,  itemPadre,  direccion):
        size=os.path.getsize(direccion)
        item = QTreeWidgetItemModificado(itemPadre,  direccion, size)
        item.setCheckState(0, QtCore.Qt.Unchecked)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        #le pongo como nombre del item: "nombre del archivo" ("tamaño" "unidad") ej: Fito (150 MiB)
        item.setText(0, QtGui.QApplication.translate("MainWindow", os.path.basename(direccion)+' ('+str(item.getTamanioUnidad()[0])+' '+item.getTamanioUnidad()[1]+')', None, QtGui.QApplication.UnicodeUTF8))
        return item
    
    #Este metodo se usa para devolver todas las direcciones de los archivos para grabar
    #Solo fue una prueba, para saber si andaba (y anda ;D)
    def metodoDevuelveRutasParaGrabar(self):
        items=self.treeWidget.findItems('', QtCore.Qt.MatchRecursive|QtCore.Qt.MatchContains) #items guarda todos los items del arbol
        self.textEdit.setText('') #aca se deberia crear un string o lo que sea (lo del textEdit fue una prueba, no existe tal textEdit actualmente)
        for item in items: #itero sobre todos los items del arbol
          if item.checkState(0)==2: #si el item esta marcado
                self.textEdit.setText(self.textEdit.toPlainText()+'\n'+item.getDireccion()) #lo agrego al string (lo del textEdit fue una prueba)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.showFullScreen()
    sys.exit(app.exec_())
