from datetime import date as Date
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtMultimedia import QSoundEffect
from PySide6 import QtCore
from Booking_List_ui import Ui_list
from Selecting_Booking_ui import Ui_select

class BookingSystem(QMainWindow, object):
    def __init__(self):
        QMainWindow.__init__(self)
        self.observers = []
        self.bookings = {}
        
    def addObserver(self, o):
        self.observers.append(o)
    
    def notifyObservers(self, data):
        for o in self.observers:
            o.update(data)
            
    def addBooking( self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]
            
    def getBookings(self,date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k,v))
        self.notifyObservers(bookings)
        return bookings
    
    def display(self, date):
        self.getBookings(date)
        
    def getstr_booking(self, date):
        booking = []
        for k , v in self.bookings.items():
            if k == date:
                for item in v:
                    temp = str(k) + " : " + item
                    booking.append(temp)
        return "\n".join(booking)
        
class BookingObserver(object):
    def update(self, date):
        pass

class StaffUi(BookingObserver):
    def __init__ (self, S, name):
        self.name = name
        self.system = S
        
    def update(self,bookings):
        print(self.name + ": StaffUi.update():")
        print("-- Booking Data --")
        for data in bookings:
            items = data[1]
            for item in items:
                print(str(data[0])+": "+item)
                
    def submit(self,date):
        self.system.display(date)
        
class bookinglist(QMainWindow):
    def __init__(self, system):  # Added parameter
        QMainWindow.__init__(self)
        self.system = system
        self.ui = Ui_list()
        self.ui.setupUi(self)
        self.ui.select_btn.clicked.connect(self.select)
    
    def select(self):
        self.main = selectbooking()
        self.main.show()  # Corrected: Added parentheses
        self.main.ui.submit_btn.clicked.connect(self.display)

    def display(self):
        day = self.main.ui.day.text()
        month = self.main.ui.month.text()
        year = self.main.ui.year.text()
        date = Date(int(year), int(month), int(day))
        self.ui.text.setText(self.system.getstr_booking(date))
        self.main.close()

class selectbooking(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_select()
        self.ui.setupUi(self)
        self.show()  # Corrected: Added parentheses
        

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = BookingSystem()
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")
    ui1 = StaffUi(s, "UI#1")
    s.addObserver(ui1)
    ui1.submit(Date(2011,10,1))
    window = bookinglist(s)
    window.show()
    sys.exit(app.exec())