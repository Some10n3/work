import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import QSoundEffect

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.frame_no = 0
        self.images = [
            QPixmap("SoftwareEngineeringPrinciple/Lab/Lab4/images/frame-" + str(i + 1) + ".png")
            for i in range(20)]
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(75)
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("SoftwareEngineeringPrinciple/Lab/Lab4/sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_frame(self):
        self.frame_no += 1
        if self.frame_no >= 20:
            self.frame_no = 0
            self.sound.play()
        self.update()

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.anim_area)
        self.layout.addWidget(QPushButton("Pause"))
        self.setLayout(self.layout)
        #connect button to pause_play method
        self.layout.itemAt(1).widget().clicked.connect(self.pause_play)
        self.setMinimumSize(330, 400)

    def pause_play(self):
        if self.anim_area.timer.isActive():
            self.anim_area.timer.stop()
            #change text on button to "Play"
            self.layout.itemAt(1).widget().setText("Play")
        else:
            self.anim_area.timer.start()
            #change text on button to "Pause"
            self.layout.itemAt(1).widget().setText("Pause")

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())