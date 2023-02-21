from PySide6.QtWidgets import(QApplication,QMainWindow,QWidget,QLayout,QMessageBox)
#from PyQt5 import QtWidgets, QtGui
from ui_login import Ui_Loginapp
#from tela_principal import Ui_Form_principal
from teste_interface import Ui_tela_principal
import sys
from database import DataBase


class Login(QWidget, Ui_Loginapp): # A classe Login herda os atributos de QWidget e Ui_Login
    # Inicia a classe
    def __init__(self) -> None: # Inicia a classe
        super(Login, self).__init__() # Importa a classe
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.checar_login)

    def checar_login(self):
        self.usuarios = DataBase()
        self.usuarios.conecta()
        autenticado = self.usuarios.checar_usuario(self.txt_usuario_login.text().upper(),self.txt_senha_login.text())
        
        if self.txt_usuario_login == "ian" and self.txt_senha_login == "123":
            
        #if autenticado.lower() == "administrador" or autenticado.lower() == "usuario":
            self.w = Home(autenticado.lower())
            #self.w = Home(self.txt_usuario_login.text(),autenticado.lower())
            self.w.show()
            self.close()
        
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou Senha incorreto \n \n Tentativa: {self.tentativas + 1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                # bloquear usuario de acessar o sistema
                self.usuarios.close_connection()
                sys.exit(0)

class Home (QMainWindow,Ui_tela_principal,Login): # Herda os atributos de QWidget e Ui_Login
    def __init__(self,usuario):
        super(Home,self).__init__() # Inicia os elements da super-classe
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        ################### PAGINAS DO SISTEMA ###################
        self.btn_painel.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_painel))
        self.btn_agenda.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_agenda))
        self.btn_prontuarios.clicked.connect(lambda:self.Pages.setCurrentWidget(self.btn_prontuarios))

        self.btn_cadastrar_usu.clicked.connect(self.cadastrar_usuario)
        
    def cadastrar_usuario(self):
        if self.txt_senha_login.text() != self.txt_usu_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Senha divergentes")
            msg.setText("A senha nao é igual")
            msg.exec()
            return None

        nome = self.txt_usu_nome.text()
        telefone = self.txt_usu_tel.text()
        endereco = self.txt_usu_endereco()
        email = self.txt_usu_email()
        convenio = self.txt_usu_convenio()
        usuario = self.txt_usuario_login.text()
        senha = self.txt_senha_login.text()
        senha2 = self.txt_usu_senha_2.text()
        acesso = self.cb_acesso.currentText()

        """db = DataBase()
        db.conecta()
        db.inserir_usuario(nome,telefone,endereco,email,convenio,usuario,senha,senha2,acesso)
        db.close_connection()"""

        """msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro Realizado com sucesso")
        msg.exec()"""

        self.txt_usu_nome.setText("")
        #self.txt_usu_usuario.setText("")
        #self.txt_usu_senha.setText("")
        self.txt_usu_senha_2.setText("")
        self.txt_usuario_login.setText("")
        self.txt_senha_login.setText("")
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login() # Instancia a classe
    window.show()
    app.exec() # Executa a aplicação


