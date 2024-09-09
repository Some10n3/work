# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Selecting Booking.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_select(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.day = QLineEdit(Form)
        self.day.setObjectName(u"day")
        self.day.setGeometry(QRect(80, 60, 271, 22))
        self.month = QLineEdit(Form)
        self.month.setObjectName(u"month")
        self.month.setGeometry(QRect(80, 120, 271, 22))
        self.year = QLineEdit(Form)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(80, 170, 271, 22))
        self.submit_btn = QPushButton(Form)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(72, 240, 261, 28))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 55, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 55, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 180, 55, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.submit_btn.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.label.setText(QCoreApplication.translate("Form", u"Day", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Month", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Year", None))
    # retranslateUi

