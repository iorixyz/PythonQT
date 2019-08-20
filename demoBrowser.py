# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1009, 685)
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        self.pushButtonGo.setGeometry(QtCore.QRect(560, 580, 75, 23))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        self.lineEditURL.setGeometry(QtCore.QRect(210, 580, 291, 20))
        self.lineEditURL.setObjectName("lineEditURL")
        self.widget = QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 50, 851, 491))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 580, 91, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonGo.setText(_translate("Dialog", "Go"))
        self.label.setText(_translate("Dialog", "Enter URL"))


from PyQt5.QtWebEngineWidgets import QWebEngineView
