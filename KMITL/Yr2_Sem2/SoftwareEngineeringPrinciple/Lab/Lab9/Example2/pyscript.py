import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime

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


def get_time():
    return datetime.now().strftime("%H:%M:%S")

class NotificationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.input_text = None
        self.innerText2 = None
        self.button = None
        self.button2 = None

    def on_click(self, event):
        text = self.input_text.value
        js.alert(text + " THB = " + str(float(text) / 30) + " USD")

    def on_click2(self, event):
        text = self.input_text2.value
        js.alert(text + "USD = " + str(float(text) * 30) + " THB")

    def drawWidget(self):
        # Create display text for usd to thb converter
        

        # Create display text for thb to usd converter
        text2 = document.createTextNode("USD to THB Converter")
        self.element.appendChild(text2)
        self.element.appendChild(document.createElement("br"))

        self.input_text2 = document.createElement("input", type="text")
        self.input_text2.style.width = "600px"
        self.element.appendChild(self.input_text2)

        self.button2 = document.createElement("button")
        self.button2.innerText = "Convert"
        self.button2.style.width = "600px"
        self.button2.onclick = self.on_click2
        self.element.appendChild(self.button2)

        #append text to element
        self.element.appendChild(document.createElement("br"))
        text = document.createTextNode("THB to USD Converter")
        self.element.appendChild(text)
        self.element.appendChild(document.createElement("br"))

        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "Convert"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)
    
    def get_element(self):
        return document.getElementById(self.element_id)

if __name__ == "__main__":
    output = NotificationWidget("container")
    output.drawWidget()