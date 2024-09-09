
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_Form

class phone(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.callingBool = False

        self.ui.label.setAlignment(Qt.AlignCenter)

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
        self.ui.call_button.setStyleSheet("color: green")

    def dial(self):
        label = self.ui.label.text()
        if label == "Call Ended":
            label = ""
            self.ui.label.setStyleSheet("color: black")
        button = self.sender()
        digit = button.text()
        label += digit
        self.ui.label.setText(label)

    def back(self):
        label = self.ui.label.text()
        label = label[:-1]
        self.ui.label.setText(label)

    def call(self):
        if self.callingBool:
            self.ui.call_button.setText("Call")
            self.ui.call_button.setStyleSheet("color: green")
            self.callingBool = False
            return
        label = self.ui.label.text()
        self.ui.label.setText("Calling " + label)
        self.callingBool = True
        self.calling()

    def calling(self):
        label = self.ui.label.text()
        self.ui.call_button.setText("End Call")
        self.ui.call_button.setStyleSheet("color: red")
        while self.callingBool:
            if not self.callingBool:
                self.ui.label.setText("Call Ended")
                self.ui.label.setStyleSheet("color: red")
                break
            self.sleep(1)
            self.ui.label.setText(label + " . ")
            if not self.callingBool:
                self.ui.label.setText("Call Ended")
                self.ui.label.setStyleSheet("color: red")
                break
            self.sleep(1)
            self.ui.label.setText(label + " . . ")
            if not self.callingBool:
                self.ui.label.setText("Call Ended")
                self.ui.label.setStyleSheet("color: red")
                break
            self.sleep(1)
            self.ui.label.setText(label + " . . . ")
            if not self.callingBool:
                self.ui.label.setText("Call Ended") 
                self.ui.label.setStyleSheet("color: red")
                break
            self.sleep(1)
            self.ui.label.setText(label)
            if not self.callingBool:
                self.ui.label.setText("Call Ended")
                self.ui.label.setStyleSheet("color: red")
                break

    def sleep(self, sec):
        loop = QEventLoop()
        QTimer.singleShot(sec*1000, loop.quit)
        loop.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = phone()
    ui.show()
    sys.exit(app.exec_())