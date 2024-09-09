import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Simple_spin_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.num = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)
        plus = QPushButton("+", self)
        plus.clicked.connect(self.updateNumber)
        vbox.addWidget(plus)
        minus = QPushButton("-", self)
        minus.clicked.connect(self.updateNumber)
        vbox.addWidget(minus)
        reset = QPushButton("Reset", self)
        reset.clicked.connect(self.updateNumber)
        vbox.addWidget(reset)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.show()

    def updateNumber(self):
        sender = self.sender()
        if sender.text() == "+":
            self.num += 1
        elif sender.text() == "Reset":
            self.num = 0
        else:
            self.num -= 1
        self.label.setText(str(self.num))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Simple_spin_window()
    w.setWindowTitle("numCounter")
    w.resize(300, 100)
    
    sys.exit(app.exec_())