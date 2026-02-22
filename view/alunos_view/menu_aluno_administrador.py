from util.limpar_tela_util import limpar_tela
from model.alunos_model import identificar_aluno, selecionar_aluno
from repository.alunos_repository import listar_alunos, deletar_aluno, buscar_aluno
from view.alunos_view.menu_aluno import criar_conta_aluno

def menu_aluno_administrador():
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Menu Aluno Administrador\n--------------------------------------------")
        menu = ["Cadastrar Aluno", "Listar Alunos", "Buscar Aluno", "Atualizar Aluno", "Deletar Aluno", "Voltar"]

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: criar_conta_aluno()
                case 2: 
                    imprimir_alunos()
                    if len(listar_alunos()) != 0:
                        print("Alunos listados com sucesso!")
                case 3: procurar_aluno()
                case 4: selecionar_aluno()
                case 5: remover_aluno()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def imprimir_alunos():
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        alunos = listar_alunos()

        for aluno in alunos:
            print(f"Aluno {aluno[0]}\nNome: {aluno[1]}\nE-mail: {aluno[2]}\nAltura: {aluno[3]}m\nPeso: {aluno[4]}kg\nData de Nascimento: {aluno[5]}\nSenha: {aluno[6]}")
            print("--------------------------------------------")

def remover_aluno():
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        imprimir_alunos()

        try:
            id_aluno = int(input("Digite o ID do aluno para deletar: "))
            aluno_identificado = identificar_aluno(id_aluno, 0)

            if aluno_identificado:
                deletar_aluno(id_aluno)
            else:
                print("ID do aluno inválido! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def procurar_aluno():
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:   
        email = input("Digite o e-mail do aluno para buscar: ")
        aluno_identificado = identificar_aluno(email, 2)

        if aluno_identificado:
            aluno_busca = buscar_aluno(email)
            print("--------------------------------------------")

            for aluno in aluno_busca:
                print(f"Aluno {aluno[0]}\nNome: {aluno[1]}\nE-mail: {aluno[2]}\nAltura: {aluno[3]}m\nPeso: {aluno[4]}kg\nData de Nascimento: {aluno[5]}\nSenha: {aluno[6]}")
        else:
            print("E-mail do aluno inválido! Tente novamente.")