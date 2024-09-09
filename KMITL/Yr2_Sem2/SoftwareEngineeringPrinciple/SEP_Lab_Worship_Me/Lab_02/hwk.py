import sys
from random import randint
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class ApplicationWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        vbox = QVBoxLayout()
        self.setWindowTitle("Random Number Generator")

        self.label = QLabel(self)
        self.label.setText("Enter the number of Random Digits you want:")
        vbox.addWidget(self.label)

        self.entry = QLineEdit(self)
        vbox.addWidget(self.entry)

        self.btn = QPushButton("Generate Random Number", self) # TODO
        self.btn.clicked.connect(self.generate_random)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)
        self.show()
    
    def generate_random(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        text = ""

        if not self.entry.text().isnumeric():
            text = "Invalid Input, you dum dum"
        
        elif int(self.entry.text()) <= 0:
            text = "Number of digits cannot be <= 0, dum dum"
        
        else:
            text += "Your random number is: "
            for i in range(int(self.entry.text())):
                text += str(randint(0, 9))
        
        label.setText(text)
        layout.addWidget(label)

        close_button = QPushButton('OK', self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ApplicationWindow()
    sys.exit(app.exec_())
