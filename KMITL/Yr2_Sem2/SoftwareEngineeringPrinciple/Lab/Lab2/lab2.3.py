import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Simple_timer_window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.num = time.strftime("%X")
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)
        timer = QTimer(self)
        timer.timeout.connect(self.updateTime)
        timer.start(500)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.show()

    def updateTime(self):
        self.num = time.strftime("%X")
        self.label.setText(str(self.num))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Simple_timer_window()
    w.setWindowTitle("timeCounter")
    w.resize(300, 100)
    
    sys.exit(app.exec_())