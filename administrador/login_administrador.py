from limpar_tela.limpar_tela import limpar_tela
from administrador.menu_administrador import menu_administrador
from alunos.login_aluno import input_asterisco

def login_administrador():
    while True:
        limpar_tela()

        print("--------------------------------------------\n           Login\n--------------------------------------------")
        senha_acesso = input_asterisco("Digite a senha de acesso: ")

        if senha_acesso == "1234":
            print("Login realizado com sucesso! Seja bem-vindo(a)!")
            menu_administrador()
            break
        else:
            print("Senha de acesso inválida! Tente novamente.")