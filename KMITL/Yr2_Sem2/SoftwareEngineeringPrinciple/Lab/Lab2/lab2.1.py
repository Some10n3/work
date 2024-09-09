import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *

# class Simple_spin_window(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.num = ""
#         vbox = QVBoxLayout()
#         self.label = QLabel(self)
#         self.label.setText(self.num)
#         vbox.addWidget(self.label)
#         btn = QPushButton("Hello World Button", self)
#         btn.clicked.connect(self.helloWorld)
#         btn.move(50, 50)
#         vbox.addStretch(1)
#         self.setLayout(vbox)
#         self.show()

#     def helloWorld(self):
#         self.num = "Hello World"
#         self.label.setText(self.num)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    btn = QPushButton("Hello World Button", w)
    btn.clicked.connect(lambda: print("Hello World"))
    btn.move(50, 50)
    w.setWindowTitle("Simple")
    w.resize(250, 150)
    w.show()
    sys.exit(app.exec_())