from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import autenticar_aluno
from alunos.painel_aluno import painel_aluno
from msvcrt import getch

def login():
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