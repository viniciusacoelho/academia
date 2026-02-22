from repository.planos_repository import deletar_plano, listar_planos

def identificar_plano(atributo: int, posicao: int):
    planos = listar_planos()
    for plano in planos:
        if atributo == plano[posicao]:
            return True
    return False

def confirmar_cancelar_plano():
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

        except ValueError:
            return "[ERRO]: Digite um número!"