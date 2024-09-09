# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")
        font = QFont()
        font.setPointSize(72)
        self.num_label.setFont(font)

        self.horizontalLayout.addWidget(self.num_label)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inc_button = QPushButton(self.widget)
        self.inc_button.setObjectName(u"inc_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inc_button.sizePolicy().hasHeightForWidth())
        self.inc_button.setSizePolicy(sizePolicy)
        self.inc_button.setFont(font)

        self.verticalLayout.addWidget(self.inc_button)

        self.dec_button = QPushButton(self.widget)
        self.dec_button.setObjectName(u"dec_button")
        sizePolicy.setHeightForWidth(self.dec_button.sizePolicy().hasHeightForWidth())
        self.dec_button.setSizePolicy(sizePolicy)
        self.dec_button.setFont(font)

        self.verticalLayout.addWidget(self.dec_button)

        self.reset_button = QPushButton(self.widget)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        self.reset_button.setFont(font1)

        self.verticalLayout.addWidget(self.reset_button)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">0</p></body></html>", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.dec_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

