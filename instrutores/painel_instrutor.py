from limpar_tela.limpar_tela import limpar_tela
# from instrutores.atualizar_instrutor import atualizar_instrutor
from instrutores.crud_instrutores import listar_aluno_instrutor, atualizar_instrutor
from alunos.crud_alunos import listar_alunos
from treinos.registrar_treino import registrar_treino
from treinos.painel_treino import editar_treino
from alunos.painel_aluno import excluir_conta
from exercicios.menu_exercicio import menu_exercicio

def painel_instrutor(instrutor_autenticado: list):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Treino\n--------------------------------------------")

        menu = ["Criar Treino", "Editar Treino", "Criar Exercício", "Editar Exercício", "Visualizar Alunos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        # TODO: Funcionalidade de Adicionar/Remover Exercício
        # menu = ["Criar Treino", "Editar Treino", "Adicionar Exercício", "Visualizar Alunos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: criar_treino(instrutor_autenticado)
                case 2: editar_treino_instrutor()
                case 3: visualizar_alunos(instrutor_autenticado[0])
                case 4: atualizar_cadastro(instrutor_autenticado[0])
                case 5: excluir_conta(instrutor_autenticado[0], "Instrutor")
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def criar_treino(instrutor_autenticado: int):
    alunos = listar_alunos()
    for aluno in alunos:
        print(f"{aluno[0]} - {aluno[1]}")
    id_aluno = int(input("Digite o ID do aluno para criar o treino: "))
    registrar_treino(instrutor_autenticado, id_aluno)

def editar_treino_instrutor():
    while True:
        alunos = listar_alunos()
        for aluno in alunos:
            print(f"{aluno[0]} - {aluno[1]}")
        try:
            id_aluno = int(input("Digite o ID do aluno para editar o treino: "))
            editar_treino(id_aluno)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def visualizar_alunos(id_instrutor: int):
    alunos = listar_aluno_instrutor(id_instrutor)
    for aluno in alunos:
        print(f"{aluno[0]} - {aluno[1]}")

def atualizar_cadastro(id_instrutor: int):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n          Atualizar Instrutor\n--------------------------------------------")

        menu = ["Editar Nome", "Editar E-mail", "Editar CPF", "Editar Senha", "Voltar"]
        while True:
            for i in range(len(menu)):
                print(f"{i + 1} - {menu[i]}")

            try:
                print("--------------------------------------------")
                opcao = int(input("Digite uma opção: "))
                
                match opcao:
                    case 1:
                        novo_nome = input("Digite seu novo nome: ")
                        atualizar_instrutor(id_instrutor, novo_nome, "nome")
                        break
                    case 2:
                        novo_email = input("Digite seu novo e-mail: ")
                        atualizar_instrutor(id_instrutor, novo_email, "email")
                        break
                    case 3:
                        novo_cpf = input("Digite seu novo CPF: ")
                        atualizar_instrutor(id_instrutor, novo_cpf, "cpf")
                        break
                    case 4:
                        nova_senha = float(input("Digite sua nova senha: "))
                        atualizar_instrutor(id_instrutor, nova_senha, "senha")
                        break
                    case 5:
                        print("Voltando...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente.")

            except ValueError:
                print("[ERRO]: Digite um número!")