# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'val_count.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(40, 70, 141, 171))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(240, 30, 120, 251))
        self.dec_button = QPushButton(self.widget)
        self.dec_button.setObjectName(u"dec_button")
        self.dec_button.setGeometry(QRect(20, 10, 81, 71))
        self.inc_button = QPushButton(self.widget)
        self.inc_button.setObjectName(u"inc_button")
        self.inc_button.setGeometry(QRect(20, 90, 81, 71))
        self.reset_button = QPushButton(self.widget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(20, 170, 81, 71))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_label.setText("")
        self.dec_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"reset", None))
    # retranslateUi

