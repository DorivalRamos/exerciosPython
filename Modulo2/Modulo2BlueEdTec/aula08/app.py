from flask import Blueprint, render_template, request, Flask, redirect
from werkzeug.exceptions import MethodNotAllowed
app = Flask(__name__)
itens = []


@app.route('/')
def index():
    nomeLista = "Lista de coisas para fazer"
    listaPronta = True
    return render_template('index.html', 
        nomeLista = nomeLista,
        listaPronta = listaPronta,
        itens=itens
        )

@app.route('/pagina2')
def pagina2():
    return '<h1> Rota dois, Verme Saiajin <h1>'

@app.route('/nova', methods=['POST'])
def nova():
    if request.method == 'POST' :
        item = request.form['item']
        itens.append(item)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

