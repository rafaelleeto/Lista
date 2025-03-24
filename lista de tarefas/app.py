from flask import Flask,render_template #Importando Biblioteca flask

app = Flask(__name__) # Criando um objeto flask chamado app

@app.route('/')
def hello():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True, port=5002)