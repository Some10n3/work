import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Convert_currency_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        vbox = QVBoxLayout()
        self.thb_label = QLabel(self)
        self.thb_label.setText("Thai Baht (THB):")
        vbox.addWidget(self.thb_label)

        self.thb_entry = QLineEdit(self)
        self.thb_entry.setText("0.00")
        vbox.addWidget(self.thb_entry)

        self.usd_label = QLabel(self)
        self.usd_label.setText("US Dollar (USD):")
        vbox.addWidget(self.usd_label)

        self.usd_entry = QLineEdit(self)
        self.usd_entry.setText("0.00")
        vbox.addWidget(self.usd_entry)

        thb_to_usd_btn = QPushButton("THB to USD", self)
        thb_to_usd_btn.clicked.connect(self.thb_to_usd)
        vbox.addWidget(thb_to_usd_btn)

        usd_to_thb_btn = QPushButton("USD to THB", self)
        usd_to_thb_btn.clicked.connect(self.usd_to_thb)
        vbox.addWidget(usd_to_thb_btn)

        self.setLayout(vbox)
        self.show()
    
    def thb_to_usd(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        value = float(self.thb_entry.text())

        label = QLabel(self)
        label.setText(f"{value:.02f} THB is {value/30:.02f} USD")
        layout.addWidget(label)

        close_button = QPushButton('Close Window', self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.show()

    def usd_to_thb(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        value = float(self.usd_entry.text())

        label = QLabel(self)
        label.setText(f"{value:.02f} USD is {value*30:.02f} THB")
        layout.addWidget(label)

        close_button = QPushButton('Close Window', self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Convert_currency_window()

    sys.exit(app.exec_())