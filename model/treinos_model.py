from repository.treinos_repository import listar_treinos

def selecionar_treino():
    from view.treinos_view.menu_treino import imprimir_treinos
    imprimir_treinos()

    try:
        print("--------------------------------------------")
        id_treino = int(input("Digite o ID do treino: "))
        treino_identificado = identificar_treino(id_treino, 0)

        if treino_identificado:
            return id_treino
        else:
            return "ID do treino inválido! Tente novamente."

    except ValueError:
        return "[ERRO]: Digite um número!"

def identificar_treino(atributo: int, posicao: int):
    treinos = listar_treinos()

    for treino in treinos:
        if atributo == treino[posicao]:
            return True

    return False