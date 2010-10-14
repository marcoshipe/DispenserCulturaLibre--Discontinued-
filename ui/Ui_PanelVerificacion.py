# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/casa/bblug/Dispenser/ui/Forms/PanelVerificacion.ui'
#
# Created: Wed Aug 11 12:12:18 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelVerificacion(object):
    def setupUi(self, panelVerificacion):
        panelVerificacion.setObjectName("panelVerificacion")
        panelVerificacion.resize(787, 635)
        self.verticalLayout = QtGui.QVBoxLayout(panelVerificacion)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(panelVerificacion)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(panelVerificacion)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dispositivoTextEdit = QtGui.QPlainTextEdit(panelVerificacion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispositivoTextEdit.sizePolicy().hasHeightForWidth())
        self.dispositivoTextEdit.setSizePolicy(sizePolicy)
        self.dispositivoTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.dispositivoTextEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.dispositivoTextEdit.setReadOnly(True)
        self.dispositivoTextEdit.setObjectName("dispositivoTextEdit")
        self.verticalLayout.addWidget(self.dispositivoTextEdit)
        self.label_3 = QtGui.QLabel(panelVerificacion)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.datosTextEdit = QtGui.QPlainTextEdit(panelVerificacion)
        self.datosTextEdit.setReadOnly(True)
        self.datosTextEdit.setObjectName("datosTextEdit")
        self.verticalLayout.addWidget(self.datosTextEdit)
        self.label_4 = QtGui.QLabel(panelVerificacion)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.widget = QtGui.QWidget(panelVerificacion)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.volverBoton = QtGui.QPushButton(self.widget)
        self.volverBoton.setObjectName("volverBoton")
        self.horizontalLayout.addWidget(self.volverBoton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.grabarBoton = QtGui.QPushButton(self.widget)
        self.grabarBoton.setObjectName("grabarBoton")
        self.horizontalLayout.addWidget(self.grabarBoton)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(panelVerificacion)
        QtCore.QMetaObject.connectSlotsByName(panelVerificacion)

    def retranslateUi(self, panelVerificacion):
        panelVerificacion.setWindowTitle(QtGui.QApplication.translate("panelVerificacion", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("panelVerificacion", "Si los datos siguientes son correctos, presione el boton Grabar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("panelVerificacion", "dispositivo seleccionado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("panelVerificacion", "Datos a grabar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("panelVerificacion", "Atencion: No desconecte el dispositivo despues de poner grabar, o puede romperse y perderse informacion", None, QtGui.QApplication.UnicodeUTF8))
        self.volverBoton.setText(QtGui.QApplication.translate("panelVerificacion", "Volver", None, QtGui.QApplication.UnicodeUTF8))
        self.grabarBoton.setText(QtGui.QApplication.translate("panelVerificacion", "Grabar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    panelVerificacion = QtGui.QWidget()
    ui = Ui_panelVerificacion()
    ui.setupUi(panelVerificacion)
    panelVerificacion.show()
    sys.exit(app.exec_())

