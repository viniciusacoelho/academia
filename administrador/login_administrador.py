from limpar_tela.limpar_tela import limpar_tela
from alunos.menu_aluno import input_asterisco
from administrador.menu_administrador import menu_administrador

def login_administrador():
    SENHA_ACESSO = "1234"

    while True:
        limpar_tela()

        print("--------------------------------------------\n                   Login\n--------------------------------------------")
        senha = input_asterisco("Digite a senha de acesso: ")

        if senha == SENHA_ACESSO:
            print("Login realizado com sucesso! Seja bem-vindo(a)!")
            menu_administrador()
            break
        else:
            print("Senha de acesso inválida! Tente novamente.")