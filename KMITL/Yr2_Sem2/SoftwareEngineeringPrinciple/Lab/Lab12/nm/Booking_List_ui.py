# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Booking List.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_list(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.text = QTextEdit(Form)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(40, 20, 321, 191))
        self.select_btn = QPushButton(Form)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(70, 240, 261, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.select_btn.setText(QCoreApplication.translate("Form", u"Select Bookings...", None))
    # retranslateUi

