from limpar_tela.limpar_tela import limpar_tela
# from alunos.criar_conta_aluno import criar_conta
# from alunos.login_aluno import login
from alunos.crud_alunos import cadastrar_aluno
from alunos.login_aluno import input_asterisco
from alunos.crud_alunos import autenticar_aluno
from alunos.painel_aluno import painel_aluno
from alunos.validar_aluno import validar_nome, validar_email, validar_altura
from msvcrt import getch

def menu_aluno():
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Menu Aluno\n--------------------------------------------")

        menu = ["Criar Conta", "Login", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: criar_conta_aluno()
                case 2: login_aluno()
                case 3:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def criar_conta_aluno():
    limpar_tela()

    print("\n--------------------------------------------\n            Criar Conta\n--------------------------------------------")

    while True:
        nome = input("Digite seu nome: ")
        nome_valido = validar_nome(nome)
        
        if nome_valido:
            break
        else:
            print("Nome invádlido. Tente novamente.")
    
    while True:
        email = input("Digite seu e-mail: ")
        email_valido = validar_email(email)
        if email_valido:
            break
        else:
            print("E-mail invádlido. Tente novamente.")

    while True:
        try:
            altura = float(input("Digite sua altura: "))
            altura_valida = validar_altura(str(altura))
            
            if altura_valida:
                break
            else:
                print("E-mail invádlido. Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    ## TODO: validar se uma pessoa não digitar o ponto e tiver 3 numeros colocar um ponto ou imprimir uma mensagem de erro
    while True:
        try:
            peso = float(input("Digite seu peso: "))
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

    data_nascimento = input("Digite sua data de nascimento: ")
    # while True:
        # try:
        #     data_nascimento = int(input("Digite sua data de nascimento: "))
        #     break
        # except ValueError:
        #     print("[ERRO]: Digite um número!")

    senha = input_asterisco("Digite sua senha: ")

    cadastrar_aluno(nome, email, altura, peso, data_nascimento, senha)

def login_aluno():
    while True:
        limpar_tela()

        print("--------------------------------------------\n           Login\n--------------------------------------------")

        email = input("Digite seu e-mail: ")
        senha = input_asterisco("Digite sua senha: ")

        aluno_autenticado = autenticar_aluno(email, senha)

        if aluno_autenticado:
            painel_aluno(aluno_autenticado[0])
        else:
            print("E-mail e/ou senha incorretos! Tente novamente.")

def input_asterisco(mensagem=""):
    print(mensagem, end="", flush=True)
    senha = ""

    while True:
        char = getch()

        if char in {b'\r', b'\n'}:  # Enter
            print()
            break
        elif char == b'\x08':  # Backspace
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        else:
            senha += char.decode("UTF-8")
            print("*", end="", flush=True)

    return senha