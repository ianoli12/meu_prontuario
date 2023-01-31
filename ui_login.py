# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(552, 466)
        Login.setCursor(QCursor(Qt.PointingHandCursor))
        Login.setStyleSheet(u"background-color: rgb(142, 28, 255)")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 190, 421, 231))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0.2);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(100, 50, 211, 21))
        font = QFont()
        font.setPointSize(10)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
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
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(100, 100, 211, 21))
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 150, 161, 20))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 30, 111, 101))
        self.label_3.setPixmap(QPixmap(u"../projeto_prontuario(curso)/imagens/logo.png"))
        self.label_3.setScaledContents(True)
        QWidget.setTabOrder(self.txt_usuario, self.txt_password)
        QWidget.setTabOrder(self.txt_password, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"User", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Meu Prontu\u00e1rio", None))
        self.label_3.setText("")
    # retranslateUi

