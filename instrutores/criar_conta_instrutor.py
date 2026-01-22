from limpar_tela.limpar_tela import limpar_tela
from instrutores.crud_instrutores import cadastrar_instrutor
from alunos.login_aluno import input_asterisco

def criar_conta():
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Criar Conta\n--------------------------------------------")

        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        # cpf = int(input("Digite seu CPF: "))
        cpf = input("Digite seu CPF: ")
        senha = input_asterisco("Digite sua senha: ")

        cadastrar_instrutor(nome, email, cpf, senha)