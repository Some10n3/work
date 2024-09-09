import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class BookingSystem(object):
    def __init__(self):
        self.observers = []
        self.bookings = {}

    def addObserver(self, o):
        self.observers.append(o)

    def notifyObservers(self, data):
        for o in self.observers:
            o.update(data)

    def addBooking(self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]

    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k, v))

        self.notifyObservers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)


class BookingObserver(object):
    def update(self, data):
        pass

class StaffUi(BookingObserver, QWidget):
    def __init__(self,s,name):
        QWidget.__init__(self, None)
        self.name = name
        self.system = s

        self.build_ui()

    def update(self,bookings):
        output_str = ""
        print(self.name + ": StaffUi.update():")
        print("-- Booking Data --")
        for data in bookings:
            items = data[1]
            for item in items:
                temp_o = str(data[0]) + ": " + item
                print(temp_o)
                output_str += temp_o + "\n"

        if output_str == "":
            output_str = "No Booking Found"
        self.booking_text.setText(output_str)

    def submit(self, date):
        self.system.display(date)
    
    def build_ui(self):
        layout = QVBoxLayout()
        
        self.booking_text  = QTextEdit()
        self.booking_text.setReadOnly(True)

        self.select_booking_btn = QPushButton("Select Bookings ...")
        self.select_booking_btn.clicked.connect(self.btn_callback)

        layout.addWidget(self.booking_text)
        layout.addWidget(self.select_booking_btn)

        self.setLayout(layout)
        self.setMinimumSize(300, 300)

    def btn_callback(self):
        print("Hello")
        self.popup = QWidget()

        layout = QGridLayout()

        self.day_lbl = QLabel("Day")
        self.day_entry = QLineEdit()

        self.mth_lbl = QLabel("Month")
        self.mth_entry = QLineEdit()

        self.yr_lbl = QLabel("Year")
        self.yr_entry = QLineEdit()

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.popup_btn_callback)

        layout.addWidget(self.day_lbl, 0, 0, 1, 1)
        layout.addWidget(self.day_entry, 0, 1, 1, 1)
        layout.addWidget(self.mth_lbl, 1, 0, 1, 1)
        layout.addWidget(self.mth_entry, 1, 1, 1, 1)
        layout.addWidget(self.yr_lbl, 2, 0, 1, 1)
        layout.addWidget(self.yr_entry, 2, 1, 1, 1)
        layout.addWidget(self.submit_btn, 3, 0, 1, 2)

        self.popup.setLayout(layout)
        self.popup.show()

    def popup_btn_callback(self):
        day = int(self.day_entry.text())
        mth = int(self.mth_entry.text())
        yr = int(self.yr_entry.text())

        self.submit(Date(yr, mth, day))
        self.popup.close()
    
from datetime import date as Date

def main():
    app = QApplication(sys.argv)

    s =  BookingSystem()
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")

    ui1 =  StaffUi(s,"UI#1")
    s.addObserver(ui1)

    ui1.submit(Date(2011, 10 ,1))
    ui1.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
