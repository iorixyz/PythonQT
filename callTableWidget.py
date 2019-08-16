import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from DemotableWIdget import *


class MyForm(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = data
        self.addcontent()

    def addcontent(self):
        row = 0
        col = 0
        for tup in self.data:
            for item in tup:
                oneitem = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, oneitem)
                col += 1
        row += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    data = []
    data.append(('Suite', '39'))
    data.append(('SuperLuxury', '29'))
    data.append(('Super Deluxe', '19'))
    data.append(('Ordinary', '9'))
    w = MyForm(data)
    w.show()
    sys.exit(app.exec_())
