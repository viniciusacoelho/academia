from limpar_tela.limpar_tela import limpar_tela
from planos.crud_planos import listar_planos, cadastrar_plano_aluno, listar_plano_aluno, deletar_plano_aluno
from pagamento.pagamento import pagamento
from planos.menu_plano import imprimir_planos

def painel_plano(id_aluno: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel Plano\n--------------------------------------------")

        menu = ["Visualizar Plano", "Assinar Plano", "Cancelar Plano", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: visualizar_plano(id_aluno)
                case 2: assinar_plano(id_aluno)
                case 3: cancelar_plano(id_aluno)
                case 4:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def visualizar_plano(id_aluno: int):
    plano_aluno = listar_plano_aluno(id_aluno)

    if len(plano_aluno) == 0:
        print("Nenhum plano escolhido anteriormente.")
    else:
        planos = listar_plano_aluno(id_aluno)

        for plano in planos:
            print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")

def assinar_plano(id_aluno: int):
    # TODO: Talvez transformar em função:
    while True:
        plano_aluno = listar_plano_aluno(id_aluno)
        if len(plano_aluno) == 1:
            print("Plano já assinado anteriormente.")
            break

        total_planos = listar_planos()

        if len(total_planos) > 0:
            while True:
                imprimir_planos()

                try:
                    id_plano = int(input("Digite o ID do plano para assinar: "))
                    metodo_pagamento, data_hora = pagamento()
                    cadastrar_plano_aluno(id_aluno, id_plano, metodo_pagamento, data_hora)
                    break
                except ValueError:
                    print("[ERRO]: Digite um número!")
            break

        else:
            print("Nenhum plano cadastrado anteriormente.")
            break

def cancelar_plano(id_aluno: int):
    # TODO: Talvez transformar em função:
    while True:
        plano_aluno = listar_plano_aluno(id_aluno)
    
        if len(plano_aluno) == 0:
            print("Nenhum plano assinado anteriormente.")
            break

        visualizar_plano(id_aluno)

        try:
            id_plano = int(input("Digite o ID do plano para cancelar: "))
            confirmar_cancelar_plano(id_plano, id_aluno)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def confirmar_cancelar_plano(id_plano: int, id_aluno: int):
    while True:
        resposta = input("Tem certeza que deseja cancelar seu plano? (s/n): ").lower()

        if resposta == "s" or resposta == "sim":
            deletar_plano_aluno(id_plano, id_aluno)
            break
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            break
        else:
            print("Resposta inválida! Tente novamente.")