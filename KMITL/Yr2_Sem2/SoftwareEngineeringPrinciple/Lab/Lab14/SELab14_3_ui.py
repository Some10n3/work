import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *


class TrafficLight(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Traffic Light Demo")
        self.setGeometry(100, 100, 300, 100)

        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()

        self.button_red = QPushButton("")
        # self.button_red.clicked.connect(self.red)
        layout.addWidget(self.button_red,0,0)

        self.button_yellow = QPushButton("")
        # self.button_yellow.clicked.connect(self.yellow)
        layout.addWidget(self.button_yellow,0,1)

        self.button_green = QPushButton("")
        # self.button_green.clicked.connect(self.green)
        layout.addWidget(self.button_green,0,2)

        self.button_red.setStyleSheet("background-color: red")

        self.label_number = QLabel("Timer: 4")
        layout.addWidget(self.label_number,1,0,1,3)

        self.setLayout(layout)
        self.time = 4
        self.color = "red"

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        

    def loop(self):
        # print("loop")
        # Timer to update the timer every second
        if self.color == "red" and self.time < 1:
            self.color = "green"
            self.change_color(self.color)
            self.setTimer(2)
        elif self.color == "green" and self.time  < 1:
            self.color = "yellow"
            self.change_color(self.color)
            self.setTimer(2)
        elif self.color == "yellow" and self.time < 1:
            self.color = "red"
            self.change_color(self.color)
            self.setTimer(4)

    def setTimer(self, time):
        self.time = time

    def change_color(self, color):
        self.button_red.setStyleSheet("background-color: white")
        self.button_yellow.setStyleSheet("background-color: white")
        self.button_green.setStyleSheet("background-color: white")

        if color == "red":
            self.button_red.setStyleSheet("background-color: red")
        elif color == "yellow":
            self.button_yellow.setStyleSheet("background-color: yellow")
        elif color == "green":
            self.button_green.setStyleSheet("background-color: green")

    def tick(self):
        # print("tick")
        self.loop()
        self.label_number.setText("Timer: {}".format(self.time))
        self.time -= 1
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrafficLight()
    window.show()
    sys.exit(app.exec())
