# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Loginapp(object):
    def setupUi(self, Loginapp):
        if not Loginapp.objectName():
            Loginapp.setObjectName(u"Loginapp")
        Loginapp.resize(552, 466)
        Loginapp.setCursor(QCursor(Qt.PointingHandCursor))
        Loginapp.setStyleSheet(u"background-color: rgb(142, 28, 255)")
        self.frame = QFrame(Loginapp)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 190, 421, 231))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0.2);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usuario_login = QLineEdit(self.frame)
        self.txt_usuario_login.setObjectName(u"txt_usuario_login")
        self.txt_usuario_login.setGeometry(QRect(100, 50, 211, 21))
        font = QFont()
        font.setPointSize(10)
        self.txt_usuario_login.setFont(font)
        self.txt_usuario_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_usuario_login.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(140, 140, 131, 41))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.txt_senha_login = QLineEdit(self.frame)
        self.txt_senha_login.setObjectName(u"txt_senha_login")
        self.txt_senha_login.setGeometry(QRect(100, 100, 211, 21))
        self.txt_senha_login.setFont(font)
        self.txt_senha_login.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_senha_login.setEchoMode(QLineEdit.Password)
        self.txt_senha_login.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Loginapp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 150, 161, 20))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Loginapp)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 30, 111, 101))
        self.label_3.setPixmap(QPixmap(u"../projeto_prontuario(curso)/imagens/logo.png"))
        self.label_3.setScaledContents(True)
        QWidget.setTabOrder(self.txt_usuario_login, self.txt_senha_login)
        QWidget.setTabOrder(self.txt_senha_login, self.btn_login)

        self.retranslateUi(Loginapp)

        QMetaObject.connectSlotsByName(Loginapp)
    # setupUi

    def retranslateUi(self, Loginapp):
        Loginapp.setWindowTitle(QCoreApplication.translate("Loginapp", u"Form", None))
        self.txt_usuario_login.setPlaceholderText(QCoreApplication.translate("Loginapp", u"User", None))
        self.btn_login.setText(QCoreApplication.translate("Loginapp", u"Login", None))
        self.txt_senha_login.setPlaceholderText(QCoreApplication.translate("Loginapp", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("Loginapp", u"Meu Prontu\u00e1rio", None))
        self.label_3.setText("")
    # retranslateUi

