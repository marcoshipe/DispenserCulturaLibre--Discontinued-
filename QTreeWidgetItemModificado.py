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
    Extencion de QTreeWidgetItem(usada para crear el arbol de archivos del panelQue) 
    que agrega la direccion y el tamaño (con la unidad: ej GiB, MiB, etc) del archivo o directorio.
    En esta clase se deberian agregar las demas propiedades del archivo (como una descripcion, una imagen, etc).
    """
    def __init__ (self, itemPadre,  direccion, size):
        QtGui.QTreeWidgetItem.__init__(self,  itemPadre)
        self.direccion=direccion
        (self.size, self.unidad)=self.convertirTamanio(os.path.getsize(direccion))
    
    def convertirTamanio(self,  bytes):
        """
        Metodo que convierte un tamaño dado en bytes al que parece mas comodo: bytes, KiB, MiB o GiB
        """
        size=bytes
        if size>1073741824:
            size/=1073741824
            unidad='GiB'
        else:
            if size>1048576:
                size/=1048576
                unidad="MiB"
            else:
                if size>1024:
                    size/=1024
                    unidad="KiB"
                else:
                    unidad="bytes"
        return (size, unidad)
    
    def getTamanioUnidad(self):
        """
        devuelve una tupla con el tamaño del archivo y su unidad
        """
        return (self.size, self.unidad)
    
    def getDireccion(self):
        """
        devuelve la direccion del archivo (ej: si el archivo se llama pepe.txt, devuelve /carpeta-donde-este/pepe.txt)
        """
        return self.direccion
