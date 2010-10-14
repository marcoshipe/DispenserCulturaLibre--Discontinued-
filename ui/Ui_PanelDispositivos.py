# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/casa/bblug/Dispenser/ui/Forms/PanelDispositivos.ui'
#
# Created: Wed Aug 11 13:49:30 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelDonde(object):
    def setupUi(self, panelDonde):
        panelDonde.setObjectName("panelDonde")
        panelDonde.resize(804, 532)
        self.verticalLayout = QtGui.QVBoxLayout(panelDonde)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
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
        self.widget = QtGui.QWidget(panelDonde)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pendriveRadio = QtGui.QRadioButton(self.widget_2)
        self.pendriveRadio.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(16)
        self.pendriveRadio.setFont(font)
        self.pendriveRadio.setObjectName("pendriveRadio")
        self.verticalLayout_2.addWidget(self.pendriveRadio)
        self.cdRadio = QtGui.QRadioButton(self.widget_2)
        self.cdRadio.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(16)
        self.cdRadio.setFont(font)
        self.cdRadio.setObjectName("cdRadio")
        self.verticalLayout_2.addWidget(self.cdRadio)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget)
        spacerItem3 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.botonesWidget = QtGui.QWidget(panelDonde)
        self.botonesWidget.setObjectName("botonesWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.botonesWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.anteriorBoton = QtGui.QPushButton(self.botonesWidget)
        self.anteriorBoton.setObjectName("anteriorBoton")
        self.horizontalLayout_3.addWidget(self.anteriorBoton)
        spacerItem5 = QtGui.QSpacerItem(583, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.siguienteBoton = QtGui.QPushButton(self.botonesWidget)
        self.siguienteBoton.setObjectName("siguienteBoton")
        self.horizontalLayout_3.addWidget(self.siguienteBoton)
        self.verticalLayout.addWidget(self.botonesWidget)

        self.retranslateUi(panelDonde)
        QtCore.QMetaObject.connectSlotsByName(panelDonde)

    def retranslateUi(self, panelDonde):
        panelDonde.setWindowTitle(QtGui.QApplication.translate("panelDonde", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tituloLabel.setText(QtGui.QApplication.translate("panelDonde", "Seleccionar el dispositivo en el que grabar:", None, QtGui.QApplication.UnicodeUTF8))
        self.pendriveRadio.setText(QtGui.QApplication.translate("panelDonde", "insertar Pendrive", None, QtGui.QApplication.UnicodeUTF8))
        self.cdRadio.setText(QtGui.QApplication.translate("panelDonde", "Insertar Cd/Dvd", None, QtGui.QApplication.UnicodeUTF8))
        self.anteriorBoton.setText(QtGui.QApplication.translate("panelDonde", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.siguienteBoton.setText(QtGui.QApplication.translate("panelDonde", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    panelDonde = QtGui.QWidget()
    ui = Ui_panelDonde()
    ui.setupUi(panelDonde)
    panelDonde.show()
    sys.exit(app.exec_())

