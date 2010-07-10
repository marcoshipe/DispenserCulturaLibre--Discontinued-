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

# Form implementation generated from reading ui file '/home/casa/bblug/dispenser/Dispenser/ui/PanelQue'
#
# Created: Sat Jul  3 17:16:22 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelQue(object):
    def setupUi(self, panelQue):
        panelQue.setObjectName("panelQue")
        panelQue.resize(764, 562)
        self.verticalLayout = QtGui.QVBoxLayout(panelQue)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tituloLabel = QtGui.QLabel(panelQue)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(18)
        self.tituloLabel.setFont(font)
        self.tituloLabel.setObjectName("tituloLabel")
        self.verticalLayout.addWidget(self.tituloLabel)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.seleccionWidget = QtGui.QWidget(panelQue)
        self.seleccionWidget.setObjectName("seleccionWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.seleccionWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.treeWidget = QtGui.QTreeWidget(self.seleccionWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.treeWidget)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.seleccionWidget)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.progressBarWidget = QtGui.QWidget(panelQue)
        self.progressBarWidget.setObjectName("progressBarWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.progressBarWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtGui.QProgressBar(self.progressBarWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.progressBarWidget)
        self.botonesWidget = QtGui.QWidget(panelQue)
        self.botonesWidget.setObjectName("botonesWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.botonesWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.anteriorBoton = QtGui.QPushButton(self.botonesWidget)
        self.anteriorBoton.setObjectName("anteriorBoton")
        self.horizontalLayout_2.addWidget(self.anteriorBoton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.siguienteBoton = QtGui.QPushButton(self.botonesWidget)
        self.siguienteBoton.setObjectName("siguienteBoton")
        self.horizontalLayout_2.addWidget(self.siguienteBoton)
        self.verticalLayout.addWidget(self.botonesWidget)

        self.retranslateUi(panelQue)
        QtCore.QMetaObject.connectSlotsByName(panelQue)

    def retranslateUi(self, panelQue):
        panelQue.setWindowTitle(QtGui.QApplication.translate("panelQue", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tituloLabel.setText(QtGui.QApplication.translate("panelQue", "Seleccione los archivos que quiere grabar:", None, QtGui.QApplication.UnicodeUTF8))
        self.anteriorBoton.setText(QtGui.QApplication.translate("panelQue", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.siguienteBoton.setText(QtGui.QApplication.translate("panelQue", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))

