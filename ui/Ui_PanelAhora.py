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

# Form implementation generated from reading ui file '/home/casa/bblug/dispenser/Dispenser/ui/PanelAhora.ui'
#
# Created: Sat Jul  3 17:16:19 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelAhora(object):
    def setupUi(self, panelAhora):
        panelAhora.setObjectName("panelAhora")
        panelAhora.resize(788, 582)
        self.verticalLayout = QtGui.QVBoxLayout(panelAhora)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.tituloLabel = QtGui.QLabel(panelAhora)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(18)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setObjectName("tituloLabel")
        self.verticalLayout.addWidget(self.tituloLabel)
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.progressBar = QtGui.QProgressBar(panelAhora)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.presentacionWidget = QtGui.QWidget(panelAhora)
        self.presentacionWidget.setObjectName("presentacionWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.presentacionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.presentacionImagenLabel = QtGui.QLabel(self.presentacionWidget)
        self.presentacionImagenLabel.setText("")
        self.presentacionImagenLabel.setPixmap(QtGui.QPixmap("../presentacion.jpg"))
        self.presentacionImagenLabel.setObjectName("presentacionImagenLabel")
        self.horizontalLayout.addWidget(self.presentacionImagenLabel)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.presentacionWidget)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(panelAhora)
        QtCore.QMetaObject.connectSlotsByName(panelAhora)

    def retranslateUi(self, panelAhora):
        panelAhora.setWindowTitle(QtGui.QApplication.translate("panelAhora", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tituloLabel.setText(QtGui.QApplication.translate("panelAhora", "Aguarde, se esta grabando lo que usted eligio", None, QtGui.QApplication.UnicodeUTF8))
