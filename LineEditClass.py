# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LineEditClass.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 409)
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(240, 110, 113, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 110, 111, 21))
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(90, 190, 59, 16))
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(240, 170, 114, 32))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your name"))
        self.labelResponse.setText(_translate("Dialog", "TextLabel"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
