# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoTwoProgressBarsContextManager.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 379)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 211, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 150, 211, 31))
        self.label_2.setObjectName("label_2")
        self.progressBarFileDownload = QtWidgets.QProgressBar(Dialog)
        self.progressBarFileDownload.setGeometry(QtCore.QRect(170, 70, 231, 23))
        self.progressBarFileDownload.setProperty("value", 0)
        self.progressBarFileDownload.setObjectName("progressBarFileDownload")
        self.progressBarVirusScan = QtWidgets.QProgressBar(Dialog)
        self.progressBarVirusScan.setGeometry(QtCore.QRect(170, 210, 231, 23))
        self.progressBarVirusScan.setProperty("value", 0)
        self.progressBarVirusScan.setObjectName("progressBarVirusScan")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.label_2.setText(_translate("Dialog", "Scanning for Virus"))
