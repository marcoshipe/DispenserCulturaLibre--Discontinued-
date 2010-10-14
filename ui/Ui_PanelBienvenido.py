# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/casa/bblug/Dispenser/ui/Forms/PanelBienvenido.ui'
#
# Created: Sun Oct 10 16:22:34 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_panelBienvenido(object):
    def setupUi(self, panelBienvenido):
        panelBienvenido.setObjectName("panelBienvenido")
        panelBienvenido.resize(739, 534)
        panelBienvenido.setAutoFillBackground(True)
        self.gridLayout = QtGui.QGridLayout(panelBienvenido)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(panelBienvenido)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelBienvenido = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        self.labelBienvenido.setFont(font)
        self.labelBienvenido.setObjectName("labelBienvenido")
        self.verticalLayout_2.addWidget(self.labelBienvenido)
        spacerItem = QtGui.QSpacerItem(20, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.widgetDescripcion = QtGui.QWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetDescripcion.sizePolicy().hasHeightForWidth())
        self.widgetDescripcion.setSizePolicy(sizePolicy)
        self.widgetDescripcion.setObjectName("widgetDescripcion")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetDescripcion)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.plainTextEditDescripcion = QtGui.QPlainTextEdit(self.widgetDescripcion)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditDescripcion.sizePolicy().hasHeightForWidth())
        self.plainTextEditDescripcion.setSizePolicy(sizePolicy)
        self.plainTextEditDescripcion.setMinimumSize(QtCore.QSize(0, 250))
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
        self.verticalLayout_2.addWidget(self.widgetDescripcion)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        self.widgetSiguiente = QtGui.QWidget(panelBienvenido)
        self.widgetSiguiente.setObjectName("widgetSiguiente")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetSiguiente)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.botonSiguiente = QtGui.QPushButton(self.widgetSiguiente)
        self.botonSiguiente.setObjectName("botonSiguiente")
        self.horizontalLayout.addWidget(self.botonSiguiente)
        self.gridLayout.addWidget(self.widgetSiguiente, 3, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(10, 5, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem6, 0, 1, 1, 1)

        self.retranslateUi(panelBienvenido)
        QtCore.QMetaObject.connectSlotsByName(panelBienvenido)

    def retranslateUi(self, panelBienvenido):
        panelBienvenido.setWindowTitle(QtGui.QApplication.translate("panelBienvenido", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBienvenido.setText(QtGui.QApplication.translate("panelBienvenido", "Bienvenido", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEditDescripcion.setPlainText(QtGui.QApplication.translate("panelBienvenido", "Este es un programa con el cual ustede podra llevarse contenido libre, o sea, peliculas, musica, libros, imagenes y software, entre otros, que el autor permite que se comparta (si, usted tambien se lo va a poder prestar a sus amigos).\n"
"\n"
"Por ahora tenemos poco contenido, usted puede informarnos sobre algun contenido de su agrado enviandonos un mail a (ACA VA EL MAIL ;) )\n"
"\n"
"Este programa tambien es libre, por lo cual puede compartirse (tambien puede verse como se hizo, modificarse, etc, ya que es software libre licenciado bajo la GPL v2)\n"
"\n"
"Cualquier mejora que quiera proponer puede hacerla a este mail (ACA VA EL MISMO MAIL U OTRO)\n"
"\n"
"Esperamos que disfrute del programa", None, QtGui.QApplication.UnicodeUTF8))
        self.botonSiguiente.setText(QtGui.QApplication.translate("panelBienvenido", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    panelBienvenido = QtGui.QWidget()
    ui = Ui_panelBienvenido()
    ui.setupUi(panelBienvenido)
    panelBienvenido.show()
    sys.exit(app.exec_())

