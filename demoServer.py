# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoServer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(641, 417)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 40, 51, 16))
        self.label.setObjectName("label")
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        self.lineEditMessage.setGeometry(QtCore.QRect(70, 360, 281, 20))
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(390, 360, 75, 23))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.textEditMessages = QtWidgets.QTextEdit(Dialog)
        self.textEditMessages.setGeometry(QtCore.QRect(70, 70, 281, 271))
        self.textEditMessages.setObjectName("textEditMessages")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Server"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
