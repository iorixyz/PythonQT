# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
        self.lineEditCountry = QtWidgets.QLineEdit(Dialog)
        self.lineEditCountry.setGeometry(QtCore.QRect(140, 60, 181, 21))
        self.lineEditCountry.setObjectName("lineEditCountry")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 60, 91, 16))
        self.label.setObjectName("label")
        self.pushButtonCountry = QtWidgets.QPushButton(Dialog)
        self.pushButtonCountry.setGeometry(QtCore.QRect(330, 60, 131, 32))
        self.pushButtonCountry.setObjectName("pushButtonCountry")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your Country"))
        self.pushButtonCountry.setText(_translate("Dialog", "Choose Country"))
