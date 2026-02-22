from repository.exercicios_repository import listar_exercicios
from repository.treino_exercicio_repository import listar_treino_exercicio, deletar_treino_exercicio
from model.treinos_model import identificar_treino

def selecionar_exercicio():
    while True:
        try:
            id_exercicio = int(input("Digite o ID do exercício: "))
            exercicio_identificado = identificar_exercicio(id_exercicio, 0)

            if exercicio_identificado:
                return id_exercicio
            else:
                print("ID do exercício não cadastrado anteriormente. Tente novamente.")
                print("--------------------------------------------")
        except ValueError:
            print("[ERRO]: Digite um número!")
            print("--------------------------------------------")

def identificar_exercicio(id_exercicio: int, posicao: int):
    exercicios = listar_exercicios()
    for exercicio in exercicios:
        if id_exercicio == exercicio[posicao]:
            return True
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