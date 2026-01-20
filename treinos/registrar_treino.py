from limpar_tela.limpar_tela import limpar_tela
from treinos.crud_treinos import cadastrar_treino

def registrar_treino(id_instrutor: int, id_aluno: int):
    limpar_tela()

    print("--------------------------------------------\n              Cadastrar Treino\n--------------------------------------------")

    menu = ["Empurrar", "Puxar", "Inferior", "Inferior Intermediário"]

    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            id_treino = int(input("Digite o ID do tipo de treino: "))
            
            match id_treino:
                case 1:
                    tipo = "Empurrar"
                    break
                case 2:
                    tipo = "Puxar"
                    break
                case 3:
                    tipo = "Inferior"
                    break
                case 4:
                    tipo = "Inferior Intermediário"
                    break
                case 4:
                    print("ID de treino inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    quantidade_exercicios = int(input("Digite a quantidade de exercícios: "))

    for i in range(quantidade_exercicios):
        nome_exercicio = input(f"Digite o nome do exercício {i + 1}: ")
        peso = int(input(f"Digite o peso do exercício {i + 1}: "))
        repeticoes = int(input(f"Digite o número de repetições do exercício {i + 1}: "))
        series = int(input(f"Digite a quantidade de séries do exercício {i + 1}: "))
        # tempo_descanso = float(input(f"Digite o tempo de descanso do exercício {i + 1}: "))
        tempo_descanso = input(f"Digite o tempo de descanso do exercício {i + 1}: ")

        cadastrar_treino(tipo, nome_exercicio, peso, repeticoes, series, tempo_descanso, id_aluno, id_instrutor)