import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton2 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)


    def dispSelected(self):
        selected_size = "";
        selected_payment = "";
        if self.ui.radioButtonMedium.isChecked() == True:
            selected_size = "Medium"
        if self.ui.radioButtonLarge.isChecked() == True:
            selected_size = "Large"
        if self.ui.radioButtonXL.isChecked() == True:
            selected_size = "Extra Large"
        if self.ui.radioButtonXXL.isChecked() == True:
            selected_size = "Extra Extra Large"

        if self.ui.radioButtonNetBanking.isChecked() ==True:
            selected_payment = "NetBanking"
        if self.ui.radioButtonDebitCard.isChecked() == True:
            selected_payment = "Debit/ Credit Card"
        if self.ui.radioButtonCashOnDelivery.isChecked() == True:
            selected_payment = "Cash On Delivery"
        self.ui.labelSelected.setText("Chosen shirt siez is " + selected_size + " and payment method as " + selected_payment)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())