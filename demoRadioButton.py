# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoRadioButton.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 365)
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setGeometry(QtCore.QRect(190, 20, 141, 16))
        self.labelFare.setObjectName("labelFare")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 300, 181, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(70, 60, 131, 16))
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBusinessClass.setGeometry(QtCore.QRect(70, 110, 161, 16))
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(70, 160, 161, 16))
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFare.setText(_translate("Dialog", "Choose the flight type"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Flight $150"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))


