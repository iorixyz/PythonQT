import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPainter
from demoDrawLine import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        qp.end()

    def mousePressEvent(self, event):
        if event.bottons() & QtCore.Qt.LeftButton:
            self.pos1[0],  self.pos1[1] = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())