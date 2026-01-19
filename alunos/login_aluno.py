from alunos.crud_alunos import autenticar_aluno

def login(aluno_autenticado: list):
    print("--------------------------------------------\n           Login\n--------------------------------------------")

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    autenticar_aluno(email, senha)