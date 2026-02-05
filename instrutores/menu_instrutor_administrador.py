from limpar_tela.limpar_tela import limpar_tela
from instrutores.menu_instrutor import criar_conta_instrutor
from instrutores.crud_instrutores import listar_instrutores, buscar_instrutor, deletar_instrutor
from instrutores.painel_instrutor import atualizar_cadastro

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
                    print("Instrutores listados com sucesso!")
                case 3: procurar_instrutor()
                case 4: selecionar_instrutor()
                case 5: remover_instrutor()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

def imprimir_instrutores():
    instrutores = listar_instrutores()

    for instrutor in instrutores:
        print(f"instrutor {instrutor[0]}\nNome: {instrutor[1]}\nE-mail: {instrutor[2]}\nCPF: {instrutor[3]}\nSenha: {instrutor[4]}\n")
        print("--------------------------------------------")

def procurar_instrutor():
    email = input("Digite o e-mail do instrutor para buscar: ")
    instrutor_busca = buscar_instrutor(email)

    for instrutor in instrutor_busca:
        print(f"instrutor {instrutor[0]}\nNome: {instrutor[1]}\nE-mail: {instrutor[2]}\nCPF: {instrutor[3]}\nSenha: {instrutor[4]}\n")

def selecionar_instrutor():
    while True:
        imprimir_instrutores()

        try:
            id_instrutor = int(input("Digite o ID do instrutor para atualizar: "))
            atualizar_cadastro(id_instrutor)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def remover_instrutor():
    while True:
        imprimir_instrutores()

        try:
            id_instrutor = int(input("Digite o ID do instrutor para deletar: "))
            deletar_instrutor(id_instrutor)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")