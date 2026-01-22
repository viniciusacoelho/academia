from limpar_tela.limpar_tela import limpar_tela
from instrutores.crud_instrutores import autenticar_instrutor
from instrutores.painel_instrutor import painel_instrutor
from alunos.login_aluno import input_asterisco

def login():
    while True:
        limpar_tela()

        print("--------------------------------------------\n           Login\n--------------------------------------------")

        email = input("Digite seu e-mail: ")
        senha = input_asterisco("Digite sua senha: ")

        instrutor_autenticado = autenticar_instrutor(email, senha)

        painel_instrutor(instrutor_autenticado[0])