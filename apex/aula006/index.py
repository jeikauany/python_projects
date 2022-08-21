from flask import Flask

app = Flask(_name_)

@app.route('/')
def inicio():
    return 'Olá'
@app.route('/pessoa')
def pessoas():
    return 'Olá, pessoas'

app.run(debug= True)







