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

# Form implementation generated from reading ui file '/home/casa/bblug/dispenser/Dispenser/ui/PanelBienvenido.ui'
#
# Created: Sun Jul  4 14:47:28 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelBienvenido(object):
    def setupUi(self, panelBienvenido):
        panelBienvenido.setObjectName("panelBienvenido")
        panelBienvenido.resize(739, 534)
        self.verticalLayout = QtGui.QVBoxLayout(panelBienvenido)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelBienvenido = QtGui.QLabel(panelBienvenido)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        self.labelBienvenido.setFont(font)
        self.labelBienvenido.setObjectName("labelBienvenido")
        self.verticalLayout.addWidget(self.labelBienvenido)
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.widgetDescripcion = QtGui.QWidget(panelBienvenido)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetDescripcion.sizePolicy().hasHeightForWidth())
        self.widgetDescripcion.setSizePolicy(sizePolicy)
        self.widgetDescripcion.setObjectName("widgetDescripcion")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetDescripcion)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.plainTextEditDescripcion = QtGui.QPlainTextEdit(self.widgetDescripcion)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(217, 212, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 212, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.plainTextEditDescripcion.setPalette(palette)
        self.plainTextEditDescripcion.setFrameShape(QtGui.QFrame.NoFrame)
        self.plainTextEditDescripcion.setReadOnly(True)
        self.plainTextEditDescripcion.setObjectName("plainTextEditDescripcion")
        self.horizontalLayout_2.addWidget(self.plainTextEditDescripcion)
        self.verticalLayout.addWidget(self.widgetDescripcion)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem2)
        self.widgetSiguiente = QtGui.QWidget(panelBienvenido)
        self.widgetSiguiente.setObjectName("widgetSiguiente")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetSiguiente)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.botonSiguiente = QtGui.QPushButton(self.widgetSiguiente)
        self.botonSiguiente.setObjectName("botonSiguiente")
        self.horizontalLayout.addWidget(self.botonSiguiente)
        self.verticalLayout.addWidget(self.widgetSiguiente)

        self.retranslateUi(panelBienvenido)
        QtCore.QMetaObject.connectSlotsByName(panelBienvenido)

    def retranslateUi(self, panelBienvenido):
        panelBienvenido.setWindowTitle(QtGui.QApplication.translate("panelBienvenido", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBienvenido.setText(QtGui.QApplication.translate("panelBienvenido", "Bienvenido", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEditDescripcion.setPlainText(QtGui.QApplication.translate("panelBienvenido", "Aca va una descripcion\n"
"Aca va una descripcion\n"
"Aca va una descripcion\n"
"Aca va una descripcion\n"
"Aca va una descripcion\n"
"Aca va una descripcion\n"
"\n"
"Aca va una descripcion\n"
"Aca va una descripcion\n"
"Aca va una descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.botonSiguiente.setText(QtGui.QApplication.translate("panelBienvenido", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))

