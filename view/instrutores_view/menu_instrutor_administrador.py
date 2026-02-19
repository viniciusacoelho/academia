from util.limpar_tela_util import limpar_tela
from view.instrutores_view.menu_instrutor import criar_conta_instrutor
from repository.instrutores_repository import listar_instrutores, buscar_instrutor, deletar_instrutor
from view.instrutores_view.painel_instrutor import editar_instrutor
from model.instrutores_model import identificar_instrutor

def menu_instrutor_administrador():
    while True:    
        limpar_tela()

        print("--------------------------------------------\n        Menu Instrutor Administrador\n--------------------------------------------")

        menu = ["Cadastrar Instrutor", "Listar Instrutores", "Buscar Instrutor", "Atualizar Instrutor", "Deletar Instrutor", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: criar_conta_instrutor()
                case 2: 
                    imprimir_instrutores()
                    if len(listar_instrutores()) != 0:
                        print("Instrutores listados com sucesso!")
                case 3: procurar_instrutor()
                case 4: editar_instrutor()
                case 5: remover_instrutor()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

def imprimir_instrutores():
    quantidade_instrutores = len(listar_instrutores())

    if quantidade_instrutores == 0:
        print("Nenhum instrutor cadastrado anteriormente.")
    else:
        instrutores = listar_instrutores()

        for instrutor in instrutores:
            print(f"instrutor {instrutor[0]}\nNome: {instrutor[1]}\nE-mail: {instrutor[2]}\nCPF: {instrutor[3]}\nSenha: {instrutor[4]}")
            print("--------------------------------------------")

def procurar_instrutor():
    quantidade_instrutores = len(listar_instrutores())

    if quantidade_instrutores == 0:
        print("Nenhum instrutor cadastrado anteriormente.")
    else:
        email = input("Digite o e-mail do instrutor para buscar: ")
        instrutor_identificado = identificar_instrutor(email, 2)

        if instrutor_identificado:
            instrutor_busca = buscar_instrutor(email)
            print("--------------------------------------------")

            for instrutor in instrutor_busca:
                print(f"instrutor {instrutor[0]}\nNome: {instrutor[1]}\nE-mail: {instrutor[2]}\nCPF: {instrutor[3]}\nSenha: {instrutor[4]}")
        else:
            print("E-mail do instrutor inválido! Tente novamente.")

def remover_instrutor():
    quantidade_instrutores = len(listar_instrutores())

    if quantidade_instrutores == 0:
        print("Nenhum instrutor cadastrado anteriormente.")
    else:
        imprimir_instrutores()

        try:
            id_instrutor = int(input("Digite o ID do instrutor para deletar: "))
            instrutor_identificado = identificar_instrutor(id_instrutor, 0)

            if instrutor_identificado:
                deletar_instrutor(id_instrutor)
            else:
                print("ID do aluno inválido! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")