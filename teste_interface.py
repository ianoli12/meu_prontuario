# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_tela_principal(object):
    def setupUi(self, tela_principal):
        if not tela_principal.objectName():
            tela_principal.setObjectName(u"tela_principal")
        tela_principal.resize(562, 491)
        self.pushButton = QPushButton(tela_principal)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 220, 75, 23))

        self.retranslateUi(tela_principal)

        QMetaObject.connectSlotsByName(tela_principal)
    # setupUi

    def retranslateUi(self, tela_principal):
        tela_principal.setWindowTitle(QCoreApplication.translate("tela_principal", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("tela_principal", u"PushButton", None))
    # retranslateUi

