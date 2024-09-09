from fileinput import close
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_MainWindow

class CallUi(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.text = ""

        self.ui.btn_0.clicked.connect(lambda x: self.btn_callback(0))
        self.ui.btn_1.clicked.connect(lambda x: self.btn_callback(1))
        self.ui.btn_2.clicked.connect(lambda x: self.btn_callback(2))    
        self.ui.btn_3.clicked.connect(lambda x: self.btn_callback(3))    
        self.ui.btn_4.clicked.connect(lambda x: self.btn_callback(4))    
        self.ui.btn_5.clicked.connect(lambda x: self.btn_callback(5))    
        self.ui.btn_6.clicked.connect(lambda x: self.btn_callback(6))    
        self.ui.btn_7.clicked.connect(lambda x: self.btn_callback(7))    
        self.ui.btn_8.clicked.connect(lambda x: self.btn_callback(8))    
        self.ui.btn_9.clicked.connect(lambda x: self.btn_callback(9))    
        self.ui.btn_star.clicked.connect(lambda x: self.btn_callback(-1))    
        self.ui.btn_pound.clicked.connect(lambda x: self.btn_callback(-2))
        
        self.ui.btn_delete.clicked.connect(self.del_callback)
        self.ui.btn_talk.clicked.connect(self.talk_callback)
    
    def btn_callback(self, num):
        if num == -1:
            self.text += "*"
        elif num == -2:
            self.text += "#"
        else:
            self.text += str(num)
        
        self.ui.lineEdit.setText(self.text)
    
    def del_callback(self):
        if len(self.text) > 1:
            self.text = self.text[:-1]
        else:
            self.text = ""
        
        self.ui.lineEdit.setText(self.text)
    
    def talk_callback(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)

        label.setText("Dialling " + self.text)
        layout.addWidget(label)

        close_button = QPushButton('OK', self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CallUi()
    w.show()
    sys.exit(app.exec_())