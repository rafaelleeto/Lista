import sqlite3 # Importa bibliotecas necessárias!

def conectar_banco(): # Função que conecta o banco
    conexao=sqlite3.connect("banco_lista.db") 
    return conexao 

def criar_tabelas(): # Função que cria tabela de usuario e tarefas no SQL
    conexao = conectar_banco() 
    cursor = conexao.cursor() 
    
    # Cria tabela Usuario com parametros de email, nome e senha)
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    # Cria tabela de tarefas com parametros de id primario, email do usuario, conteudo da tarefa e status)
    cursor.execute('''create table if not exists tarefas
                   (id integer primary key,email_usuario text,conteudo text,status text, FOREIGN KEY (email_usuario) REFERENCES usuarios(email))''')
    conexao.commit() 
    
def criar_usuario(email, nome, senha): # Função que pega parametros enviados pelo usuario para fazer registro
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        # Insere os valores digitados no SQL (email,nome,senha)
        cursor.execute('insert into usuarios (email,nome,senha) VALUES (?,?,?) ',(email,nome,senha))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def criar_tarefas(email_usuario,conteudo,status): # Função que pega parametros inseridos pelo usuario para criar uma tabela
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # Insere valores dentro do SQL (email_usuario,conteudo,status)
        cursor.execute('''INSERT INTO tarefas(email_usuario,conteudo,status,) values (?, ?, ? )''',(email_usuario,conteudo,status))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()  
        
def logar_usuario(email,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
        
if __name__=="__main__":
    conectar_banco() 
    criar_tabelas()
    