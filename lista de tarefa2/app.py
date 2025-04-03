from flask import Flask,render_template,request,redirect,flash,session
import db

app = Flask(__name__)
app.secret_key="rafael"

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method=='GET':
        return render_template('cadastro.html')
    email=request.form['email']
    nome=request.form['name']
    senha=request.form['password']
    
    db.criar_usuario(email,nome,senha)
    flash('usuario criado com sucesso')
    return redirect ('/login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    
    senha=request.form['password']
    
    if senha==db.localizar_usuario(request.form['email'])[0]:
        session['email']=request.form['email']
        return redirect('/lista')
    flash('Tente novamente')
    
    return redirect('/login')
        
        
        

    






if __name__=='__main__':
    app.run(debug=True, port=5000)