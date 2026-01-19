from instrutores.crud_instrutores import autenticar_instrutor

def login(instrutor_autenticado: list):
    print("--------------------------------------------\n           Login\n--------------------------------------------")

    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    autenticar_instrutor(email, senha)