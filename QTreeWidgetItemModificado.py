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

from PyQt4 import QtGui
import os

class QTreeWidgetItemModificado(QtGui.QTreeWidgetItem):
    """
    Extencion de QTreeWidgetItem(usada para crear el arbol de archivos del panelContenidos) 
    que agrega el path y el tamaño en bytes del archivo o directorio.
    En esta clase se deberian agregar las demas propiedades del archivo (como una descripcion, una imagen, etc).
    """
    def __init__ (self, itemPadre,  direccion, size):
        QtGui.QTreeWidgetItem.__init__(self,  itemPadre)
        self.direccion=direccion
        self.sizeBytes=size
    
    def getTamanioBytes(self):
        return self.sizeBytes
    
    def setTamanioBytes(self, size):
        self.sizeBytes=size
    
    def getDireccion(self):
        """
        devuelve el path completo del archivo (ej: si el archivo se llama pepe.txt, devuelve /carpeta-donde-este/pepe.txt)
        """
        return self.direccion
