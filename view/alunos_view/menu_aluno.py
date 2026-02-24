from util.limpar_tela_util import limpar_tela
from util.validacoes_util import validar_nome, validar_email, validar_senha
from service.banco_de_dados_service import validar_unique
from service.alunos_service import validar_altura, validar_peso, validar_data_nascimento, formartar_data_nascimento
from util.input_asterisco_util import input_asterisco
from repository.alunos_repository import cadastrar_aluno, autenticar_aluno
from view.alunos_view.painel_aluno import painel_aluno

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
            print("Nome inválido! Tente novamente.")
    
    while True:
        email = input("Digite seu e-mail: ")
        email_valido = validar_email(email)

        if email_valido:
            email_unico = validar_unique(email, "alunos", 2)

            if email_unico:
                break
            else:
                print("E-mail já cadastrado anteriormente. Tente novamente.")
        else:
            print("E-mail inválido! Tente novamente.")

    while True:
        try:
            altura = float(input("Digite sua altura: "))
            altura_valida = validar_altura(str(altura))
            
            if altura_valida:
                break
            else:
                print("Altura inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    ## TODO: validar se uma pessoa não digitar o ponto e tiver 3 numeros colocar um ponto ou imprimir uma mensagem de erro
    while True:
        try:
            peso = float(input("Digite seu peso: "))
            peso_valido = validar_peso(peso)
            
            if peso_valido:
                break
            else:
                print("Peso inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        data_nascimento = input("Digite sua data de nascimento: ")

        try:
            int(data_nascimento)
            data_nascimento_valida = validar_data_nascimento(data_nascimento)

            if data_nascimento_valida:
                data_nascimento = formartar_data_nascimento(data_nascimento)
                break
            else:
                print("Data de nascimento inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        senha = input_asterisco("Digite sua senha: ")
        break
        # senha_valida = validar_senha(senha)
    
        # if senha_valida:
        #     break
        # else:
        #     print("Senha inválida! Tente novamente.")
    
    while True:
        confirmar_senha = input_asterisco("Confirme sua senha: ")
        if confirmar_senha == senha:
            break
        else:
            print("Senhas diferentes! Tente novamente.")

    cadastrar_aluno(nome, email, altura, peso, data_nascimento, senha)

def login_aluno():
    while True:
        limpar_tela()

        print("--------------------------------------------\n           Login\n--------------------------------------------")

        email = input("Digite seu e-mail: ")
        senha = input_asterisco("Digite sua senha: ")

        aluno_autenticado = autenticar_aluno(email, senha)

        if aluno_autenticado:
            print(f"Login realizado com sucesso! Seja bem-vindo(a) {aluno_autenticado[1]}!")
            painel_aluno(aluno_autenticado)
        else:
            print("E-mail e/ou senha incorretos! Tente novamente.")