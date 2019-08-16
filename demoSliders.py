# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSliders.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(736, 453)
        self.horizontalScrollBarSugarLevel = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBarSugarLevel.setGeometry(QtCore.QRect(390, 20, 160, 16))
        self.horizontalScrollBarSugarLevel.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarSugarLevel.setObjectName("horizontalScrollBarSugarLevel")
        self.verticalScrollBarPulseRate = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBarPulseRate.setGeometry(QtCore.QRect(260, 140, 16, 160))
        self.verticalScrollBarPulseRate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarPulseRate.setObjectName("verticalScrollBarPulseRate")
        self.horizontalSliderBloodPressure = QtWidgets.QSlider(Dialog)
        self.horizontalSliderBloodPressure.setGeometry(QtCore.QRect(400, 80, 160, 22))
        self.horizontalSliderBloodPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBloodPressure.setObjectName("horizontalSliderBloodPressure")
        self.verticalSliderCholestrolLevel = QtWidgets.QSlider(Dialog)
        self.verticalSliderCholestrolLevel.setGeometry(QtCore.QRect(590, 139, 22, 171))
        self.verticalSliderCholestrolLevel.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderCholestrolLevel.setObjectName("verticalSliderCholestrolLevel")
        self.lineEditResult = QtWidgets.QLineEdit(Dialog)
        self.lineEditResult.setGeometry(QtCore.QRect(240, 350, 311, 20))
        self.lineEditResult.setObjectName("lineEditResult")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 30, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(113, 140, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(443, 150, 111, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sugar Level"))
        self.label_2.setText(_translate("Dialog", "Blood Pressure"))
        self.label_3.setText(_translate("Dialog", "Pulse rate"))
        self.label_4.setText(_translate("Dialog", "Cholestrol Level"))


