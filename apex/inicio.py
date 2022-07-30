import os
from flask import Flask, render_template, request, redirect
from funcionarios import getAll, salvarFuncionario

os.system('cls')
app = Flask(__name__)

@app.route('/')
def inicio():
    titulo = 'Olá, sejam bem_vindos!'
    return render_template('index.html', mensagem=titulo)

@app.route('/funcionario')
def func():
    funcionarios = getAll()
    return render_template('funcionario.html', funcionario=funcionarios)


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')


@app.route('/salvar', methods=['POST']) 
def salvar():
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    idade = request.form.get('idade')
    func1 = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade}
    salvarFuncionario(func1)
    return redirect('/funcionario')

app.run(debug=True, host='0.0.0.0')

