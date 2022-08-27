# importando as bibliotecas
from flask import Flask, render_template, request, make_response, redirect
from utils.utils import fazer_login, registrar


# iniciando o flask
app = Flask(__name__)


# rota principal
@app.route("/")
def hello_world():
    # por padrão ele pega direto da pasta
    return render_template('index.html')


# devolvendo apenas o template de login
@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')


# criando a rota de login
@app.route('/login', methods=["POST"])
def logar():
    # pega a requisição do formulário
    req = request.form
   
    # verifica se foi encaminhado login e senha
    if "login" not in req or "senha" not in req:
        return ":(", 422
   
    # pega as oque veio de requisição
    user = req["login"]
    password = req["senha"]
   
    # chama a função para fazer login
    logar = fazer_login(user, password)
    if (logar is None):
   
        # retornando a resposta
        return render_template('login.html', error = "Usuário e senha inválidos")
   
    # montando a resposta
    resposta = make_response(redirect("/produtos"))
    resposta.set_cookie("login", user, samesite = "Strict")
    resposta.set_cookie("senha", password, samesite = "Strict")
   
    # devolvendo a resposta
    return resposta


@app.route('/registrar', methods=["GET"])
def cadastro():
    return render_template("registrar.html")


# criando a parte de cadastro
@app.route('/registrar', methods=["POST"])
def cadastrar():
    req = request.form
    # pegando a requisição do formulário
    # observação: Os campos login e senha vem do html
    user = req["login"]
    password = req["senha"]

    # registra
    registrar(user, password)
    
    # monta a resposta
    resposta = make_response(redirect("/login"))
    resposta.set_cookie("login", user, samesite = "Strict")
    resposta.set_cookie("senha", password, samesite = "Strict")
    # devolvendo a resposta
    return resposta


# produtos
@app.route('/produtos', methods=["GET"])
def produtos():
    return 'Produtos'


# iniciando a aplicação
if __name__ == "__main__":
    app.run(debug=True)





