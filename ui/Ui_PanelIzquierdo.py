# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/casa/bblug/Dispenser/ui/Forms/PanelIzquierdo.ui'
#
# Created: Sun Oct 10 16:46:14 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelIzquierdo(object):
    def setupUi(self, panelIzquierdo):
        panelIzquierdo.setObjectName("panelIzquierdo")
        panelIzquierdo.resize(385, 490)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(panelIzquierdo.sizePolicy().hasHeightForWidth())
        panelIzquierdo.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(panelIzquierdo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bienvenidoFrame = QtGui.QFrame(panelIzquierdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bienvenidoFrame.sizePolicy().hasHeightForWidth())
        self.bienvenidoFrame.setSizePolicy(sizePolicy)
        self.bienvenidoFrame.setAutoFillBackground(True)
        self.bienvenidoFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.bienvenidoFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.bienvenidoFrame.setObjectName("bienvenidoFrame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.bienvenidoFrame)
        self.horizontalLayout.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.bienvenidoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../../usr/share/icons/Humanity/actions/16/forward.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.bienvenidoLabel = QtGui.QLabel(self.bienvenidoFrame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.bienvenidoLabel.setFont(font)
        self.bienvenidoLabel.setObjectName("bienvenidoLabel")
        self.horizontalLayout.addWidget(self.bienvenidoLabel)
        spacerItem = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.bienvenidoFrame)
        self.dispositivosFrame = QtGui.QFrame(panelIzquierdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispositivosFrame.sizePolicy().hasHeightForWidth())
        self.dispositivosFrame.setSizePolicy(sizePolicy)
        self.dispositivosFrame.setAutoFillBackground(True)
        self.dispositivosFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.dispositivosFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.dispositivosFrame.setObjectName("dispositivosFrame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dispositivosFrame)
        self.horizontalLayout_2.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.dispositivosFrame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../../../../usr/share/icons/Humanity/actions/16/forward.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dispositivosLabel = QtGui.QLabel(self.dispositivosFrame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.dispositivosLabel.setFont(font)
        self.dispositivosLabel.setObjectName("dispositivosLabel")
        self.horizontalLayout_2.addWidget(self.dispositivosLabel)
        spacerItem1 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.dispositivosFrame)
        self.contenidosFrame = QtGui.QFrame(panelIzquierdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contenidosFrame.sizePolicy().hasHeightForWidth())
        self.contenidosFrame.setSizePolicy(sizePolicy)
        self.contenidosFrame.setAutoFillBackground(True)
        self.contenidosFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.contenidosFrame.setFrameShadow(QtGui.QFrame.Plain)
        self.contenidosFrame.setObjectName("contenidosFrame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.contenidosFrame)
        self.horizontalLayout_3.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtGui.QLabel(self.contenidosFrame)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../../../usr/share/icons/Humanity/actions/16/forward.svg"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.contenidosLabel = QtGui.QLabel(self.contenidosFrame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.contenidosLabel.setFont(font)
        self.contenidosLabel.setObjectName("contenidosLabel")
        self.horizontalLayout_3.addWidget(self.contenidosLabel)
        spacerItem2 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.contenidosFrame)
        self.verificacionFrame = QtGui.QFrame(panelIzquierdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verificacionFrame.sizePolicy().hasHeightForWidth())
        self.verificacionFrame.setSizePolicy(sizePolicy)
        self.verificacionFrame.setAutoFillBackground(True)
        self.verificacionFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.verificacionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.verificacionFrame.setObjectName("verificacionFrame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.verificacionFrame)
        self.horizontalLayout_4.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtGui.QLabel(self.verificacionFrame)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../../../../../usr/share/icons/Humanity/actions/16/forward.svg"))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verificacionLabel = QtGui.QLabel(self.verificacionFrame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.verificacionLabel.setFont(font)
        self.verificacionLabel.setObjectName("verificacionLabel")
        self.horizontalLayout_4.addWidget(self.verificacionLabel)
        spacerItem3 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.verificacionFrame)
        self.grabacionFrame = QtGui.QFrame(panelIzquierdo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grabacionFrame.sizePolicy().hasHeightForWidth())
        self.grabacionFrame.setSizePolicy(sizePolicy)
        self.grabacionFrame.setAutoFillBackground(True)
        self.grabacionFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.grabacionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.grabacionFrame.setObjectName("grabacionFrame")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.grabacionFrame)
        self.horizontalLayout_5.setContentsMargins(-1, 1, -1, 1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtGui.QLabel(self.grabacionFrame)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../../../../usr/share/icons/Humanity/actions/16/forward.svg"))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.grabacionLabel = QtGui.QLabel(self.grabacionFrame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setWeight(75)
        font.setBold(True)
        self.grabacionLabel.setFont(font)
        self.grabacionLabel.setObjectName("grabacionLabel")
        self.horizontalLayout_5.addWidget(self.grabacionLabel)
        spacerItem4 = QtGui.QSpacerItem(3, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.grabacionFrame)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)

        self.retranslateUi(panelIzquierdo)
        QtCore.QMetaObject.connectSlotsByName(panelIzquierdo)

    def retranslateUi(self, panelIzquierdo):
        panelIzquierdo.setWindowTitle(QtGui.QApplication.translate("panelIzquierdo", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.bienvenidoLabel.setText(QtGui.QApplication.translate("panelIzquierdo", "1) Bienvenido", None, QtGui.QApplication.UnicodeUTF8))
        self.dispositivosLabel.setText(QtGui.QApplication.translate("panelIzquierdo", "2) Elegir donde grabar", None, QtGui.QApplication.UnicodeUTF8))
        self.contenidosLabel.setText(QtGui.QApplication.translate("panelIzquierdo", "3) Elegir que contenido grabar", None, QtGui.QApplication.UnicodeUTF8))
        self.verificacionLabel.setText(QtGui.QApplication.translate("panelIzquierdo", "4) Verificación de datos", None, QtGui.QApplication.UnicodeUTF8))
        self.grabacionLabel.setText(QtGui.QApplication.translate("panelIzquierdo", "5) Grabación", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    panelIzquierdo = QtGui.QWidget()
    ui = Ui_panelIzquierdo()
    ui.setupUi(panelIzquierdo)
    panelIzquierdo.show()
    sys.exit(app.exec_())

