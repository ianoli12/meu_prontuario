# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_tela_principal(object):
    def setupUi(self, tela_principal):
        if not tela_principal.objectName():
            tela_principal.setObjectName(u"tela_principal")
        tela_principal.resize(901, 759)
        self.frame = QFrame(tela_principal)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 54, 879, 60))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_painel = QPushButton(self.frame)
        self.btn_painel.setObjectName(u"btn_painel")
        self.btn_painel.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Bahnschrift Light SemiCondensed"])
        self.btn_painel.setFont(font)
        self.btn_painel.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_painel)

        self.btn_agenda = QPushButton(self.frame)
        self.btn_agenda.setObjectName(u"btn_agenda")
        self.btn_agenda.setFont(font)
        self.btn_agenda.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_agenda)

        self.btn_prontuarios = QPushButton(self.frame)
        self.btn_prontuarios.setObjectName(u"btn_prontuarios")
        self.btn_prontuarios.setFont(font)
        self.btn_prontuarios.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_prontuarios)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setFont(font)
        self.btn_sobre.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_sobre)

        self.btn_sobre.raise_()
        self.btn_prontuarios.raise_()
        self.btn_agenda.raise_()
        self.btn_painel.raise_()
        self.label = QLabel(tela_principal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 14, 879, 34))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font1.setPointSize(21)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.label.setScaledContents(True)
        self.btn_pg_cadastro = QPushButton(tela_principal)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setGeometry(QRect(10, 728, 879, 23))
        self.Pages = QStackedWidget(tela_principal)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setEnabled(True)
        self.Pages.setGeometry(QRect(10, 120, 879, 602))
        self.pg_painel = QWidget()
        self.pg_painel.setObjectName(u"pg_painel")
        self.pg_painel.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.pg_painel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.pg_painel)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_14)

        self.frame_2 = QFrame(self.pg_painel)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.pg_painel)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_pac_total = QLabel(self.frame_3)
        self.lb_pac_total.setObjectName(u"lb_pac_total")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font4.setPointSize(31)
        self.lb_pac_total.setFont(font4)
        self.lb_pac_total.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_pac_total)

        self.lb_pac_confirmados = QLabel(self.frame_3)
        self.lb_pac_confirmados.setObjectName(u"lb_pac_confirmados")
        self.lb_pac_confirmados.setFont(font4)
        self.lb_pac_confirmados.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_pac_confirmados)

        self.lb_pac_atendidos = QLabel(self.frame_3)
        self.lb_pac_atendidos.setObjectName(u"lb_pac_atendidos")
        self.lb_pac_atendidos.setEnabled(True)
        self.lb_pac_atendidos.setFont(font4)
        self.lb_pac_atendidos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_pac_atendidos)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_painel)
        self.pg_agenda = QWidget()
        self.pg_agenda.setObjectName(u"pg_agenda")
        self.Pages.addWidget(self.pg_agenda)
        self.pg_prontuarios = QWidget()
        self.pg_prontuarios.setObjectName(u"pg_prontuarios")
        self.pg_prontuarios.setEnabled(True)
        self.verticalLayout_5 = QVBoxLayout(self.pg_prontuarios)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_20 = QLabel(self.pg_prontuarios)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_20)

        self.frame_8 = QFrame(self.pg_prontuarios)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setEnabled(True)
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_19)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.pg_prontuarios)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setEnabled(True)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget = QTableWidget(self.frame_9)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_9.addWidget(self.tableWidget)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setCheckable(False)

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_9.addWidget(self.frame_10)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.Pages.addWidget(self.pg_prontuarios)
        self.pg_cad_usu = QWidget()
        self.pg_cad_usu.setObjectName(u"pg_cad_usu")
        self.verticalLayout_13 = QVBoxLayout(self.pg_cad_usu)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_25 = QLabel(self.pg_cad_usu)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setMinimumSize(QSize(0, 0))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_25)

        self.frame_18 = QFrame(self.pg_cad_usu)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.frame_18)
        self.label_26.setObjectName(u"label_26")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy4)
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_26)


        self.verticalLayout_13.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.pg_cad_usu)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_3 = QLabel(self.frame_20)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_3)

        self.txt_usu_codigo = QLineEdit(self.frame_20)
        self.txt_usu_codigo.setObjectName(u"txt_usu_codigo")

        self.verticalLayout_14.addWidget(self.txt_usu_codigo)

        self.label_30 = QLabel(self.frame_20)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_30)

        self.txt_usu_nome = QLineEdit(self.frame_20)
        self.txt_usu_nome.setObjectName(u"txt_usu_nome")

        self.verticalLayout_14.addWidget(self.txt_usu_nome)

        self.label_28 = QLabel(self.frame_20)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_28)

        self.txt_usu_tel = QLineEdit(self.frame_20)
        self.txt_usu_tel.setObjectName(u"txt_usu_tel")

        self.verticalLayout_14.addWidget(self.txt_usu_tel)

        self.label_29 = QLabel(self.frame_20)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_29)

        self.txt_usu_endereco = QLineEdit(self.frame_20)
        self.txt_usu_endereco.setObjectName(u"txt_usu_endereco")

        self.verticalLayout_14.addWidget(self.txt_usu_endereco)

        self.label_2 = QLabel(self.frame_20)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_2)

        self.txt_usu_email = QLineEdit(self.frame_20)
        self.txt_usu_email.setObjectName(u"txt_usu_email")

        self.verticalLayout_14.addWidget(self.txt_usu_email)

        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_27)

        self.txt_usu_convenio = QLineEdit(self.frame_20)
        self.txt_usu_convenio.setObjectName(u"txt_usu_convenio")

        self.verticalLayout_14.addWidget(self.txt_usu_convenio)

        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_18)

        self.txt_usu_usuario = QLineEdit(self.frame_20)
        self.txt_usu_usuario.setObjectName(u"txt_usu_usuario")

        self.verticalLayout_14.addWidget(self.txt_usu_usuario)

        self.label_4 = QLabel(self.frame_20)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_4)

        self.txt_usu_senha = QLineEdit(self.frame_20)
        self.txt_usu_senha.setObjectName(u"txt_usu_senha")

        self.verticalLayout_14.addWidget(self.txt_usu_senha)

        self.label_8 = QLabel(self.frame_20)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_14.addWidget(self.label_8)

        self.txt_usu_senha_2 = QLineEdit(self.frame_20)
        self.txt_usu_senha_2.setObjectName(u"txt_usu_senha_2")

        self.verticalLayout_14.addWidget(self.txt_usu_senha_2)

        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_17)

        self.cb_acesso = QComboBox(self.frame_20)
        self.cb_acesso.addItem("")
        self.cb_acesso.addItem("")
        self.cb_acesso.setObjectName(u"cb_acesso")

        self.verticalLayout_14.addWidget(self.cb_acesso)

        self.btn_cadastrar_usu = QPushButton(self.frame_20)
        self.btn_cadastrar_usu.setObjectName(u"btn_cadastrar_usu")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_cadastrar_usu.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_usu.setSizePolicy(sizePolicy5)

        self.verticalLayout_14.addWidget(self.btn_cadastrar_usu)


        self.verticalLayout_13.addWidget(self.frame_20)

        self.Pages.addWidget(self.pg_cad_usu)
        self.frame_4 = QFrame(tela_principal)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setGeometry(QRect(0, 0, 901, 761))
        self.frame_4.setStyleSheet(u"background-color: rgb(170, 0, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.btn_pg_cadastro.raise_()
        self.Pages.raise_()

        self.retranslateUi(tela_principal)

        self.Pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(tela_principal)
    # setupUi

    def retranslateUi(self, tela_principal):
        tela_principal.setWindowTitle(QCoreApplication.translate("tela_principal", u"Form", None))
        self.btn_painel.setText(QCoreApplication.translate("tela_principal", u"PAINEL", None))
        self.btn_agenda.setText(QCoreApplication.translate("tela_principal", u"AGENDA", None))
        self.btn_prontuarios.setText(QCoreApplication.translate("tela_principal", u"PRONTU\u00c1RIOS", None))
        self.btn_sobre.setText(QCoreApplication.translate("tela_principal", u"SOBRE", None))
        self.label.setText(QCoreApplication.translate("tela_principal", u"Meu Prontu\u00e1rio", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("tela_principal", u"CADASTRAR USUARIO", None))
        self.label_14.setText(QCoreApplication.translate("tela_principal", u"PAINEL", None))
        self.label_6.setText(QCoreApplication.translate("tela_principal", u"Total de Pacientes:", None))
        self.label_7.setText(QCoreApplication.translate("tela_principal", u"Pacientes Confirmados:", None))
        self.label_5.setText(QCoreApplication.translate("tela_principal", u"Pacientes Atendidos:", None))
        self.lb_pac_total.setText(QCoreApplication.translate("tela_principal", u"TextLabel", None))
        self.lb_pac_confirmados.setText(QCoreApplication.translate("tela_principal", u"TextLabel", None))
        self.lb_pac_atendidos.setText(QCoreApplication.translate("tela_principal", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("tela_principal", u"PRONTU\u00c1RIOS", None))
        self.label_19.setText(QCoreApplication.translate("tela_principal", u"Rela\u00e7\u00e3o de Prontu\u00e1rios", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("tela_principal", u"CODIGO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("tela_principal", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("tela_principal", u"TELEFONE", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("tela_principal", u"CONVENIO", None));
        self.pushButton_3.setText(QCoreApplication.translate("tela_principal", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("tela_principal", u"Adicionar Paciente", None))
        self.pushButton_2.setText(QCoreApplication.translate("tela_principal", u"Excluir", None))
        self.label_25.setText(QCoreApplication.translate("tela_principal", u"CADASTRO", None))
        self.label_26.setText(QCoreApplication.translate("tela_principal", u"Cadastro de Usu\u00e1rios:", None))
        self.label_3.setText(QCoreApplication.translate("tela_principal", u"C\u00f3digo:", None))
        self.label_30.setText(QCoreApplication.translate("tela_principal", u"Nome:", None))
        self.label_28.setText(QCoreApplication.translate("tela_principal", u"Telefone:", None))
        self.label_29.setText(QCoreApplication.translate("tela_principal", u"Endere\u00e7o:", None))
        self.label_2.setText(QCoreApplication.translate("tela_principal", u"E-mail:", None))
        self.label_27.setText(QCoreApplication.translate("tela_principal", u"Conv\u00eanio:", None))
        self.label_18.setText(QCoreApplication.translate("tela_principal", u"Usu\u00e1rio:", None))
        self.label_4.setText(QCoreApplication.translate("tela_principal", u"Senha:", None))
        self.label_8.setText(QCoreApplication.translate("tela_principal", u"Confirmar Senha:", None))
        self.label_17.setText(QCoreApplication.translate("tela_principal", u"Acesso", None))
        self.cb_acesso.setItemText(0, QCoreApplication.translate("tela_principal", u"USUARIO", None))
        self.cb_acesso.setItemText(1, QCoreApplication.translate("tela_principal", u"ADMINISTRADOR", None))

        self.btn_cadastrar_usu.setText(QCoreApplication.translate("tela_principal", u"Cadastrar", None))
    # retranslateUi

