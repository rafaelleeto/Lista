from flask import Flask,render_template,request,redirect #Importando Biblioteca flask
import db
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__) # Criando um objeto flask chamado app

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro ():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    usuario = request.form['usuario']
    email = request.form['email']
    senha = generate_password_hash(request.form['senha'])
    

    if db.criar_usuario(email, usuario, senha):
        return "Usuário criado com sucesso"
    else:
        return "Cadastro não funcionou!"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def logar():
    email = request.form['email']
    usuario=db.localizar_usuario(email)
    
    if usuario is None:
        return "Usuario não existe"
    
    senha = request.form['senha']
    
    if senha is None:
        return "Senha não existe"
    
    if check_password_hash(senha)!=usuario[0]:
        return "Senha errada"
    
    return redirect('/lista')

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/criar_tarefa',methods=['POST'])
def criar_tarefa():
    
    email="leetobr@gmail.com.br"
    tarefa = request.form['tarefa']
    db.criar_tarefas(email,tarefa,0)
    return redirect('/lista')
    
    

    
        
        
    

    


    


if __name__=='__main__':
    app.run(debug=True, port=5002)