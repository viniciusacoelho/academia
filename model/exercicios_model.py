from repository.exercicios_repository import listar_exercicios
from repository.treino_exercicio_repository import listar_treino_exercicio, deletar_treino_exercicio
from model.treinos_model import identificar_treino

def selecionar_exercicio():
    from view.exercicios_view.menu_exercicio import imprimir_exercicios

    while True:
        imprimir_exercicios()

        try:
            id_exercicio = int(input("Digite o ID do exercício: "))

            exercicio_identificado = identificar_exercicio(id_exercicio)
            if exercicio_identificado:
                return id_exercicio
            else:
                return "ID do exercício não cadastrado anteriormente. Tente novamente."

            # exercicios = listar_exercicios()
            # for exercicio in exercicios:
            #     if id_exercicio == exercicio[0]:
            #         return id_exercicio
            # else:
            #     print("ID do exercício não cadastrado anteriormente. Tente novamente.")

        except ValueError:
            return "[ERRO]: Digite um número!"

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
            return "ID do exercício não cadastrado anteriormente. Tente novamente."
    except ValueError:
        print("[ERRO]: Digite um número!")

def confirmar_remover_exercicio(id_exercicio: int, id_aluno: int):
    while True:
        resposta = input("Tem certeza que deseja remover o exercicio? (s/n): ").lower()

        if resposta == "s" or resposta == "sim":
            deletar_treino_exercicio(id_exercicio, id_aluno)
            break
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            break
        else:
            print("Resposta inválida! Tente novamente.")