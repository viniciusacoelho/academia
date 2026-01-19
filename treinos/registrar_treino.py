from limpar_tela.limpar_tela import limpar_tela
from treinos.crud_treinos import cadastrar_treino

def registrar_treino():
    limpar_tela()

    print("--------------------------------------------\n              Cadastrar Treino\n--------------------------------------------")

    menu = ["Empurrar", "Puxar", "Inferior", "Inferior Itermediário"]

    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            id = int(input("Digite o ID do tipo do treino: "))
            
            if id == 1:
                tipo = "Puxar"
            elif id == 2:
                tipo = "Empurrar"
            elif id == 3:
                tipo = "Inferior"
            elif id == 4:
                tipo = "Inferior Intermediário"
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

    quantidade_exercicios = int(input("Digite a quantidade de exercícios: "))

    for exercicio in range(quantidade_exercicios):
        nome_exercicio = input(f"Digite o nome do exercício {exercicio + 1}: ")
        peso = float(input(f"Digite o peso do exercício {exercicio + 1}: "))
        repeticoes = int(input(f"Digite o número de repetições do exercício {exercicio + 1}: "))
        series = int(input(f"Digite a quantidade de séries do exercício {exercicio + 1}: "))
        # tempo_descanso = float(input(f"Digite o tempo de descanso do exercício {exercicio + 1}: "))
        tempo_descanso = input(f"Digite o tempo de descanso do exercício {exercicio + 1}: ")

    cadastrar_treino(tipo, quantidade_exercicios, nome_exercicio, peso, repeticoes, series, tempo_descanso)