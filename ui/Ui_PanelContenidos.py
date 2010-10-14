# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/casa/bblug/Dispenser/ui/Forms/PanelContenidos.ui'
#
# Created: Sun Aug  8 15:21:40 2010
#      by: PyQt4 UI code generator 4.7.2
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    panelQue = QtGui.QWidget()
    ui = Ui_panelQue()
    ui.setupUi(panelQue)
    panelQue.show()
    sys.exit(app.exec_())

