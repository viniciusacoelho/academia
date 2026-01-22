from limpar_tela.limpar_tela import limpar_tela
from treinos.crud_treinos import atualizar_treino

def atualizar_treino(id_treino: int):
    while True:
        limpar_tela()
    
        print("\n--------------------------------------------\n           Atualizar Treino\n--------------------------------------------")

        menu = ["Nome do Exercício", "Peso", "Repetições", "Séries", "Tempo de Descanço", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    novo_nome = input("Digite o novo nome do exercício: ")
                    atualizar_treino(id_treino, novo_nome, "nome")
                    break
                case 2:
                    novo_peso = float(input(f"Digite o novo peso do exercício: "))
                    atualizar_treino(id_treino, novo_peso, "peso")
                    break
                case 3:
                    novo_numero_repeticoes = int(input(f"Digite o novo número de repetições do exercício: "))
                    atualizar_treino(id_treino, novo_numero_repeticoes, "repeticoes")
                    break
                case 4:
                    novo_numero_series = int(input(f"Digite a nova quantidade de séries do exercício: "))
                    atualizar_treino(id_treino, novo_numero_series, "series")
                    break
                case 5:
                    novo_tempo_descanso = float(input(f"Digite o novo tempo de descanso do exercício: "))
                    atualizar_treino(id_treino, novo_tempo_descanso, "tempo_descanso")
                    break
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")