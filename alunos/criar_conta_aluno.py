from limpar_tela.limpar_tela import limpar_tela
from alunos.validar_aluno import validar_nome, validar_email, validar_altura
from alunos.crud_alunos import cadastrar_aluno
from alunos.login_aluno import input_asterisco

def criar_conta():
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
            altura_valida = validar_altura(altura)
            
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