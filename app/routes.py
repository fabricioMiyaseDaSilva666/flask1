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
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")
        dados = {"cpf":cpf, "nome":nome, "telefone":telefone, "endereco":endereco}
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
            if chave == '2435':
                idCadastro = codigo
                return idCadastro
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"Amy Lee"}
        requisicao = requests.patch(f'{link}/cadastro/-O8mjUyCEn87oSLEKDAH/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Aldo deu errado \n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastro/-O8mjUyCEn87oSLEKDAH/.json')
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n {e}'