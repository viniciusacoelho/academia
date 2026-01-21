from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import autenticar_aluno
from alunos.painel_aluno import painel_aluno

def login():
    limpar_tela()
    print("--------------------------------------------\n           Login\n--------------------------------------------")

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    aluno_autenticado = autenticar_aluno(email, senha)

    painel_aluno(aluno_autenticado[0])