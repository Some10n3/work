import sys
import vlc
import threading
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *

class Radio:
	def __init__(self):
		self.instance = vlc.Instance('--input-repeat=-1', '--no-video')
		self.player = self.instance.media_player_new()
		self.media = self.instance.media_new("https://listen.moe/stream")
		self.player.set_media(self.media)

		self.is_playing = False
		self.thread_spawned = False
		self.thread_finished = True

		self.radio_thread = None

	def play(self):
		if not self.thread_spawned:
			self.radio_thread = threading.Thread(target=self.play_stream)
			self.radio_thread.start()
			self.thread_spawned = True
			self.thread_finished = False

	def play_stream(self):
		self.is_playing = True
		self.player.play()

		while(True):
			if not self.is_playing:
				break
			self.player.audio_set_mute(False)
			self.player.audio_set_volume(50)

		print("Stopped")
		self.player.stop()
		self.thread_finished = True

	def stop(self):
		if not self.is_playing:
			return
		if self.radio_thread is None:
			return
		self.is_playing = False
		while(not self.thread_finished):
			pass

		self.radio_thread.join()
		self.thread_spawned = False
		self.thread_finished = False


class AnimationArea(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)

		self.PATH = "loading/frame-"
		self.frame_no = 0
		self.cum_frame_no = 0
		self.images = [
			QPixmap(self.PATH + str(i+1) + ".png") for i in range(30)
		]

		self.radio = Radio()

		self.is_playing = True
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_value)

		self.QSE = QSoundEffect()
		self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))

	def paintEvent(self, e):
		p = QPainter()
		p.begin(self)
		p.drawPixmap(QRect(75, 0, 40, 40), self.images[self.frame_no])
		p.end()

	def update_value(self):
		self.frame_no += 1
		self.cum_frame_no += 1
		if self.frame_no >= 30:
			self.frame_no = 0
		if self.cum_frame_no == 60:
			self.frame_no = 0
			self.cum_frame_no = 0
			self.timer.stop()
			self.hide()
			self.QSE.play()
			self.radio.play()
		self.update()

	def play(self):
		self.timer.start(75)

	def get_radio(self):
		return self.radio


class MainApp(QWidget):
	def __init__(self):
		QWidget.__init__(self, None)

		self.is_playing = False

		layout = QVBoxLayout()

		self.anim_area = AnimationArea()
		layout.addWidget(self.anim_area)
		self.anim_area.hide()

		self.radio = self.anim_area.get_radio()

		self.play_btn = QPushButton("Play LISTEN.moe")
		self.play_btn.clicked.connect(self.btn_callback)
		layout.addWidget(self.play_btn)

		self.setLayout(layout)
		self.setMinimumSize(200, 100)

	def btn_callback(self):
		if not self.is_playing:
			self.is_playing = True
			self.anim_area.show()
			self.anim_area.play()
			self.play_btn.setText("Stop")
		else:
			self.is_playing = False
			self.play_btn.setText("Play LISTEN.moe")
			self.radio.stop()

	def closeEvent(self, e):
		self.radio.stop()

def main():
	app = QApplication(sys.argv)

	w = MainApp()
	w.show()

	return app.exec()

if __name__ == "__main__":
	sys.exit(main())
