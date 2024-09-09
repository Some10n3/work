import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class convertCurrency(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Currency Converter")
        self.resize(300, 100)
        self.setLayout(QVBoxLayout())

        self.label = QLabel(self)
        self.label.setText("Enter money:")
        self.layout().addWidget(self.label)

        self.input = QLineEdit(self)
        self.layout().addWidget(self.input)

        self.btn = QPushButton("Convert from THB to USD", self)
        self.btn.clicked.connect(self.convertToUSD)

        self.btn2 = QPushButton("Convert from USD to THB", self)
        self.btn2.clicked.connect(self.convertToTHB)

        self.layout().addWidget(self.btn)
        self.layout().addWidget(self.btn2)

        self.show()

    def convertToTHB(self):
        self.input.setText(str(float(self.input.text()) * 35.0))

    def convertToUSD(self):
        self.input.setText(str(float(self.input.text()) / 35.0))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = convertCurrency()
    w.setWindowTitle("Currency Converter")
    w.resize(300, 100)
    
    sys.exit(app.exec_())