# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSimpleInheritance.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(608, 366)
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(290, 40, 113, 21))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lineEditGeographyMarks = QtWidgets.QLineEdit(Dialog)
        self.lineEditGeographyMarks.setGeometry(QtCore.QRect(290, 160, 113, 21))
        self.lineEditGeographyMarks.setObjectName("lineEditGeographyMarks")
        self.lineEditHistoryMarks = QtWidgets.QLineEdit(Dialog)
        self.lineEditHistoryMarks.setGeometry(QtCore.QRect(290, 120, 113, 21))
        self.lineEditHistoryMarks.setObjectName("lineEditHistoryMarks")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(290, 80, 113, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 131, 16))
        self.label_4.setObjectName("label_4")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 210, 341, 31))
        self.labelResponse.setText("")
        self.labelResponse.setWordWrap(True)
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(190, 270, 114, 32))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.label_3.setText(_translate("Dialog", "History Marks"))
        self.label_4.setText(_translate("Dialog", "Geography Marks"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
