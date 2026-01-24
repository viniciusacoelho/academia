from limpar_tela.limpar_tela import limpar_tela
# from instrutores.criar_conta_instrutor import criar_conta
# from instrutores.login_instrutor import login
from instrutores.crud_instrutores import listar_instrutores
from instrutores.crud_instrutores import cadastrar_instrutor
from alunos.login_aluno import input_asterisco

from instrutores.crud_instrutores import autenticar_instrutor
from instrutores.painel_instrutor import painel_instrutor

def menu_instrutor():
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Menu Instrutor\n--------------------------------------------")

        menu = ["Criar Conta", "Login", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: criar_conta()
                case 2: login()
                case 3:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

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

def login():
    while True:
        limpar_tela()

        print("--------------------------------------------\n           Login\n--------------------------------------------")

        email = input("Digite seu e-mail: ")
        senha = input_asterisco("Digite sua senha: ")

        instrutor_autenticado = autenticar_instrutor(email, senha)

        if instrutor_autenticado:
            painel_instrutor(instrutor_autenticado[0])
        else:
            print("E-mail e/ou senha incorretos! Tente novamente.")