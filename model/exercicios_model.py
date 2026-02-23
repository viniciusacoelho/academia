from repository.exercicios_repository import listar_exercicios

def identificar_exercicio(id_exercicio: int, posicao: int):
    exercicios = listar_exercicios()

    for exercicio in exercicios:
        if id_exercicio == exercicio[posicao]:
            return True

    return False

def selecionar_exercicio():
    try:
        id_exercicio = int(input("Digite o ID do exercício: "))
        exercicio_identificado = identificar_exercicio(id_exercicio, 0)

        if exercicio_identificado:
            return id_exercicio
        else:
            print("ID do exercício não cadastrado anteriormente. Tente novamente.")
            print("--------------------------------------------")
            return False

    except ValueError:
        print("[ERRO]: Digite um número!")
        print("--------------------------------------------")
        return False

def confirmar_deletar_exercicio(id_exercicio: int):
    while True:
        resposta = input("Tem certeza que deseja excluir o exercício? (s/n): ").lower()

        if resposta == "s" or resposta == "sim":
            return id_exercicio
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            return False
        else:
            print("Resposta inválida! Tente novamente.")
            return False