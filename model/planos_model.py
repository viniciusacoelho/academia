from repository.planos_repository import deletar_plano, listar_planos

def decidir_excluir_plano(id_plano: int):
    while True:
        resposta = input("Tem certeza que deseja excluir o plano? (s/n): ").lower()
        if resposta == "s" or resposta == "sim":
            deletar_plano(id_plano)
            break
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            break
        else:
            print("Resposta inválida! Tente novamente.")

def identificar_plano(atributo: int, posicao: int):
    planos = listar_planos()
    for plano in planos:
        if atributo == plano[posicao]:
            return True
    return False

def confirmar_cancelar_plano(id_plano: int, id_aluno: int):
    while True:
        resposta = input("Tem certeza que deseja cancelar seu plano? (s/n): ").lower()

        if resposta == "s" or resposta == "sim":
            return True
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            return False
        else:
            print("Resposta inválida! Tente novamente.")

def selecionar_plano():
    from view.planos_view.menu_plano import imprimir_planos
    while True:
        print("--------------------------------------------")
        imprimir_planos()

        try:
            id_plano = int(input("Digite o ID do plano: "))

            plano_identificado = identificar_plano(id_plano, 0)
            if plano_identificado:
                return id_plano
            else:
                return "ID do plano não cadastrado anteriormente. Tente novamente."

            # planos = listar_planos()
            # for plano in planos:
            #     if id_plano == plano[0]:
            #         return id_plano
            # else:
            #     print("ID do plano não cadastrado anteriormente. Tente novamente.")

        except ValueError:
            return "[ERRO]: Digite um número!"