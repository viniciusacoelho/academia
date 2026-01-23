from limpar_tela.limpar_tela import limpar_tela
from planos.crud_planos import listar_planos, cadastrar_plano_aluno, listar_plano_aluno, deletar_plano_aluno
from pagamento.pagamento import pagamento

def painel_plano(id_aluno: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel Plano\n--------------------------------------------")

        menu = ["Assinar Plano", "Visualizar Plano", "Cancelar Plano", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: assinar_plano(id_aluno)
                case 2: visualizar_plano(id_aluno)
                case 3: cancelar_plano(id_aluno)
                case 4:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def assinar_plano(id_aluno: int):
    while True:
        planos = listar_planos()

        for plano in planos:
            print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: {plano[4]}")

        try:
            id_plano = int(input("Digite o ID do plano para assinar: "))
            metodo_pagamento, data_hora = pagamento()
            cadastrar_plano_aluno(id_aluno, id_plano, data_hora, metodo_pagamento)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def visualizar_plano(id_aluno: int):
    planos = listar_plano_aluno(id_aluno)
    for plano in planos:
        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")

def cancelar_plano(id_aluno):
    while True:
        visualizar_plano(id_aluno)

        try:
            id_plano = int(input("Digite o ID do plano para cancelar: "))

            while True:
                resposta = input("Tem certeza que deseja cancelar seu plano? (s/n): ").lower()
                if resposta == "s" or resposta == "sim":
                    deletar_plano_aluno(id_plano)
                    break
                elif resposta == "n" or resposta == "não" or resposta == "nao":
                    break
                else:
                    print("Resposta inválida! Tente novamente.")

            break
        except ValueError:
            print("[ERRO]: Digite um número!")