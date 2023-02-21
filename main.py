from PySide6.QtWidgets import(QApplication,QMainWindow,QWidget,QMessageBox,QVBoxLayout,QLineEdit)
from PyQt5 import QtWidgets, QtGui
from ui_login import Ui_Login
from tela_principal import Ui_Form
import sys
from database import DataBase
from teste_interface import Ui_tela_principal


class Login(QWidget,Ui_Login):
    # Inicia a classe
    def __init__(self) -> None:
        super(Login,self).__init__() # Importa a Classe
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.ChecarLogin)       

    def ChecarLogin(self):
        self.usuario = DataBase()
        self.usuario.conecta()
        autenticado = self.usuario.checar_usuario(self.txt_usuario.text().upper(),self.txt_password.text())

        if autenticado.lower() == "administrador" or autenticado.lower() == "usuario":
            self.w = Ui_tela_principal(autenticado.lower())
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou Senha incorreto \n\n Tentativa: {self.tentativas + 1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                self.usuario.close_connection()
                sys.exit(0)

        
class Principal(QMainWindow,Ui_tela_principal): # Herda os atributos de QWidget e Ui_Login
    def __init__(self,usuario):
        super(Principal,self).__init__() # Inicia os elements da super-classe
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        # se o usuario nao for administrador, o botão de cadastro some.
        if usuario.lower() == "usuario":
            self.btn_pg_cadastro.setVisible(False)

        ################### PAGINAS DO SISTEMA ###################
        self.btn_painel.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_painel))
        self.btn_agenda.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_agenda))
        self.btn_prontuarios.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_prontuarios))
        self.btn_sobre.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_sobre))
        #self.btn_outro.clicked.connect (lambda:self.Pages.setCurrentWidget(self.pg_outro))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cad_usu))

        #self.btn_cadastrar_usu.clicked.connect(self.cadastrar_usuario)

        #self.Pages.setCurrentWidget(self.btn_pg_cadastro)

    def cadastrar_usuario(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senha divergentes")
            msg.setText("A senha nao é igual")
            msg.exec()
            return None

        ################# CADASTRO DE USUARIO #################
        #codigo = self.txt_usu_codigo.text()
        nome = self.txt_usu_nome.text()
        telefone = self.txt_usu_tel.text()
        endereco = self.txt_usu_endereco.text()
        email = self.txt_usu_email.text()
        convenio = self.txt_usu_convenio.text()
        usuario = self.txt_usu_usuario.text()
        senha = self.txt_usu_senha.text()
        acesso = self.cb_acesso.currentText()

        db = DataBase()
        db.conecta()
        db.inserir_usuario(nome,telefone,endereco,email,convenio,usuario,senha,acesso)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro Realizado com sucesso")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login() # Instancia a classe
    window.show()
    app.exec() # Executa a aplicação

