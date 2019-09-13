# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMenuBar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 30, 151, 51))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 23))
        self.menubar.setObjectName("menubar")
        self.menuDraw = QtWidgets.QMenu(self.menubar)
        self.menuDraw.setObjectName("menuDraw")
        self.menuProperties = QtWidgets.QMenu(self.menuDraw)
        self.menuProperties.setObjectName("menuProperties")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDraw_Circle = QtWidgets.QAction(MainWindow)
        self.actionDraw_Circle.setObjectName("actionDraw_Circle")
        self.actionDraw_Retangle = QtWidgets.QAction(MainWindow)
        self.actionDraw_Retangle.setObjectName("actionDraw_Retangle")
        self.actionDraw_Line = QtWidgets.QAction(MainWindow)
        self.actionDraw_Line.setObjectName("actionDraw_Line")
        self.actionPage_Setup = QtWidgets.QAction(MainWindow)
        self.actionPage_Setup.setObjectName("actionPage_Setup")
        self.actionSet_Password = QtWidgets.QAction(MainWindow)
        self.actionSet_Password.setObjectName("actionSet_Password")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuProperties.addAction(self.actionPage_Setup)
        self.menuProperties.addAction(self.actionSet_Password)
        self.menuDraw.addAction(self.actionDraw_Circle)
        self.menuDraw.addAction(self.actionDraw_Retangle)
        self.menuDraw.addAction(self.actionDraw_Line)
        self.menuDraw.addSeparator()
        self.menuDraw.addAction(self.menuProperties.menuAction())
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuDraw.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuDraw.setTitle(_translate("MainWindow", "Draw"))
        self.menuProperties.setTitle(_translate("MainWindow", "Properties"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionDraw_Circle.setText(_translate("MainWindow", "To draw a circle"))
        self.actionDraw_Circle.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionDraw_Retangle.setText(_translate("MainWindow", "Draw Retangle"))
        self.actionDraw_Line.setText(_translate("MainWindow", "Draw Line"))
        self.actionPage_Setup.setText(_translate("MainWindow", "Page Setup"))
        self.actionSet_Password.setText(_translate("MainWindow", "Set Password"))
        self.actionSet_Password.setShortcut(_translate("MainWindow", "Shift+P"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
