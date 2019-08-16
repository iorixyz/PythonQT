# -*- coding: utf-8 -*-

try:
    from PySide import QtCore
    from PySide import QtWidgets
    from PySide import QtQuick
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets
    from PyQt5 import QtQuick


class good:
    def __init__(self):