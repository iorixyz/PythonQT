# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoStudentClass.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(630, 409)
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(240, 110, 113, 21))
        self.lineEditCode.setObjectName("lineEditCode")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 110, 111, 21))
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(140, 180, 181, 16))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(190, 200, 114, 32))
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(240, 150, 113, 21))
        self.lineEditName.setObjectName("lineEditName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
