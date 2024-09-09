import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect
import random
import math

class Rabbit:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.w = 40
        self.h = 40
        self.frame_no = 0
        self.frame_delay = 0
        self.images = [
            QPixmap("SoftwareEngineeringPrinciple/Homework/hw4/images/frame-" + str(i + 1) + ".png")
            for i in range(4)]
        self.image = self.images[self.frame_no]

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def move_rabbit(self, arena_w, arena_h, target_x, target_y):
        self.frame_delay += 1
        if self.frame_delay >= 20:
            self.frame_delay = 0
            self.frame_no += 1
            if self.frame_no >= 4:
                self.frame_no = 0
            self.image = self.images[self.frame_no]

        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance > 0.5:
            self.x += dx / distance
            self.y += dy / distance
        else:
            self.random_pos(arena_w, arena_h)

    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(arena_h // 2, arena_h - self.h)

    def is_hit(self, circle_center, circle_radius):
       dx = self.x - circle_center[0]
       dy = self.y - circle_center[1]
       distance = math.sqrt(dx**2 + dy**2)
       return distance <= circle_radius

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(300, 300)
        self.arena_h = 300
        self.arena_w = 300
        self.rabbit = Rabbit()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)
        self.soundH = QSoundEffect()
        self.soundH.setSource(QUrl.fromLocalFile("SoftwareEngineeringPrinciple/Homework/hw4/sounds/rabbit_hit.wav"))
        self.soundM = QSoundEffect()
        self.soundM.setSource(QUrl.fromLocalFile("SoftwareEngineeringPrinciple/Homework/hw4/sounds/rabbit_missed.wav"))
        self.circle_radius = 30
        self.circle_center = (self.arena_w // 2, self.arena_h // 2 + self.circle_radius // 2)
        self.background = QPixmap("SoftwareEngineeringPrinciple/Homework/hw4/images/background.png")
        self.label = QLabel(self)
        self.label.setText("")
        font = self.label.font()
        font.setPointSize(10)
        font.setFamily("Arial")
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(self.circle_center[0] - self.circle_radius // 2, self.circle_center[1] - self.circle_radius - 30, 2*self.circle_radius, 10)
        self.label.show()
        self.setFocusPolicy(Qt.StrongFocus)
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            if self.rabbit.is_hit(self.circle_center, self.circle_radius):
                self.soundH.play()
                self.label.setText("Hit!")
                self.label.setStyleSheet("color: green")
            else:
                self.soundM.play()
                self.label.setText("Missed!")
                self.label.setStyleSheet("color: red")
            self.respawn_rabbit()

    def respawn_rabbit(self):
        self.rabbit.random_pos(self.arena_w, self.arena_h)

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, self.arena_w, self.arena_h), self.background)
        self.rabbit.draw(p)
        p.drawEllipse(self.circle_center[0] - self.circle_radius, self.circle_center[1] - self.circle_radius, 2*self.circle_radius, 2*self.circle_radius)
        p.end()

    def update_frame(self):
        self.rabbit.move_rabbit(self.arena_w, self.arena_h, self.circle_center[0] - self.circle_radius // 2, self.circle_center[1] - self.circle_radius // 2)
        self.update()

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.anim_area)
        self.setLayout(self.layout)
        self.setMinimumSize(300, 300)

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())