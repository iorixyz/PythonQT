# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoCheckbox2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 486)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 20, 54, 12))
        self.label.setObjectName("label")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(100, 360, 121, 51))
        self.labelAmount.setText("")
        self.labelAmount.setWordWrap(True)
        self.labelAmount.setObjectName("labelAmount")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 270, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(63, 70, 131, 20))
        self.label_4.setObjectName("label_4")
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(210, 70, 201, 151))
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChoclateChips.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxCookieDough.setGeometry(QtCore.QRect(20, 60, 161, 16))
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChoclateAlmond.setGeometry(QtCore.QRect(20, 90, 151, 16))
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxRockyRoad.setGeometry(QtCore.QRect(20, 120, 121, 16))
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(380, 260, 131, 131))
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxCoffee.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxSoda.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxTea.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.checkBoxTea.setObjectName("checkBoxTea")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_3.setText(_translate("Dialog", "Select your Drink"))
        self.label_4.setText(_translate("Dialog", "Select your Icecream"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "IceCream"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Choclate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Choclate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))


