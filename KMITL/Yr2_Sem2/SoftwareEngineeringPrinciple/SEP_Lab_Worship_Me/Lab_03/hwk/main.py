import sys
from random import randint, seed
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_ui import Ui_Form

class Rng(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)

		self.ui = Ui_Form()
		self.ui.setupUi(self)

		self.rng_value = 0
		self.seed_value = 69
		seed(self.seed_value)

		self.ui.generate_btn.clicked.connect(self.generate_rng)
		self.ui.seed_btn.clicked.connect(self.set_seed)
		self.ui.reset_btn.clicked.connect(self.reset)

	def generate_rng(self):
		output_str = ""
		text = self.ui.digit_entry.text()

		dialog = QDialog(self)
		layout = QVBoxLayout()
		label = QLabel(self)

		if not text.isnumeric():
			output_str = "Invalid Input, you dum dum"

		elif int(text) <= 0:
			output_str = "Input must be greater than 0"

		else:
			output_str = "Your random number is: "
			for i in range(int(text)):
				output_str += str(randint(0, 9))

		label.setText(output_str)
		layout.addWidget(label)

		close_button = QPushButton('OK', self)
		close_button.clicked.connect(dialog.close)
		layout.addWidget(close_button)
		dialog.setLayout(layout)

		dialog.show()

	def set_seed(self):
		seed_str = self.ui.seed_entry.text()
		output_str = ""

		if not seed_str.isnumeric():
			output_str = "Invalid seed input, dum dum"

		else:
			output_str = "Setting seed to: " + seed_str

		self.seed_value = int(seed_str)
		seed(self.seed_value)

		dialog = QDialog(self)
		layout = QVBoxLayout()
		label = QLabel(self)

		label.setText(output_str)
		layout.addWidget(label)

		close_button = QPushButton('OK', self)
		close_button.clicked.connect(dialog.close)
		layout.addWidget(close_button)
		dialog.setLayout(layout)

		dialog.show()

	def reset(self):
		self.seed_value = 69
		seed(self.seed_value)

		dialog = QDialog(self)
		layout = QVBoxLayout()
		label = QLabel(self)

		label.setText("The Seed Value has been reset to its initial state")
		layout.addWidget(label)

		close_button = QPushButton('OK', self)
		close_button.clicked.connect(dialog.close)
		layout.addWidget(close_button)
		dialog.setLayout(layout)

		dialog.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = Rng()
	w.show()
	sys.exit(app.exec_())
