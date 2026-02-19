from util.limpar_tela_util import limpar_tela
from repository.exercicios_repository import listar_exercicios, atualizar_exercicio
from repository.treino_exercicio_repository import cadastrar_treino_exercicio, listar_treino_exercicio, listar_treino_exercicio, deletar_treino_exercicio 
from view.exercicios_view.menu_exercicio import registrar_exercicio, identificar_exercicio
from view.treinos_view.menu_treino import identificar_treino
# from treinos.painel_treino import visulizar_treinos
from repository.treinos_repository import listar_treino_aluno
from service.exercicios_service import validar_quantidade_series, validar_peso, validar_numero_repeticoes, validar_tempo_descanso
from service.exercicios_service import validar_quantidade_exercicios
from util.validacoes_util import validar_nome
from model.exercicios_model import selecionar_exercicio, confirmar_remover_exercicio

def painel_exercicio(id_aluno: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel exercicio\n--------------------------------------------")

        menu = ["Adicionar Exercício", "Editar Exercício", "Excluir Exercício", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: adicionar_exercicio(id_aluno)
                # case 2: editar_exercicio(id_aluno)
                # case 3: excluir_exercicio(id_aluno)
                case 4:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def adicionar_exercicio(id_aluno: int):
    total_treino_aluno = listar_treino_aluno(id_aluno)

    if len(total_treino_aluno) == 0:
        print("Nenhum exercício escolhido anteriormente.")
    else:
        # TODO: Verificar se essa função funciona agora
        # visulizar_treinos(id_aluno)
        treinos_aluno = listar_treino_aluno(id_aluno)

        for treino_aluno in treinos_aluno:
            print(f"Treino {treino_aluno[0]}\nNome: {treino_aluno[1]}\nTipo: {treino_aluno[2]}")
            print("Exercícios:")
            
            if len(listar_treino_exercicio(treino_aluno[0])) == 0:
                print("Nenhum exercício cadastrado anteriormente.")
            else:
                for i in range(len(listar_treino_exercicio(treino_aluno[0]))):
                    exercicios = listar_treino_exercicio(treino_aluno[0])
                    for exercicio in exercicios:
                        print(f"Exercício {exercicio[0]}\nNome: {exercicio[1]}\nQuantidade de séries: {exercicio[2]}\nNúmero de repetições: {exercicio[3]}\nPeso: {exercicio[4]}kg\nTempo de Descanço: {exercicio[5]}")
                        print("--------------------------------------------")
            print(f"Instrutor: {treino_aluno[3]}")
            print("--------------------------------------------")

        try:
            id_treino = int(input("Digite o ID do treino para adicionar o exercício: "))
            treino_identificado = identificar_treino(id_treino, 0)

            if treino_identificado:
                quantidade_exercicios = int(input("Digite a quantidade de exercícios: "))
                quantidade_exercicios_validas = validar_quantidade_exercicios(quantidade_exercicios)

                if quantidade_exercicios_validas:
                    for i in range(quantidade_exercicios):
                
                        exercicios = registrar_exercicio()

                        for id_exercicio in exercicios:
                            cadastrar_treino_exercicio(id_treino, id_exercicio[0])
            else:
                print("ID do treino inválido! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def editar_exercicio(id_aluno: int):
    total_exercicio_aluno = listar_treino_exercicio(id_aluno)

    if len(total_exercicio_aluno) == 0:
        print("Nenhum exercício escolhido anteriormente.")
    else:
        id_exercicio = selecionar_exercicio()
        
        while True:
            limpar_tela()

            print("\n--------------------------------------------\n          Atualizar exercício\n--------------------------------------------")
            menu = ["Nome", "Quantidade de Séries", "Número de Repetições", "Peso", "Tempo de Descanço", "Voltar"]

            while True:
                for i in range(len(menu)):
                    print(f"{i + 1} - {menu[i]}")

                try:
                    print("--------------------------------------------")
                    opcao = int(input("Digite uma opção: "))

                    match opcao:
                        case 1:
                            while True:
                                nome = input("Digite o novo nome do exercício: ")
                                novo_nome_valido = validar_nome(nome)
                                if novo_nome_valido:
                                    atualizar_exercicio(id_exercicio, nome, "nome", "Nome")
                                    break
                                else:
                                    print("Novo nome inválido! Tente novamente.")
                        case 2:
                            while True:
                                try:
                                    nova_quantidade_series = input("Digite a nova quantidade de séries do exercício: ")
                                    nova_quantidade_series_validas = validar_quantidade_series(nova_quantidade_series)
                                    if nova_quantidade_series_validas:
                                        atualizar_exercicio(id_exercicio, nova_quantidade_series, "quantidade_series", "Quantidade de Séries")
                                        break
                                    else:
                                        print("Nova quantidade de séries inválidas! Tente novamente.")
                                except ValueError:
                                    print("[ERRO]: Digite um número!")
                        case 3:
                            while True:
                                try:
                                    novo_numero_repeticoes = float(input("Digite o novo número de repetições do exercício: "))
                                    novo_numero_repeticoes_valido = validar_numero_repeticoes(novo_numero_repeticoes)
                                    if novo_numero_repeticoes_valido:
                                        atualizar_exercicio(id_exercicio, novo_numero_repeticoes, "numero_repetcioes", "Número de Repetições")
                                        break
                                    else:
                                        print("Novo número de repetições inválido! Tente novamente.")
                                except ValueError:
                                    print("[ERRO]: Digite um número!")
                        case 4:
                            while True:
                                try:
                                    print("--------------------------------------------")
                                    novo_peso = int(input("Digite o novo peso de exercicio: "))
                                    novo_peso_valido = validar_peso(novo_peso)
                                    if novo_peso_valido:
                                        atualizar_exercicio(id_exercicio, novo_peso, "peso", "Peso")
                                        break
                                    else:
                                        print("Novo peso inválido! Tente novamente.")
                                except ValueError:
                                    print("[ERRO]: Digite um número!")
                        case 5:
                            while True:
                                menu = ["Segundo (s)", "Minuto (min)", "Hora (h)"]
                                for i in range(len(menu)):
                                    print(f"{i + 1} - {menu[i]}")

                                nova_unidade_medida = input("Digite a nova unidade de medida do tempo de descanço: ").lower()

                                if nova_unidade_medida == "segundo" or nova_unidade_medida == "s":
                                    nova_unidade_medida = "s"
                                    break
                                elif nova_unidade_medida == "minuto" or nova_unidade_medida == "min" or nova_unidade_medida == "m":
                                    nova_unidade_medida = "min"
                                    break
                                elif nova_unidade_medida == "hora" or nova_unidade_medida == "h":
                                    nova_unidade_medida = "h"
                                    break
                                else:
                                    print("Unidade de medida inválida! Tente novamente.")
                            while True:
                                try:
                                    novo_tempo_descanso = float(input("Digite o novo tempo de descanço do exercício: "))
                                    novo_tempo_descanso_valido = validar_tempo_descanso(novo_tempo_descanso)
                                    if novo_tempo_descanso_valido:
                                        novo_tempo_descanso_validado = str(novo_tempo_descanso)
                                        atualizar_exercicio(id_exercicio, novo_tempo_descanso_validado + nova_unidade_medida, "tempo_descanso", "Tempo de Descanço")
                                        break
                                    else:
                                        print("Tempo de descanço inválido! Tente novamente.")
                                except ValueError:
                                    print("[ERRO]: Digite um número!")
                            break
                        case 6:
                            print("Voltando...")
                            break
                        case _:
                            print("Opção inválida! Tente novamente.")

                except ValueError:
                    print("[ERRO]: Digite um número!")

def excluir_exercicio(id_aluno: int):
    total_exercicio_aluno = listar_treino_exercicio(id_aluno)

    if len(total_exercicio_aluno) == 0:
        print("Nenhum exercício escolhido anteriormente.")
    else:
        while True:
            # visulizar_treinos(id_aluno)
            treinos_aluno = listar_treino_aluno(id_aluno)

            for treino_aluno in treinos_aluno:
                print(f"Treino {treino_aluno[0]}\nTipo: {treino_aluno[1]}\nExercícios: {treino_aluno[2]}\nID do Aluno: {treino_aluno[3]}\nID do Instrutor: {treino_aluno[4]}")

            try:
                id_treino = int(input("Digite o ID do treino para remover o exercício: "))

                id_exercicio = int(input("Digite o ID do exercício para remover: "))
                confirmar_remover_exercicio(id_treino, id_exercicio)
                break
            except ValueError:
                print("[ERRO]: Digite um número!")