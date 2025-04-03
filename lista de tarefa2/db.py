import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("Bancodedados.db")
    return conexao

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''create table if not exists usuarios 
                   (email text primary key, name text, password text) ''')
    
    cursor.execute('''create table if not exists tarefas
                   (id interger primary key, email_usuario text, conteudo text,status text, FOREIGN KEY (email_usuario) REFERENCES usuarios(email))''')
    
    conexao.commit()
    conexao.close()


    
    
def criar_usuario(email,nome,senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (email,name,password) VALUES (?,?,?) ',(email,nome,senha))
    conexao.commit()
    conexao.close()

def localizar_usuario(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('select password from usuarios where email=? ',(email,))
    senha=cursor.fetchone()
    conexao.close()
    return senha

if __name__=="__main__":
    conectar_banco()
    criar_tabelas()