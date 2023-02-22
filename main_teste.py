import sys
from PyQt5 import QtWidgets, uic
import sqlite3
from PySide6.QtWidgets import(QApplication,QMainWindow,QWidget,QLayout,QMessageBox)
from ui_login import Ui_Loginapp
from teste_interface import Ui_tela_principal
import sys
from database import DataBase

app = QApplication(sys.argv)

class Home(QMainWindow,Ui_tela_principal): # Herda os atributos de QWidget e Ui_Login
    
    def __init__(self,usuario):
        super(Home,self).__init__() # Inicia os elements da super-classe
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        ################### PAGINAS DO SISTEMA ###################
        self.btn_painel.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_painel))
        self.btn_agenda.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_agenda))
        self.btn_prontuarios.clicked.connect(lambda:self.Pages.setCurrentWidget(self.pg_prontuarios))

    def exibir_prontuarios(self,codigo_pront,nome,telefone,convenio):
        con = sqlite3.connect("system.db")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM PRONTUARIOS", (codigo_pront,nome,telefone,convenio)).fetchone()
        print()
    
    
class LoginWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        
        self.usuarios = DataBase()
        self.usuarios.conecta()

        # Carrega a interface criada no QT Designer
        uic.loadUi("login_1.ui", self)

        """db = DataBase()   
        self.codigo = DataBase()
        teste = db.exibir_prontuarios()
        print(teste)"""

        # Conecta o botão de login a uma função
        self.btn_login.clicked.connect(self.checar_usuario)
        
    def checar_usuario(self):

       # Conecta ao banco de dados SQLite
        con = sqlite3.connect("system.db")
        cur = con.cursor()
       
        # Obtém o usuário e a senha digitados pelo usuário
        usuario = self.txt_usuario_login.text()
        senha = self.txt_senha_login.text()
        
        # Verifica se o usuário e a senha correspondem a algum registro no banco de dados
        result = cur.execute("SELECT * FROM USUARIOS WHERE USUARIO=? AND SENHA=?", (usuario, senha)).fetchone()
        print(result)
        if result:
            # Usuário e senha válidos
            QtWidgets.QMessageBox.information(self, "Sucesso", "Você realizou o login com sucesso!")
            usuario = self.abrir_home(usuario)
            print("Deu certo")
            
        else:
            # Usuário e senha inválidos
            QtWidgets.QMessageBox.warning(self, "Falha", "Usuário ou senha incorretos!")

    def abrir_home(self,usuario):
        self.hide()
        self.home = Home(usuario)
        self.home.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


