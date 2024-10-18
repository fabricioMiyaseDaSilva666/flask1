from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintfabricio-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="Página Inicial")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastrar")

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        email = request.form.get("email")
        endereco = request.form.get("endereco")
        dados = {"cpf":cpf, "nome":nome, "email":email, "endereco":endereco}
        requisicao = requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json') #solicito dados
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Aldo deu errado \n {e}'

@app.route('/listarIndividual')
def listasIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = "" #Colocar o id
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '12345':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n {e}'




@app.route('/excluir')
def excluir():
    return render_template('excluir.html')

@app.route('/excluirConta', methods=["POST"])
def excluirConta():
    try:
        cpf = request.form.get("cpf")
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:
                idCadastro = codigo
                idCadastro = requests.delete(f'{link}/cadastro/.json')
                return render_template('excluirConta.html')
        return "CPF não encontrado!"
    except Exception as e:
        return f'Algo deu errado \n {e}'

