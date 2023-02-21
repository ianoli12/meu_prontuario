# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_form_principal(object):
    def setupUi(self, form_principal):
        if not form_principal.objectName():
            form_principal.setObjectName(u"form_principal")
        form_principal.resize(945, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_principal.sizePolicy().hasHeightForWidth())
        form_principal.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(form_principal)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(form_principal)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(form_principal)

        QMetaObject.connectSlotsByName(form_principal)
    # setupUi

    def retranslateUi(self, form_principal):
        form_principal.setWindowTitle(QCoreApplication.translate("form_principal", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("form_principal", u"PushButton", None))
    # retranslateUi

