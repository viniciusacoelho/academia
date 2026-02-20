from util.limpar_tela_util import limpar_tela
from repository.instrutores_repository import cadastrar_instrutor
from util.input_asterisco_util import input_asterisco
from repository.instrutores_repository import autenticar_instrutor
from view.instrutores_view.painel_instrutor import painel_instrutor
from util.validacoes_util import validar_nome, validar_email, validar_senha
from service.banco_de_dados_service import validar_unique
from service.instrutores_service import validar_cpf, formatar_cpf

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
                case 1: criar_conta_instrutor()
                case 2: login_instrutor()
                case 3:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def criar_conta_instrutor():
    limpar_tela()

    print("\n--------------------------------------------\n            Criar Conta\n--------------------------------------------")

    while True:
        nome = input("Digite seu nome: ")
        nome_valido = validar_nome(nome)

        if nome_valido:
            break
        else:
            print("Nome inválido. Tente novamente.")

    while True:
        email = input("Digite seu e-mail: ")
        email_valido = validar_email(email)

        if email_valido:
            continue
        else:
            print("E-mail inválido. Tente novamente.")

        email_unico = validar_unique(email, "instrutores", 2)

        if email_unico:
            break
        else:
            print("E-mail já cadastrado anteriormente! Tente outro e-mail.")

    while True:
        cpf = input("Digite seu CPF: ")

        try:
            int(cpf)
            cpf_valido = validar_cpf(cpf)

            if cpf_valido:
                cpf = formatar_cpf(cpf)
                break
            else:
                print("CPF inválido. Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        senha = input_asterisco("Digite sua senha: ")
        senha_valida = validar_senha(senha)

        if senha_valida:
            continue
        else:
            print("Senha inválida. Tente novamente.")

        confirmar_senha = input_asterisco("Confirme sua senha: ")

        if confirmar_senha == senha:
            break

    cadastrar_instrutor(nome, email, cpf, senha)

def login_instrutor():
    while True:
        limpar_tela()

        print("--------------------------------------------\n           Login\n--------------------------------------------")

        email = input("Digite seu e-mail: ")
        senha = input_asterisco("Digite sua senha: ")

        instrutor_autenticado = autenticar_instrutor(email, senha)

        if instrutor_autenticado:
            painel_instrutor(instrutor_autenticado)
        else:
            print("E-mail e/ou senha incorretos! Tente novamente.")