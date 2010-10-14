# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/casa/bblug/Dispenser/ui/Forms/PanelGrabacion.ui'
#
# Created: Mon Oct 11 01:50:46 2010
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
        self.label = QtGui.QLabel(panelAhora)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtGui.QProgressBar(panelAhora)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.imagenLabel = QtGui.QLabel(panelAhora)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagenLabel.sizePolicy().hasHeightForWidth())
        self.imagenLabel.setSizePolicy(sizePolicy)
        self.imagenLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imagenLabel.setText("")
        self.imagenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenLabel.setMargin(50)
        self.imagenLabel.setObjectName("imagenLabel")
        self.verticalLayout.addWidget(self.imagenLabel)
        self.terminadoWidget = QtGui.QWidget(panelAhora)
        self.terminadoWidget.setObjectName("terminadoWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.terminadoWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.terminadoWidget)
        font = QtGui.QFont()
        font.setFamily("Bitstream Charter")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.principioBoton = QtGui.QPushButton(self.terminadoWidget)
        self.principioBoton.setObjectName("principioBoton")
        self.horizontalLayout_4.addWidget(self.principioBoton)
        self.verticalLayout.addWidget(self.terminadoWidget)

        self.retranslateUi(panelAhora)
        QtCore.QMetaObject.connectSlotsByName(panelAhora)

    def retranslateUi(self, panelAhora):
        panelAhora.setWindowTitle(QtGui.QApplication.translate("panelAhora", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("panelAhora", "Aguarde mientras se graba el contenido elegido:", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("panelAhora", "Grabando: %p%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("panelAhora", "Grabacion finalizada", None, QtGui.QApplication.UnicodeUTF8))
        self.principioBoton.setText(QtGui.QApplication.translate("panelAhora", "Volver al principio", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    panelAhora = QtGui.QWidget()
    ui = Ui_panelAhora()
    ui.setupUi(panelAhora)
    panelAhora.show()
    sys.exit(app.exec_())

