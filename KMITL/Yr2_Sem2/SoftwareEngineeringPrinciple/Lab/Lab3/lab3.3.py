
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_Form

class phone(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.one_button.clicked.connect(self.dial)
        self.ui.two_button.clicked.connect(self.dial)
        self.ui.three_button.clicked.connect(self.dial)
        self.ui.four_button.clicked.connect(self.dial)
        self.ui.five_button.clicked.connect(self.dial)
        self.ui.six_button.clicked.connect(self.dial)
        self.ui.seven_button.clicked.connect(self.dial)
        self.ui.eight_button.clicked.connect(self.dial)
        self.ui.nine_button.clicked.connect(self.dial)
        self.ui.zero_button.clicked.connect(self.dial)
        self.ui.star_button.clicked.connect(self.dial)
        self.ui.hash_button.clicked.connect(self.dial)

        self.ui.back_button.clicked.connect(self.back)
        self.ui.call_button.clicked.connect(self.call)

    def dial(self):
        label = self.ui.label.text()
        button = self.sender()
        digit = button.text()
        label += digit
        self.ui.label.setText(label)

    def back(self):
        label = self.ui.label.text()
        label = label[:-1]
        self.ui.label.setText(label)

    def call(self):
        label = self.ui.label.text()
        self.ui.label.setText("Calling " + label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = phone()
    ui.show()
    sys.exit(app.exec_())