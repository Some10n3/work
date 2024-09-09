import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect
import random

class Rabbit:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 40
        self.h = 40
        self.image = QPixmap("SoftwareEngineeringPrinciple/Lab/Lab4/images/rabbit.png")

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(0, arena_h - self.h)

    def is_hit(self, mouse_x, mouse_y):
        return mouse_x >= self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(300, 300)
        self.arena_h = 300
        self.arena_w = 300
        self.rabbit = Rabbit()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000)
        self.soundH = QSoundEffect()
        self.soundH.setSource(QUrl.fromLocalFile("SoftwareEngineeringPrinciple/Lab/Lab4/sounds/rabbit_hit.wav"))
        self.soundM = QSoundEffect()
        self.soundM.setSource(QUrl.fromLocalFile("SoftwareEngineeringPrinciple/Lab/Lab4/sounds/rabbit_missed.wav"))

    def mousePressEvent(self, e):
        print("Painting")
        if self.rabbit.is_hit(e.pos().x(), e.pos().y()):
            self.soundH.play()
            print("Hit!")
        else:
            self.soundM.play()
            print("Missed!")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.rabbit.draw(p)
        p.end()

    def update_frame(self):
        self.rabbit.random_pos(self.arena_w, self.arena_h)
        self.update()

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.anim_area)
        self.setLayout(self.layout)
        self.setMinimumSize(330, 400)

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
