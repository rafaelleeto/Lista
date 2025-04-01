from flask import Flask,render_template,request,redirect,session #Importando Biblioteca flask
import db
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__) # Criando um objeto flask chamado app
app.secret_key='rafael'

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
        return redirect('/login')
    else:
        return "Cadastro não funcionou!"

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login',methods=['POST'])
def logar():
    email = request.form['email']
    usuario=db.localizar_usuario(email)
    print(usuario)
    
    if usuario is None:
        return "Usuario não existe"
    
    senha = request.form['senha']
    
    if senha is None:
        return "Senha não existe"
    
    if not check_password_hash(usuario[0],senha):
        return "Senha errada"
    
    session['email'] = email


    return redirect('/lista')

@app.route('/lista')
def lista():
    tarefas=db.pegar_tarefas(session['email'])

    return render_template('lista.html',tarefas=tarefas)

@app.route('/criar_tarefa',methods=['POST'])
def criar_tarefa():
    
    email=session['email']
    tarefa = request.form['tarefa']
    db.criar_tarefas(email,tarefa,0)
    return redirect('/lista')

@app.route('/marcar_tarefa/<id>')
def marcar_tarefa(id):
    if verificar_email(id):
        return "não pode"
    db.marcar_tarefa(id)
    return redirect('/lista')

@app.route('/excluir_tarefa/<id>')
def excluir_tarefa(id):
    if verificar_email(id):
        return "não pode"
    db.excluir_tarefa(id)
    return redirect('/lista')

@app.route('/editar_tarefa/<id>')
def editar_tarefa(id):
    
    tarefa=db.pegar_tarefa(id)
    
    if verificar_email(id):
        return "não pode"
    
    return render_template('editar_tarefa.html',id=id,tarefa=tarefa)
   

@app.route('/editar_tarefa/<id>',methods=['POST'])
def editar_tarefa2(id):
    if verificar_email(id):
        return "não pode"
    
    tarefa=request.form['tarefa']
    
    
    db.editar_tarefa(id,tarefa)
    
    return redirect('/lista')

def verificar_email(id):
    tarefa=db.pegar_tarefa(id)
    
    if session['email'] != tarefa[1]:
        return True
    else:
        return False
    
    
    
    

    
        
        
    

    


    


if __name__=='__main__':
    app.run(debug=True, port=5000)