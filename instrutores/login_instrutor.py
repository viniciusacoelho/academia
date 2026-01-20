from limpar_tela.limpar_tela import limpar_tela
from instrutores.crud_instrutores import autenticar_instrutor
from instrutores.painel_instrutor import painel_instrutor

def login():
    limpar_tela()

    print("--------------------------------------------\n           Login\n--------------------------------------------")

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    instrutor_autenticado = autenticar_instrutor(email, senha)

    painel_instrutor(instrutor_autenticado[0])