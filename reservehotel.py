# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\reservehotel.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 517)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(230, 60, 272, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 81, 21))
        self.label_4.setObjectName("label_4")
        self.Enteredinfo = QtWidgets.QLabel(Dialog)
        self.Enteredinfo.setGeometry(QtCore.QRect(160, 410, 251, 31))
        self.Enteredinfo.setText("")
        self.Enteredinfo.setWordWrap(True)
        self.Enteredinfo.setObjectName("Enteredinfo")
        self.RoomRentinfo = QtWidgets.QLabel(Dialog)
        self.RoomRentinfo.setGeometry(QtCore.QRect(60, 440, 441, 51))
        self.RoomRentinfo.setText("")
        self.RoomRentinfo.setWordWrap(True)
        self.RoomRentinfo.setObjectName("RoomRentinfo")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(230, 280, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(230, 330, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 380, 171, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hotel Room Reservation"))
        self.label_2.setText(_translate("Dialog", "Date of Reservation"))
        self.label_3.setText(_translate("Dialog", "number of days"))
        self.label_4.setText(_translate("Dialog", "Room type"))
        self.pushButton.setText(_translate("Dialog", "Calculate Room Rent"))


