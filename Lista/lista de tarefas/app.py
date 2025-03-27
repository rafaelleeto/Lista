from flask import Flask,render_template,request,redirect #Importando Biblioteca flask
import db

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
    senha = request.form['senha']

    if db.criar_usuario(email, usuario, senha):
        return "Usuário criado com sucesso"
    else:
        return "Cadastro não funcionou!"

@app.route('/login')
def login():
    return render_template('login.html')


    


if __name__=='__main__':
    app.run(debug=True, port=5002)