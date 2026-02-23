from repository.treinos_repository import listar_treinos

def identificar_treino(atributo: int, posicao: int):
    treinos = listar_treinos()

    for treino in treinos:
        if atributo == treino[posicao]:
            return True

    return False

def selecionar_treino():
    try:
        print("--------------------------------------------")
        id_treino = int(input("Digite o ID do treino: "))
        treino_identificado = identificar_treino(id_treino, 0)

        if treino_identificado:
            return id_treino
        else:
            print("ID do treino inválido! Tente novamente.")
            return False

    except ValueError:
        print("[ERRO]: Digite um número!")
        return False