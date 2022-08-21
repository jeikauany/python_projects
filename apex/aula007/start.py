from flask import Flask

app = Flask('__name__')
@app.route('/')
def inicio():
    return 'Sistemas de cadastro de pessoas'

@app.route('/Listar')
def Listar():
    return 'Listar de pessoas cadastradas'

app.run(debug=True)