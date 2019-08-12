# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoColorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(465, 331)
        self.pushButtonColor = QtWidgets.QPushButton(Dialog)
        self.pushButtonColor.setGeometry(QtCore.QRect(40, 90, 114, 32))
        self.pushButtonColor.setObjectName("pushButtonColor")
        self.frameColor = QtWidgets.QFrame(Dialog)
        self.frameColor.setGeometry(QtCore.QRect(200, 50, 221, 131))
        self.frameColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameColor.setObjectName("frameColor")
        self.labelColor = QtWidgets.QLabel(Dialog)
        self.labelColor.setGeometry(QtCore.QRect(70, 170, 59, 16))
        self.labelColor.setObjectName("labelColor")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonColor.setText(_translate("Dialog", "Choose Color"))
        self.labelColor.setText(_translate("Dialog", "TextLabel"))
