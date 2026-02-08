from limpar_tela.limpar_tela import limpar_tela
from treinos.crud_treinos import listar_treino_aluno, atualizar_treino_aluno, listar_treinos

def painel_treino(id_aluno: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel Treino\n--------------------------------------------")

        menu = ["Visualizar Treinos", "Editar Treino", "Voltar"]
        # TODO:
        # menu = ["Visualizar Treinos", "Editar Treino", "Adicionar Exercício", "Remover Exercício", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: visulizar_treinos(id_aluno)
                case 2: editar_treino(id_aluno)
                # case 3: pass    # TODO: 3ª opção de treino
                case 3:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def visulizar_treinos(id_aluno: int):
    treinos_alunos = listar_treino_aluno(id_aluno)

    for treinos_aluno in treinos_alunos:
        print(f"Treino {treinos_aluno[0]}\nTipo: {treinos_aluno[1]}\nNome do Exercício: {treinos_aluno[2]}\nPeso: {treinos_aluno[3]}\nRepetições: {treinos_aluno[4]}\nSéries: {treinos_aluno[5]}\nTempo de Descanço: {treinos_aluno[6]}")

def editar_treino(id_aluno: int):
    while True:
        visulizar_treinos(id_aluno)

        try:
            print("--------------------------------------------")
            id_treino = int(input("Digite o ID do treino para editar: "))

            treinos = listar_treinos()
            for treino in treinos:
                if id_treino == treino[0]:
                    nome_exercicio = input("Digite o nome do exercício para editar: ")
                    editar_treino_aluno(id_aluno, id_treino, nome_exercicio)
                    break
            else:
                print("ID inválido! Tente novamente.")
                print("--------------------------------------------")

        except ValueError:
            print("[ERRO]: Digite um número!")

def editar_treino_aluno(id_aluno: int, id_treino: int, nome_exercicio: str):
    while True:
        limpar_tela()
    
        print("\n--------------------------------------------\n           Atualizar Treino\n--------------------------------------------")

        menu = ["Editar Nome do Exercício", "Editar Peso", "Editar Repetições", "Editar Séries", "Editar Tempo de Descanço", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    novo_nome = input("Digite o novo nome do exercício: ")
                    atualizar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_nome, "nome_exercicio", "Nome do exerício")
                    break
                case 2:
                    while True:
                        try:
                            novo_peso = float(input(f"Digite o novo peso do exercício: "))
                            atualizar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_peso, "peso", "Peso")
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                case 3:
                    while True:
                        try:
                            novo_numero_repeticoes = int(input(f"Digite o novo número de repetições do exercício: "))
                            atualizar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_numero_repeticoes, "repeticoes", "Repetições")
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                case 4:
                    while True:
                        try:
                            novo_numero_series = int(input(f"Digite a nova quantidade de séries do exercício: "))
                            atualizar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_numero_series, "series", "Séries")
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                case 5:
                    while True:
                        try:
                            novo_tempo_descanso = float(input(f"Digite o novo tempo de descanso do exercício: "))
                            atualizar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_tempo_descanso, "tempo_descanso", "Tempo de Descanço")
                            break
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")