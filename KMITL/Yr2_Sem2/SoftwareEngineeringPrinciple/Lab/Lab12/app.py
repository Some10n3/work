from abc import ABC, abstractmethod
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_form import Ui_MainWindow
from ui_form2 import Ui_Form
from datetime import date as Date

class BookingSystem(object):
    def __init__(self):
        self.observers = []
        self.bookings = {}

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

    def addBooking(self, date, bookings):
        if date in self.bookings:
            self.bookings[date].append(bookings)
        else:
            self.bookings[date] = [bookings]

    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append(v)
                # print(k, v)

        # self.notify_observers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)

class BookingObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass

class StaffUI(BookingObserver):
    def __init__(self, name, s):
        self.name = name
        self.system = s

    def update(self, bookings):
        print(self.name + ": StaffUI.update():")
        print("--Booking Data--")
        for data in bookings:
            print(data)

    def submit(self, date):
        self.system.display(date)

class BookingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Booking List")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.selectBooking.clicked.connect(self.selectBooking)

    def selectBooking(self):
        # print("BookingWindow.selectBooking()")
        # text = ""
        # for date in s.bookings:
        #     text += str(date) + " : " + str(s.bookings[date]) + "\n" + "\n"
        # self.ui.plainTextEdit.setPlainText(text)
        # print(s.bookings)
        self.selectUI = SelectBooking()
        self.selectUI.show()
        self.selectUI.ui.pushButton.clicked.connect(self.submit)
        # close self

    def setCentralWidget(self, widget):
        return

    def setDocumentMode(self, mode):
        return

    def submit(self):
        day = int(self.selectUI.ui.plainTextEdit.toPlainText())
        month = int(self.selectUI.ui.plainTextEdit_2.toPlainText())
        year = int(self.selectUI.ui.plainTextEdit_3.toPlainText())
        date = Date(year, month, day)
        # s.display(date)
        text = ""
        for date2 in s.bookings:
            if date == date2:
                text += str(date2) + " : " + str(s.bookings[date2]) + "\n" + "\n"
        self.ui.plainTextEdit.setPlainText(text)
        self.selectUI.close()
    
    def update(self, data):
        s.display(data)

    def show(self):
        QWidget.show(self)
        
class SelectBooking(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Select Booking")
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    
    


if __name__ == "__main__":
    s = BookingSystem()
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")

    ui1 = StaffUI("UI1", s)

    s.add_observer(ui1)

    ui1.submit(Date(2011, 10, 1))

    app = QApplication(sys.argv)
    window = BookingWindow()
    window.show()

    sys.exit(app.exec())

