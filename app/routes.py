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




@app.route('/excluirConta', methods=["POST"])
def excluirConta():
    try:
        cpf = request.form.get("cpf")
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:
                idCadastro = requests.delete(f'{link}/cadastro/{codigo}/.json')
                return "EXCLUIDO COM SUCESS"
        return "CPF não encontrado!"
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('/individual', methods=["POST"])
def individual():
    try:
        cpf = request.form.get("cpf")
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:
                cpf1 = cpf
                nome = dicionario[codigo]['nome']
                email = dicionario[codigo]['email']
                endereco = dicionario[codigo]['endereco']
                idCadastro = requests.get(f'{link}/cadastro/{codigo}/.json')
                return f'CPF: {cpf1} \n\n   Nome: {nome} \n\n   Email: {email} \n\n   Endereço: {endereco}'
        return "CPF não encontrado!"
    except Exception as e:
        return f'Algo deu errado \n {e}'

@app.route('atualizar')
def atualizar():
    return render_template('atualizar.html', titulo="Atualizar")

@app.route('cadastraAtualizar', methods=['POST'])
def cadastraAtualizar():
    try:
        nome = request.form.get("nome")
        email = request.form.get("email")
        endereco = request.form.get("endereco")

        req = request.get(f'{link}/cadastro/.json')
        dicionario = req.json()
        for codigo in dicionario:
            dados = {"nome":nome,"email":email,"endereco":endereco}
            requisicao = request.patch(f'{link}/cadastro/{codigo}/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'Algo deu errado \n {e}'