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

# Form implementation generated from reading ui file '/home/casa/bblug/dispenser/Dispenser/ui/PanelIzquierdo.ui'
#
# Created: Sun Jul  4 14:47:27 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelIzquierdo(object):
    def setupUi(self, panelIzquierdo):
        panelIzquierdo.setObjectName("panelIzquierdo")
        panelIzquierdo.resize(400, 490)
        self.verticalLayout = QtGui.QVBoxLayout(panelIzquierdo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botonBienvenido = QtGui.QCommandLinkButton(panelIzquierdo)
        self.botonBienvenido.setObjectName("botonBienvenido")
        self.verticalLayout.addWidget(self.botonBienvenido)
        self.botonDonde = QtGui.QCommandLinkButton(panelIzquierdo)
        self.botonDonde.setObjectName("botonDonde")
        self.verticalLayout.addWidget(self.botonDonde)
        self.botonQue = QtGui.QCommandLinkButton(panelIzquierdo)
        self.botonQue.setObjectName("botonQue")
        self.verticalLayout.addWidget(self.botonQue)
        self.botonAhora = QtGui.QCommandLinkButton(panelIzquierdo)
        self.botonAhora.setObjectName("botonAhora")
        self.verticalLayout.addWidget(self.botonAhora)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(panelIzquierdo)
        QtCore.QMetaObject.connectSlotsByName(panelIzquierdo)

    def retranslateUi(self, panelIzquierdo):
        panelIzquierdo.setWindowTitle(QtGui.QApplication.translate("panelIzquierdo", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.botonBienvenido.setText(QtGui.QApplication.translate("panelIzquierdo", "Bienvenido", None, QtGui.QApplication.UnicodeUTF8))
        self.botonDonde.setText(QtGui.QApplication.translate("panelIzquierdo", "Donde grabamos", None, QtGui.QApplication.UnicodeUTF8))
        self.botonQue.setText(QtGui.QApplication.translate("panelIzquierdo", "Que grabamos", None, QtGui.QApplication.UnicodeUTF8))
        self.botonAhora.setText(QtGui.QApplication.translate("panelIzquierdo", "Ahora grabamos", None, QtGui.QApplication.UnicodeUTF8))

