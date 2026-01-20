from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import cadastrar_aluno

def criar_conta():
    limpar_tela()

    print("\n--------------------------------------------\n            Criar Conta\n--------------------------------------------")

    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    # data_nacimento = int(input("Digite sua data de nascimento: "))
    data_nacimento = input("Digite sua data de nascimento: ")
    senha = input("Digite sua senha: ")

    cadastrar_aluno(nome, email, altura, peso, data_nacimento, senha)