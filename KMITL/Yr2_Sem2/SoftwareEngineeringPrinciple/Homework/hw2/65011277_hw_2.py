import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class convertTemperature(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Temperature Converter")
        self.resize(300, 100)
        self.setLayout(QVBoxLayout())

        self.label = QLabel(self)
        self.label.setText("Enter temperature:")
        self.layout().addWidget(self.label)

        self.input = QLineEdit(self)
        self.layout().addWidget(self.input)

        self.btn = QPushButton("Convert from Celsius to Fahrenheit", self)
        self.btn.clicked.connect(self.convertToFahrenheit)

        self.btn2 = QPushButton("Convert from Fahrenheit to Celsius", self)
        self.btn2.clicked.connect(self.convertToCelsius)

        self.layout().addWidget(self.btn)
        self.layout().addWidget(self.btn2)

        self.show()

    def convertToFahrenheit(self):
        self.input.setText(str(round((float(self.input.text()) * 1.8) + 32, 2)))

    def convertToCelsius(self):
        self.input.setText(str(round((float(self.input.text()) - 32) / 1.8, 2)))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = convertTemperature()
    w.setWindowTitle("Temperatiure Converter")
    w.resize(300, 100)
    
    sys.exit(app.exec_())