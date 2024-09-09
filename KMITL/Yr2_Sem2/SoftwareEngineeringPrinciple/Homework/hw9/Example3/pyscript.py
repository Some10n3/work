import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime
import random
import time

images = ["./images/25.png", "./images/50.png", "./images/60.png", "./images/75.png", "./images/90.png", "./images/100.png"]

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
        self.counter = 0
        self.image = None
        self.image2 = None
        self.button = None
        self.jump_sound = None
        self.stop = False   
        # time now
        self.timer = time.time()



    def get_element(self):
        return document.getElementById(self.element_id)

    def on_click(self, event):
        if self.stop:
            self.stop = False
            # self.button.innerText = "Spin"
        else:
            self.stop = True
            # self.button.innerText = "Stop"
            #if sound is playing stop it
            if self.jump_sound:
                self.jump_sound.pause()
                self.jump_sound.currentTime = 0
            self.jump_sound.play()
            

            
        

    def on_set_interval(self):
        if self.stop:
            self.counter += 1
            if self.counter > 5:
                self.counter = 0
            self.image.src = images[self.counter]
            if time.time() - self.timer > 10:
                self.stop = False
                self.timer = time.time()
                self.check_score()

    def check_score(self):
        score = 0
        self.image.src = images[self.counter]
        #switch case
        if self.counter == 1:
            score = 50
        elif self.counter == 2:
            score = 60
        elif self.counter == 3:
            score = 75
        elif self.counter == 4:
            score = 90
        elif self.counter == 5:
            score = 100
        elif self.counter == 0:
            score = 25
        
        self.alert_score(score)

    def alert_score(self, score):
        self.element.appendChild(document.createElement("br"))
        innerText = "You won " + str(score) + " points!"
        self.element.appendChild(document.createTextNode(innerText))
        
        if score == 100:
            self.element.appendChild(document.createElement("br"))
            self.element.appendChild(document.createTextNode("You won the jackpot!"))
        elif score == 25:
            self.element.appendChild(document.createElement("br"))
            self.element.appendChild(document.createTextNode("Tip : "))
            self.element.appendChild(document.createElement("br"))
            self.image2 = document.createElement("img")
            self.image2.style.width = "100px"
            self.image2.style.height = "100px"
            self.image2.src = "./images/tip.jpg"
            self.element.appendChild(self.image2)


    def drawWidget(self):
        #display spinning rabbit
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = images[self.counter]
        self.element.appendChild(self.image)

        on_set_interval = create_proxy(self.on_set_interval)
        js.setInterval(on_set_interval, 100)

        self.jump_sound = js.Audio.new("./sounds/roulette.mp3")

        self.element.appendChild(document.createElement("br"))

        self.button = document.createElement("button")
        self.button.innerText = "Spin"
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
