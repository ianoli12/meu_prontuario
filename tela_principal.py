# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(923, 755)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: rgb(111, 8, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 60))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_painel = QPushButton(self.frame)
        self.btn_painel.setObjectName(u"btn_painel")
        self.btn_painel.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light SemiCondensed"])
        self.btn_painel.setFont(font1)
        self.btn_painel.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_painel)

        self.btn_agenda = QPushButton(self.frame)
        self.btn_agenda.setObjectName(u"btn_agenda")
        self.btn_agenda.setFont(font1)
        self.btn_agenda.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_agenda)

        self.btn_prontuarios = QPushButton(self.frame)
        self.btn_prontuarios.setObjectName(u"btn_prontuarios")
        self.btn_prontuarios.setFont(font1)
        self.btn_prontuarios.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_prontuarios)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setStyleSheet(u"background-color: rgb(191, 166, 255);")

        self.horizontalLayout_2.addWidget(self.btn_sobre)

        self.btn_sobre.raise_()
        self.btn_prontuarios.raise_()
        self.btn_agenda.raise_()
        self.btn_painel.raise_()

        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(Form)
        self.Pages.setObjectName(u"Pages")
        self.pg_painel = QWidget()
        self.pg_painel.setObjectName(u"pg_painel")
        self.verticalLayout_2 = QVBoxLayout(self.pg_painel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.pg_painel)
        self.label_14.setObjectName(u"label_14")
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
        self.verticalLayout_5 = QVBoxLayout(self.pg_prontuarios)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_20 = QLabel(self.pg_prontuarios)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_20)

        self.frame_8 = QFrame(self.pg_prontuarios)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_19)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.pg_prontuarios)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.treeWidget = QTreeWidget(self.frame_9)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout_9.addWidget(self.treeWidget)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setStyleSheet(u"background-color: rgb(191, 166, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
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
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
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

        self.verticalLayout.addWidget(self.Pages)

        self.btn_pg_cadastro = QPushButton(Form)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")

        self.verticalLayout.addWidget(self.btn_pg_cadastro)


        self.retranslateUi(Form)

        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Meu Prontu\u00e1rio", None))
        self.btn_painel.setText(QCoreApplication.translate("Form", u"PAINEL", None))
        self.btn_agenda.setText(QCoreApplication.translate("Form", u"AGENDA", None))
        self.btn_prontuarios.setText(QCoreApplication.translate("Form", u"PRONTU\u00c1RIOS", None))
        self.btn_sobre.setText(QCoreApplication.translate("Form", u"SOBRE", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"PAINEL", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Total de Pacientes:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Pacientes Confirmados:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Pacientes Atendidos:", None))
        self.lb_pac_total.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lb_pac_confirmados.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lb_pac_atendidos.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"PRONTU\u00c1RIOS", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Rela\u00e7\u00e3o de Prontu\u00e1rios", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"CONV\u00caNIO", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"TELEFONE", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"NOME", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"C\u00d3DIGO", None));
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Adicionar Paciente", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Excluir", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"CADASTRO", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Cadastro de Usu\u00e1rios:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"C\u00f3digo:", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Nome:", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Telefone:", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Endere\u00e7o:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"E-mail:", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Conv\u00eanio:", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Usu\u00e1rio:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Senha:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Acesso", None))
        self.cb_acesso.setItemText(0, QCoreApplication.translate("Form", u"USUARIO", None))
        self.cb_acesso.setItemText(1, QCoreApplication.translate("Form", u"ADMINISTRADOR", None))

        self.btn_cadastrar_usu.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("Form", u"CADASTRAR USUARIO", None))
    # retranslateUi

