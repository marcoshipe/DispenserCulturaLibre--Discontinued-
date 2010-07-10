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

# Form implementation generated from reading ui file '/home/casa/bblug/dispenser/Dispenser/ui/PanelDonde.ui'
#
# Created: Sun Jul  4 14:50:58 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelDonde(object):
    def setupUi(self, panelDonde):
        panelDonde.setObjectName("panelDonde")
        panelDonde.resize(804, 532)
        self.verticalLayout = QtGui.QVBoxLayout(panelDonde)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.tituloLabel = QtGui.QLabel(panelDonde)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(18)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setObjectName("tituloLabel")
        self.verticalLayout.addWidget(self.tituloLabel)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.pendriveWidget = QtGui.QWidget(panelDonde)
        self.pendriveWidget.setObjectName("pendriveWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.pendriveWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pendriveBoton = QtGui.QPushButton(self.pendriveWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pendriveBoton.sizePolicy().hasHeightForWidth())
        self.pendriveBoton.setSizePolicy(sizePolicy)
        self.pendriveBoton.setObjectName("pendriveBoton")
        self.horizontalLayout.addWidget(self.pendriveBoton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.pendriveWidget)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)
        self.cdDvdWidget = QtGui.QWidget(panelDonde)
        self.cdDvdWidget.setObjectName("cdDvdWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.cdDvdWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.cdDvdBoton = QtGui.QPushButton(self.cdDvdWidget)
        self.cdDvdBoton.setObjectName("cdDvdBoton")
        self.horizontalLayout_2.addWidget(self.cdDvdBoton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.cdDvdWidget)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.botonesWidget = QtGui.QWidget(panelDonde)
        self.botonesWidget.setObjectName("botonesWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.botonesWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.anteriorBoton = QtGui.QPushButton(self.botonesWidget)
        self.anteriorBoton.setObjectName("anteriorBoton")
        self.horizontalLayout_3.addWidget(self.anteriorBoton)
        spacerItem8 = QtGui.QSpacerItem(583, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.siguienteBoton = QtGui.QPushButton(self.botonesWidget)
        self.siguienteBoton.setObjectName("siguienteBoton")
        self.horizontalLayout_3.addWidget(self.siguienteBoton)
        self.verticalLayout.addWidget(self.botonesWidget)

        self.retranslateUi(panelDonde)
        QtCore.QMetaObject.connectSlotsByName(panelDonde)

    def retranslateUi(self, panelDonde):
        panelDonde.setWindowTitle(QtGui.QApplication.translate("panelDonde", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tituloLabel.setText(QtGui.QApplication.translate("panelDonde", "Seleccionar el dispositivo en el que grabar:", None, QtGui.QApplication.UnicodeUTF8))
        self.pendriveBoton.setText(QtGui.QApplication.translate("panelDonde", "Pendrive", None, QtGui.QApplication.UnicodeUTF8))
        self.cdDvdBoton.setText(QtGui.QApplication.translate("panelDonde", "Cd/Dvd", None, QtGui.QApplication.UnicodeUTF8))
        self.anteriorBoton.setText(QtGui.QApplication.translate("panelDonde", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.siguienteBoton.setText(QtGui.QApplication.translate("panelDonde", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))
