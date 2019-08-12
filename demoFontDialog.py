# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoFontDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 300)
        self.pushButtonFont = QtWidgets.QPushButton(Dialog)
        self.pushButtonFont.setGeometry(QtCore.QRect(160, 20, 151, 41))
        self.pushButtonFont.setObjectName("pushButtonFont")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(100, 80, 291, 201))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonFont.setText(_translate("Dialog", "Change Font"))
