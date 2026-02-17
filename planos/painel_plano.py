from limpar_tela.limpar_tela import limpar_tela
from planos.crud_planos import listar_planos, visualizar_plano_aluno, assinar_plano_aluno, cancelar_plano_aluno
from pagamento.pagamento import pagamento
from planos.menu_plano import imprimir_planos, identificar_plano

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
    total_planos = len(listar_planos())

    if total_planos == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        plano_aluno = visualizar_plano_aluno(id_aluno)

        if len(plano_aluno) == 0:
            print("Nenhum plano assinado anteriormente.")
        else:
            planos = visualizar_plano_aluno(id_aluno)

            for plano in planos:
                print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")

def assinar_plano(id_aluno: int):
    total_planos = len(listar_planos())

    if total_planos == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        total_planos_aluno = assinar_plano(id_aluno)

        if len(total_planos_aluno) == 1:
            print("Número máximo de planos assinado (1).")
        else:
            while True:
                print("--------------------------------------------")
                imprimir_planos()

                try:
                    id_plano = int(input("Digite o ID do plano para assinar: "))
                    plano_identificado = identificar_plano(id_plano, 0)

                    if plano_identificado:
                        metodo_pagamento, data_hora = pagamento()
                        assinar_plano_aluno(id_plano, id_aluno, metodo_pagamento, data_hora)
                        break
                    else:
                        print("ID do plano não cadastrado anteriormente. Tente novamente.")
                except ValueError:
                    print("[ERRO]: Digite um número!")

def cancelar_plano(id_aluno: int):
    total_planos = len(listar_planos())

    if total_planos == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        total_planos_aluno = visualizar_plano_aluno(id_aluno)

        if len(total_planos_aluno) == 0:
            print("Nenhum plano assinado anteriormente.")
        else:
            while True:
                print("--------------------------------------------")
                visualizar_plano(id_aluno)

                try:
                    print("--------------------------------------------")
                    id_plano = int(input("Digite o ID do plano para cancelar: "))
                    plano_identificado = identificar_plano(id_plano, 0)

                    if plano_identificado:
                        confirmar_cancelar_plano(id_plano, id_aluno)
                        break
                    else:
                        print("ID do plano não cadastrado anteriormente. Tente novamente.")
                except ValueError:
                    print("[ERRO]: Digite um número!")

def confirmar_cancelar_plano(id_plano: int, id_aluno: int):
    while True:
        resposta = input("Tem certeza que deseja cancelar seu plano? (s/n): ").lower()

        if resposta == "s" or resposta == "sim":
            cancelar_plano_aluno(id_plano, id_aluno)
            break
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            break
        else:
            print("Resposta inválida! Tente novamente.")