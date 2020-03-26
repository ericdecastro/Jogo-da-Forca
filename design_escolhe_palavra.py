# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_escolhe_palavra.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EscolhePalavra(object):
    def setupUi(self, EscolhePalavra):
        EscolhePalavra.setObjectName("EscolhePalavra")
        EscolhePalavra.resize(465, 177)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EscolhePalavra.sizePolicy().hasHeightForWidth())
        EscolhePalavra.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(EscolhePalavra)
        self.centralwidget.setObjectName("centralwidget")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(180, 100, 101, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName("okButton")
        self.labelDigitePalavra = QtWidgets.QLabel(self.centralwidget)
        self.labelDigitePalavra.setGeometry(QtCore.QRect(10, 10, 451, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.labelDigitePalavra.setFont(font)
        self.labelDigitePalavra.setObjectName("labelDigitePalavra")
        self.textDigitePalavra = QtWidgets.QLineEdit(self.centralwidget)
        self.textDigitePalavra.setGeometry(QtCore.QRect(10, 50, 441, 28))
        self.textDigitePalavra.setObjectName("textDigitePalavra")
        self.labTesteVariavel = QtWidgets.QLabel(self.centralwidget)
        self.labTesteVariavel.setGeometry(QtCore.QRect(10, 100, 141, 16))
        self.labTesteVariavel.setObjectName("labTesteVariavel")
        EscolhePalavra.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EscolhePalavra)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 22))
        self.menubar.setObjectName("menubar")
        EscolhePalavra.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EscolhePalavra)
        self.statusbar.setObjectName("statusbar")
        EscolhePalavra.setStatusBar(self.statusbar)

        self.retranslateUi(EscolhePalavra)
        QtCore.QMetaObject.connectSlotsByName(EscolhePalavra)

    def retranslateUi(self, EscolhePalavra):
        _translate = QtCore.QCoreApplication.translate
        EscolhePalavra.setWindowTitle(_translate("EscolhePalavra", "Jogo da Forca"))
        self.okButton.setText(_translate("EscolhePalavra", "Ok"))
        self.labelDigitePalavra.setText(_translate("EscolhePalavra", "Digite uma  palavra sem que os jogadores vejam:"))
        self.labTesteVariavel.setText(_translate("EscolhePalavra", "TextLabel"))

