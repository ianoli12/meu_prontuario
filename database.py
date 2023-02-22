import sqlite3
from ui_login import Ui_Loginapp

class DataBase():
    # Se eu não passar argumento nenhum, nosso banco vai ser criado como system.db
    def __init__(self,nome = "system.db") -> None:
        self.nome = nome
        
    
    # Conecta ao bd
    def conecta(self):
        self.connection = sqlite3.connect(self.nome)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def criar_tabela_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS USUARIOS(
                    COD_USU INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    NOME VARCHAR(100) NOT NULL,
                    TELEFONE VARCHAR(15) NOT NULL,
                    ENDERECO VARCHAR(100) NOT NULL,
                    EMAIL VARCHAR(15),
                    CONVENIO VARCHAR(30),
                    USUARIO VARCHAR(20) NOT NULL,
                    SENHA VARCHAR(20) NOT NULL,
                    SENHA2 VARCHAR(20) NOT NULL,
                    ACESSO VARCHAR(20) NOT NULL
                );

            """)
        except AttributeError:
            print("Faça conexão com o banco")

    def criar_tabela_prontuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS PRONTUARIOS(
                    COD_PRONTUARIO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    NOME VARCHAR(100) NOT NULL,
                    TELEFONE VARCHAR(15) NOT NULL,
                    CONVENIO VARCHAR(30)
                );

            """)
        except AttributeError:
            print("Não foi possível criar a tabela PRONTUARIOS")
    

    def inserir_usuario(self,nome,telefone,endereco,email,convenio,usuario,senha,senha2,acesso):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO USUARIOS(NOME,TELEFONE,ENDERECO,EMAIL,CONVENIO,USUARIO,SENHA,SENHA2,ACESSO) VALUES (?,?,?,?,?,?,?,?)

        """,
        (nome,telefone,endereco,email,convenio,usuario,senha,senha2,acesso))
        self.connection.commit()

    def checar_usuario(self,result):
        
        con = sqlite3.connect("system.db")
        cur = con.cursor()
        
        #try:
            #cursor = self.connection.cursor()
            #cursor.execute("""
                #SELECT * FROM USUARIOS;
            #""")

            #for linha in cursor.fetchall():
                #if linha[6].upper() == usuario.upper() and linha [7] == senha and linha[8] == "ADMINISTRADOR":
                    #return "ADMINISTRADOR"
                #elif linha[6].upper() == usuario.upper() and linha[7] == senha and linha[8] == "USUARIO":
                    #return "USUARIO"
                #else:
                    #continue
            #return "usuario"
        #except:
            #pass


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.criar_tabela_usuarios()
    db.criar_tabela_prontuarios()
    db.close_connection()