# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 189)
        Form.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.digit_entry = QLineEdit(Form)
        self.digit_entry.setObjectName(u"digit_entry")

        self.verticalLayout.addWidget(self.digit_entry)

        self.generate_btn = QPushButton(Form)
        self.generate_btn.setObjectName(u"generate_btn")

        self.verticalLayout.addWidget(self.generate_btn)

        self.seed_label = QLabel(Form)
        self.seed_label.setObjectName(u"seed_label")

        self.verticalLayout.addWidget(self.seed_label)

        self.seed_entry = QLineEdit(Form)
        self.seed_entry.setObjectName(u"seed_entry")

        self.verticalLayout.addWidget(self.seed_entry)

        self.seed_btn = QPushButton(Form)
        self.seed_btn.setObjectName(u"seed_btn")

        self.verticalLayout.addWidget(self.seed_btn)

        self.reset_btn = QPushButton(Form)
        self.reset_btn.setObjectName(u"reset_btn")

        self.verticalLayout.addWidget(self.reset_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Number of random digits:", None))
        self.generate_btn.setText(QCoreApplication.translate("Form", u"Generate Random Number", None))
        self.seed_label.setText(QCoreApplication.translate("Form", u"Seed:", None))
        self.seed_btn.setText(QCoreApplication.translate("Form", u"Set Seed", None))
        self.reset_btn.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

