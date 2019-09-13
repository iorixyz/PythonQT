# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDockWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setWindowTitle("")
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(160, 30, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 131, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dockable Sign In Form"))
        self.pushButton.setText(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "Sign In"))
        self.label_2.setText(_translate("MainWindow", "Email Address"))
        self.label_3.setText(_translate("MainWindow", "Password"))
