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
import threading, time
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QColor
from ui.Ui_VentanaPrincipal import Ui_MainWindow
from ui.Ui_PanelIzquierdo import Ui_panelIzquierdo
from ui.Ui_PanelBienvenido import Ui_panelBienvenido
from ui.Ui_PanelDispositivos import Ui_panelDonde
from ui.Ui_PanelContenidos import Ui_panelQue
from ui.Ui_PanelGrabacion import Ui_panelAhora
from ui.Ui_PanelVerificacion import Ui_panelVerificacion
from ui.Ui_error import Ui_Dialog
from aux import Aux
from QTreeWidgetItemModificado import QTreeWidgetItemModificado
from grabacion.usb import Usb
from grabacion.cdrom import CdRom
from grabacion.dispositivo import Dispositivo

class MainWindow(QMainWindow):
    """
    CLASE PRINCIPAL, POSIBLEMENTE DEBE DESGLOBARSE EN DISTINTAS CLASES (REVEER ESTO)
    """

    ####################################################################################################################################################################
    #VARIABLES DE INSTANCIA Y PEQUEÑA DESCRIPCION:                                                                                                                     #
    #self.directorioContenidoLibre: path del directorio donde se encuentra el contenido libre                                                                          #
    #self.directorioProy: path del directorio raiz del proyecto                                                                                                        #
    #self.dispositivoSeleccionado: representa al dispositivo (usb, cd, dvd o etc) seleccionado con todas sus caracteristicas. Es de tipo Dispositivo                   #
    #self.manejadorDispositivo: es de tipo base ManejadorDispositivo y tiene metodos para saber que dispositivos hay (de su tipo) y para grabar en un dipositivo       #
    #self.timerDispositivo: es el encargado de cada X tiempo llamar a un metodo para actualizar los dispositivos disponibles                                           #
    #self.timerPresentacion: es el encargado de cada X tiempo llamar a un metodo para actualizar la imagen que se muestra en la presentacion en el panel de grabacion  #
    #self.timerBarraDeProgreso: es el encargado de cada X tiempo llamar a un metodo para actuailzar la barra de progreso que muestra el porcentaje grabado             #
    #self.presentacion: es una lista de QPixmap con todas las imagenes para la presentacion a mostrar en el panel de grabacion                                         #
    #self.presentacionImagenActual: es un entero entre 0 y len(self.presentacion)-1, que guarda la imagen que se esta mostrando actualmente en la presentacion         #
    #self.app: variable necesaria para refrescar las animaciones en el panel de grabacion (en el metodo mostrarPanelGrabacion)                                         #
    #                                                                                                                                                                  #
    #A continuacion nombro los paneles, los cuales tienen, todos, tanto una clase como un widget.                                                                      #
    #El widget es el panel en si, la clase es donde se encuentran todos los componentes del panel (ver los metodos de configuracion de panel)                          #
    #self.panelIzquierdo: donde se muestra en que panel se esta                                                                                                        #
    #self.panelIzquierdoWidget                                                                                                                                         #
    #(no pongo mas los widget, pero estan de todos y tienen sintaxis semejante)                                                                                        #
    #self.panelBienvenido: muestra una pantall de bienvenida con una descripcion de que hace el programa, etc.                                                         #
    #self.panelDispositivos: muestra opciones para seleccionar el dispositivo en el que grabar el contenido (pendrive, cd/dvd, etc)                                    #
    #self.panelContenidos: muestra todo el contenido para poder seleccionar el que se quiere grabar (musica, peliculas, software, etc)                                 #
    #self.panelVerificacion: muestra el dispositivo y los datos seleccionados, y botones para volver atras y cambiarlos o para grabar                                  #
    #self.panelGrabacion: panel donde se graba el contenido elegido en el dispositivo seleccionado mientras su progreso y una presentacion con informacion variada     #
    #self.paletaPanelActivo: representa la paleta (colores) para el "boton" o "label" del panel izquierdo cuando el panel al que representa es el que se muestra       #
    #self.paletaPanelNoActivo: representa la paleta (colores) para el "boton" o "label" del panel izquierdo cuando el panel al que representa no es el que se muestra  #
    #self.paletaLabel: representa la paleta (colores) para los labels dentro de los frames en el panel izquierdo. Se utiliza para que su letra sea negra y no marron   #
    ####################################################################################################################################################################

    def __init__(self, app,  parent = None):
        QMainWindow.__init__(self, parent)

	#Se necesita para refrescar los paneles en el metodo mostrarPanelGrabacion        
	self.app=app

        #Variables para el directorio donde se guarda todo el contenido libre y para el directorio del proyecto
        self.directorioContenidoLibre=os.getcwd()+'/Contenido-Libre'
        self.directorioProy=os.getcwd()

        #Inicializacion de la Ventana principal, que es donde se colocan los demas paneles 
        #(sobre esta solo van los paneles y una linea que separa el panel izquierdo de los demas)
        self.UiVentanaPrincipal=Ui_MainWindow()
        self.UiVentanaPrincipal.setupUi(self)

        #Inicializo y configuro todos los paneles:
        self.configurarPanelIzquierdo()

        #Creo una linea para separar el panelIzquierdo de los demas
        self.line = QtGui.QFrame()
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.line)

        self.configurarPanelBienvenido()
        self.configurarPanelDispositivos()
        self.configurarPanelContenidos()
        self.configurarPanelVerificacion()
        self.configurarPanelGrabacion()        

        #Dejo solo el panel de bienvenida en la parte derecha de la pantalla (ocultando los demas salvo el Izquierdo)
        self.mostrarPanelBienvenido()

        #Conecto los botones con sus funciones respectivas (slots)
        QtCore.QMetaObject.connectSlotsByName(self)


    #Metodo usado por configurarPanelContenidos 
    #Dado el path de un directorio y un nodo QTreeWidgetItem (de un arbol) crea los nodos de todos sus archivos y subdirectorios recursivamente
    def recorrerDirectorioCreandoQTreeWidgetItems(self,  dirDirectorio,  itemDirectorio):
        size=0
        for nombreArchivo in os.listdir(dirDirectorio):
            itemArchivo=self.crearQTreeWidgetItemModificado(itemDirectorio,  dirDirectorio+'/'+nombreArchivo)
            if  os.path.isdir(dirDirectorio+'/'+nombreArchivo):
                self.recorrerDirectorioCreandoQTreeWidgetItems(dirDirectorio+'/'+nombreArchivo, itemArchivo)
            size=size+itemArchivo.getTamanioBytes()
        if os.path.isdir(dirDirectorio):
            itemDirectorio.setTamanioBytes(size)
            sizeUnidad=Aux.convertirTamanio(itemDirectorio.getTamanioBytes())
            itemDirectorio.setText(0, os.path.basename(dirDirectorio)+' ('+str(sizeUnidad[0])+' '+sizeUnidad[1]+')')

    #Metodo usado po configurarPanelContenidos y recorrerDirectorioCreandoQTreeWidgetItems
    #Dado un QTreeWidgetItemModificado (o un QTreeWidget en el caso de los elementos del arbol que no tienen padre) y el path del archivo/directorio
    #crea un QTreeWidgetItemModificado (que extiende a QTreeWidgetItem agregando el path y el tamaño en bytes del archivo o directorio (ver QTreeWidgetItemModificado))
    def crearQTreeWidgetItemModificado(self,  itemPadre,  direccion):
        size=os.path.getsize(direccion)
        item = QTreeWidgetItemModificado(itemPadre,  direccion, size)
        item.setCheckState(0, QtCore.Qt.Unchecked)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        #le pongo como nombre del item: "nombre del archivo" ("tamaño" "unidad") ej: Fito (150 MiB)
        sizeUnidad=Aux.convertirTamanio(item.getTamanioBytes())
        item.setText(0, QtGui.QApplication.translate("MainWindow", os.path.basename(direccion)+' ('+str(sizeUnidad[0])+' '+sizeUnidad[1]+')', None, QtGui.QApplication.UnicodeUTF8))
        return item

    #actualiza los dispositivos y los botones con la informacion adecuada
    def actualizarDispositivos(self):
        #creo variables para cada dispositivo asi los actualizo
        usb=Usb()
        cd=CdRom()
        usbDev = usb.hayDispositivos()
        if usbDev: #si hay algun usb
            path=usbDev.getPath()
            nombreUsb=path[path.rfind("/")+1:]
            self.panelDispositivos.pendriveRadio.setText("Pendrive insertado: "+nombreUsb+"\nespacio libre: "+(str(Aux.convertirTamanio(usbDev.getLibre()))))
            self.panelDispositivos.pendriveRadio.setEnabled(True)
        else:
            self.panelDispositivos.pendriveRadio.setText("Insertar Pendrive")
            self.panelDispositivos.pendriveRadio.setEnabled(False)
        cdDev=cd.hayDispositivos()
        if cdDev: #si hay algun cd/dvd
            path=cdDev.getPath()
            nombreCd=path
            self.panelDispositivos.cdRadio.setText(cdDev.getTipo()+" insertado: "+nombreCd+"\nespacio libre: "+(str(Aux.convertirTamanio(cdDev.getLibre()))))
            self.panelDispositivos.cdRadio.setEnabled(True)
        else:
            self.panelDispositivos.cdRadio.setText("Insertar Cd/Dvd")
            self.panelDispositivos.cdRadio.setEnabled(False)

    #Este metodo se usa para devolver todas las direcciones de los archivos y directorios seleccionados para grabar 
    #(el path es relativo, ya que se le saca el self.directorioContenidoLibre)
    #por ejemplo: musica/tema.mp3 (cuando el path completo seria algo asi: /home/.../Dispenser/contenido-libre/musica/tema.mp3)
    def archivosYDirectoriosSeleccionados(self):
        items=self.panelContenidos.treeWidget.findItems('', QtCore.Qt.MatchRecursive|QtCore.Qt.MatchContains) #items guarda todos los items del arbol
        lista=[] 
        for item in items: #itero sobre todos los items del arbol
          if (item.checkState(0)==2 or item.checkState(0)==1): #si el item esta marcado
                lista.append(item.getDireccion().lstrip(self.directorioContenidoLibre))#por cada item agrego su direccion a la lista
        return lista

    #Este metodo se usa para devolver todas las direcciones de los archivos seleccionados para grabar 
    #(el path es relativo, ya que se le saca el self.directorioContenidoLibre)
    #por ejemplo: musica/tema.mp3 (cuando el path completo seria algo asi: /home/.../Dispenser/contenido-libre/musica/tema.mp3)
    def archivosSeleccionados(self):
        items=self.panelContenidos.treeWidget.findItems('', QtCore.Qt.MatchRecursive|QtCore.Qt.MatchContains) #items guarda todos los items del arbol
        lista=[] 
        for item in items: #itero sobre todos los items del arbol
          if item.checkState(0)==2 and item.childCount()==0: #si el item esta marcado y es archivo (o sea que tiene 0 hijos)
                lista.append("/"+item.getDireccion().lstrip(self.directorioProy))#por cada item agrego su direccion a la lista
        return lista

    def comprobarYMostrarDatos(self):
        if self.dispositivoSeleccionado:
            nombreDispositivo=self.dispositivoSeleccionado.getPath()[self.dispositivoSeleccionado.getPath().rfind("/")+1:]
            self.panelVerificacion.dispositivoTextEdit.setPlainText("Dispositivo: "+nombreDispositivo+"\nespacio libre: "+(str(self.dispositivoSeleccionado.getLibre())))
        else:
            self.panelVerificacion.dispositivoTextEdit.setPlainText("DISPOSITIVO NO SELECCIONADO\nIMPOSIBLE GRABAR\nVOLVER PARA ATRAS Y SELECCIONAR UN DISPOSITIVO")
        datos=""
        for archivo in self.archivosYDirectoriosSeleccionados():
            #le dejo solo el nombre del archivo o directorio y lo voy tabulando, asi queda mas entendible
            aux=archivo.count("/")
            archivo=archivo[archivo.rfind("/")+1:]
            while aux>0:
                archivo="     "+archivo
                aux=aux-1
            datos=datos+archivo+"\n"
        self.panelVerificacion.datosTextEdit.setPlainText(datos)

    def clickBotonPendrive(self):
        #selecciono como dispositivo al usb y como manejador al manejador de usb
        usb=Usb()
        self.dispositivoSeleccionado=usb.hayDispositivos()
        self.manejadorDispositivo=usb

    def clickBotonCd(self):
        cd=CdRom()
        self.dispositivoSeleccionado=cd.hayDispositivos()
        self.manejadorDispositivo=cd

    def grabar(self):
        self.manejadorDispositivo.grabar(self.directorioProy,  self.archivosSeleccionados(),  self.dispositivoSeleccionado)

    def modificarBarraProgreso(self, item, colum):
        #los parametros son para que enganche con la señal
        i=0
        for item in self.panelContenidos.treeWidget.findItems('', QtCore.Qt.MatchRecursive|QtCore.Qt.MatchContains) : #itero sobre todos los items del arbol
          if item.checkState(0)==2 and item.childCount()==0: #si el item esta marcado y es archivo (o sea que tiene 0 hijos)
                i=i+item.getTamanioBytes()
        if self.dispositivoSeleccionado:
            if (i>self.dispositivoSeleccionado.getLibre()):
                #ACA DEVERIA CAMBIARSE EL TEXT DE LA PROGRESS BAR A LLENO
                self.panelContenidos.progressBar.setValue(self.dispositivoSeleccionado.getLibre())
            else:
                self.panelContenidos.progressBar.setValue(i)
        else:
            self.panelContenidos.progressBar.setValue(100)

    def actualizarPresentacion(self):
        self.presentacionImagenActual=(self.presentacionImagenActual+1)%len(self.presentacion)
        self.panelGrabacion.imagenLabel.setPixmap(self.presentacion[self.presentacionImagenActual])
    
    def actualizarBarraDeProgreso(self):
        self.app.processEvents()
        #ESTO NO TIENE QUE IR, ES SOLO PARA MOSTRAR QUE LA BARRA FUNCIONA
        self.textoBarraActual=(self.textoBarraActual+1)%len(self.textoBarra)
        self.panelGrabacion.progressBar.setFormat(self.textoBarra[self.textoBarraActual])
        self.panelGrabacion.progressBar.setValue(self.panelGrabacion.progressBar.value()+5)

    ##############################################################################################################
    #Metodos que son llamados por los botones de los paneles (los que necesitan algo mas que mostrar los paneles)#
    ##############################################################################################################
    def panelDispositivosBotonAnterior(self):
        self.timerDispositivos.stop()
        self.mostrarPanelBienvenido()

    def panelDispositivosBotonSiguiente(self):
        self.timerDispositivos.stop()
        self.mostrarPanelContenidos()

    def panelVerificacionBotonGrabar(self):
        if (self.dispositivoSeleccionado):
            self.mostrarPanelGrabacion()
        else:
            self.dialogErrorWidget.exec_()

    #############################################################################################################
    #Metodos encargados de inicializar y configurar los paneles. Son llamados desde el constructor de la clase  #
    #############################################################################################################
    def configurarPanelIzquierdo(self):
        self.panelIzquierdoWidget = QtGui.QWidget()
        self.panelIzquierdo = Ui_panelIzquierdo()
        self.panelIzquierdo.setupUi(self.panelIzquierdoWidget)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelIzquierdoWidget)
        #Creo 2 variables para cambiar los frames del panel izquierdo segun el panel actual que se muestra.
        self.paletaPanelNoActivo=QPalette(self.panelIzquierdo.bienvenidoFrame.palette())
        self.paletaPanelActivo=QPalette(self.paletaPanelNoActivo)
        #le cambio los colores al borde y al fondo (WindowText y Window respectivamente)de la paletaPanelActivo
        self.paletaPanelActivo.setColor(0, 0, QColor(148, 134, 125))
        self.paletaPanelActivo.setColor(0, 10, QColor(188, 183, 176))
        #pongo las letras de los labels en negro, asi dejan de heredar del frame y no toman el color "marron" cuando se activa un panel
        self.paletaLabel=QPalette(self.panelIzquierdo.bienvenidoLabel.palette())
        self.paletaLabel.setColor(0, 0, QColor(50, 50, 50))
        self.panelIzquierdo.bienvenidoLabel.setPalette(self.paletaLabel)
        self.panelIzquierdo.dispositivosLabel.setPalette(self.paletaLabel)
        self.panelIzquierdo.contenidosLabel.setPalette(self.paletaLabel)
        self.panelIzquierdo.verificacionLabel.setPalette(self.paletaLabel)
        self.panelIzquierdo.grabacionLabel.setPalette(self.paletaLabel)
    
    def configurarPanelBienvenido(self):
        self.panelBienvenidoWidget = QtGui.QWidget()
        self.panelBienvenido = Ui_panelBienvenido()
        self.panelBienvenido.setupUi(self.panelBienvenidoWidget)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelBienvenidoWidget)
        #Configuro los botones
        QtCore.QObject.connect(self.panelBienvenido.botonSiguiente, QtCore.SIGNAL("pressed()"), self.mostrarPanelDispositivos)

    def configurarPanelDispositivos(self):
        self.panelDispositivosWidget = QtGui.QWidget()
        self.panelDispositivos = Ui_panelDonde()
        self.panelDispositivos.setupUi(self.panelDispositivosWidget)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelDispositivosWidget)
        #Configuro los botones
        QtCore.QObject.connect(self.panelDispositivos.anteriorBoton, QtCore.SIGNAL("pressed()"), self.panelDispositivosBotonAnterior)
        QtCore.QObject.connect(self.panelDispositivos.siguienteBoton, QtCore.SIGNAL("pressed()"), self.panelDispositivosBotonSiguiente)
        QtCore.QObject.connect(self.panelDispositivos.pendriveRadio,  QtCore.SIGNAL("clicked()"), self.clickBotonPendrive)
        QtCore.QObject.connect(self.panelDispositivos.cdRadio,  QtCore.SIGNAL("clicked()"), self.clickBotonCd)
        #creo variable self.dispositivoSeleccionado (lo hago asi para poder comprovar si tiene valor o no 
        #en el metodo panelVerificacionBotonGrabar() y otros y se inicializa en los metodos clickBotonPendrive(), clickBoton...())
        self.dispositivoSeleccionado=None
        self.manejadorDispositivo=None
        #inicializo un timer para actualizar los dispositivos conectados y conecto su timeout con un metodo
        self.timerDispositivos = QTimer()
        QtCore.QObject.connect(self.timerDispositivos, QtCore.SIGNAL("timeout()"), self.actualizarDispositivos)

    def configurarPanelContenidos(self):
        self.panelContenidosWidget = QtGui.QWidget()
        self.panelContenidos = Ui_panelQue()
        self.panelContenidos.setupUi(self.panelContenidosWidget)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelContenidosWidget)
        #Configuro los botones
        QtCore.QObject.connect(self.panelContenidos.anteriorBoton, QtCore.SIGNAL("pressed()"), self.mostrarPanelDispositivos)
        QtCore.QObject.connect(self.panelContenidos.siguienteBoton, QtCore.SIGNAL("pressed()"), self.mostrarPanelVerificacion)
        QtCore.QObject.connect(self.panelContenidos.treeWidget, QtCore.SIGNAL("itemChanged(QTreeWidgetItem*,int)"), self.modificarBarraProgreso)
        #Lleno el objeto QTreeWidget (que es, en el panelContenidos, donde se ven los contenidos que se pueden grabar) con todo el contenido
        for nombreArchivo in os.listdir(self.directorioContenidoLibre):
            itemArchivo=self.crearQTreeWidgetItemModificado(self.panelContenidos.treeWidget,  self.directorioContenidoLibre+'/'+nombreArchivo)
            if (os.path.isdir(self.directorioContenidoLibre)):
                self.recorrerDirectorioCreandoQTreeWidgetItems(self.directorioContenidoLibre+'/'+nombreArchivo,  itemArchivo)

    def configurarPanelVerificacion(self):
        self.panelVerificacionWidget=QtGui.QWidget()
        self.panelVerificacion=Ui_panelVerificacion()
        self.panelVerificacion.setupUi(self.panelVerificacionWidget)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelVerificacionWidget)
        #configuro los botones
        QtCore.QObject.connect(self.panelVerificacion.volverBoton, QtCore.SIGNAL("pressed()"), self.mostrarPanelContenidos)
        QtCore.QObject.connect(self.panelVerificacion.grabarBoton, QtCore.SIGNAL("pressed()"), self.panelVerificacionBotonGrabar)
        #Inicializo un panel de dialogo de error, para cuando no se haya seleccionado un dispositivo o se haya desconectado
        self.dialogErrorWidget=QtGui.QDialog()
        self.dialogError=Ui_Dialog()
        self.dialogError.setupUi(self.dialogErrorWidget)

    def configurarPanelGrabacion(self):
        self.panelGrabacionWidget = QtGui.QWidget()
        self.panelGrabacion = Ui_panelAhora()
        self.panelGrabacion.setupUi(self.panelGrabacionWidget)
        self.UiVentanaPrincipal.horizontalLayout.addWidget(self.panelGrabacionWidget)
        #Configuro los botones
        QtCore.QObject.connect(self.panelGrabacion.principioBoton, QtCore.SIGNAL("pressed()"), self.mostrarPanelBienvenido)
        #Para mostrar la presentacion con info del dispenser y para la barra de progreso que se va actualizando uso un QTimer
        #inicializo el timer y conecto su timeout con un metodo
        self.timerPresentacion = QTimer()
        QtCore.QObject.connect(self.timerPresentacion, QtCore.SIGNAL("timeout()"), self.actualizarPresentacion)
        #almaceno todas las imagenes de la presentacion en una lista de QPixmax self.presentacion, 
        #y una variable para la imagen actual de la presentacion self.presentacionImagenActual
        presentacionArchivos=os.listdir(os.getcwd()+"/images-and-icons/")
        self.presentacion=[]
        for presentacionArchActual in presentacionArchivos:
            self.presentacion.append(QPixmap(os.getcwd()+"/images-and-icons/"+presentacionArchActual))
        self.presentacionImagenActual=0
        self.timerBarraDeProgreso = QTimer()
        QtCore.QObject.connect(self.timerBarraDeProgreso, QtCore.SIGNAL("timeout()"), self.actualizarBarraDeProgreso)
        #ESTO NO TIENE QUE IR, ES SOLO PARA MOSTRAR QUE LA BARRA FUNCIONA
        self.textoBarra=["grabando.", "grabando..", "grabando..."]
        self.textoBarraActual=0       

    ##############################################################################################################################
    #Metodos para mostrar y ocultar paneles (son los que usan los botones "siguiente" y "anterior" de los botones de los paneles #
    #Los botones del panel izquierdo no tienen funcionalidad, solo sirven para mostrar por que paso van                          #
    #estos metodos tambien pueden hacer alguna que otra funcion como cambiar alguna variable para que se pause o inicie un hilo  #
    ##############################################################################################################################
    def mostrarPanelBienvenido(self):
        self.panelBienvenidoWidget.show()
        self.panelDispositivosWidget.hide()
        self.panelContenidosWidget.hide()
        self.panelVerificacionWidget.hide()
        self.panelGrabacionWidget.hide()
        self.panelIzquierdo.bienvenidoFrame.setPalette(self.paletaPanelActivo)
        self.panelIzquierdo.dispositivosFrame.setPalette(self.paletaPanelNoActivo)
        self.panelIzquierdo.grabacionFrame.setPalette(self.paletaPanelNoActivo)

    def mostrarPanelDispositivos(self):
        self.panelBienvenidoWidget.hide()
        self.panelDispositivosWidget.show()
        self.panelContenidosWidget.hide()
        self.panelIzquierdo.bienvenidoFrame.setPalette(self.paletaPanelNoActivo)
        self.panelIzquierdo.dispositivosFrame.setPalette(self.paletaPanelActivo)
        self.panelIzquierdo.contenidosFrame.setPalette(self.paletaPanelNoActivo)
        #Empiezo a ejecutar el timer para actualizar los dispositivos cada 1 segundo
        #Llamo al metodo que va a llamar el timer al principio, para que no se tenga que esperar el tiempo inicial sin que se actualice
        self.actualizarDispositivos()
        self.timerDispositivos.start(1000)

    def mostrarPanelContenidos(self):
        self.panelDispositivosWidget.hide()
        self.panelContenidosWidget.show()
        self.panelVerificacionWidget.hide()
        self.panelIzquierdo.dispositivosFrame.setPalette(self.paletaPanelNoActivo)
        self.panelIzquierdo.contenidosFrame.setPalette(self.paletaPanelActivo)
        self.panelIzquierdo.verificacionFrame.setPalette(self.paletaPanelNoActivo)
        if self.dispositivoSeleccionado:
            self.panelContenidos.progressBar.setRange(0, self.dispositivoSeleccionado.getLibre())

    def mostrarPanelVerificacion(self):
        self.panelContenidosWidget.hide()
        self.panelVerificacionWidget.show()
        self.panelIzquierdo.contenidosFrame.setPalette(self.paletaPanelNoActivo)
        self.panelIzquierdo.verificacionFrame.setPalette(self.paletaPanelActivo)
        #muestro informacion sobre el dispositivo seleccionado y los datos a grabar
        self.comprobarYMostrarDatos()

    def mostrarPanelGrabacion(self):
        self.panelVerificacionWidget.hide()
        self.panelGrabacionWidget.show()
        self.panelIzquierdo.verificacionFrame.setPalette(self.paletaPanelNoActivo)
        self.panelIzquierdo.grabacionFrame.setPalette(self.paletaPanelActivo)
        #oculto la seccion donde muestra que ya se termino de grabar
        self.panelGrabacion.terminadoWidget.hide()
        #Llamo al metodo que va a llamar el timer al principio, para que no se tenga que esperar el tiempo inicial sin que se actualice
        self.actualizarPresentacion()
        self.timerPresentacion.start(7000)
        self.actualizarBarraDeProgreso()
        self.timerBarraDeProgreso.start(2000)
        #Inicio el hilo de grabacion y empiezo a grabar
        self.hiloGrabacion = threading.Thread(target=self.grabar)
        self.hiloGrabacion.start()
        #Actualizo el panel cada segundo para que se actualice la presentacion y la barra de progreso mientras que se este grabando
        while self.hiloGrabacion.isAlive():
            self.app.processEvents()
            time.sleep(1)
        self.timerPresentacion.stop()
        self.timerBarraDeProgreso.stop()
        #muestro el panel que indica que la grabacion termino con botones para volver al principio y oculto la barra de grabacion y su label
        self.panelGrabacion.terminadoWidget.show()
        self.panelGrabacion.label.hide()
        self.panelGrabacion.progressBar.hide()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow(app)
    myapp.showFullScreen()
    sys.exit(app.exec_())
