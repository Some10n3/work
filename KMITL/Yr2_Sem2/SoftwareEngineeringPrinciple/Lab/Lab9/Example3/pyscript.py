import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime
import random

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        """Return the DOM element associated with this widget."""
        if self._element is None:
            self._element = self.get_element()
        return self._element

    @abstractmethod
    def drawWidget(self):
        pass

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.image = None
        self.button = None
        self.jump_sound = None
        self.stop = False


    def get_element(self):
        return document.getElementById(self.element_id)

    def on_click(self, event):
        if self.stop:
            self.stop = False
            self.button.innerText = "Pause"
        else:
            self.stop = True
            self.button.innerText = "Resume"
        

    def on_set_interval(self):
        if self.stop:
            return
        self.counter += 1
        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def drawWidget(self):
        #display spinning rabbit
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_set_interval = create_proxy(self.on_set_interval)
        js.setInterval(on_set_interval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")

        self.button = document.createElement("button")
        self.button.innerText = "Pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)
        self.color = "red"
        self.button2 = None

    def random_color(self, event):
        self.color = "#" + str(hex(random.randint(0, 16777215)))[2:]
        self.element.style.backgroundColor = self.color

    def drawWidget(self):
        AnimationWidget.drawWidget(self)
        self.button2 = document.createElement("button")
        self.button2.innerText = "Random Color"
        self.button2.style.width = "600px"
        self.button2.onclick = self.random_color
        self.element.appendChild(self.button2)

if __name__ == "__main__":
    # output = AnimationWidget("container")
    output = ColorfulAnimationWidget("container")
    output.drawWidget()
