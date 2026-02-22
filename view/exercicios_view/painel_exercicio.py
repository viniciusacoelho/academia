from util.limpar_tela_util import limpar_tela
from repository.exercicios_repository import listar_exercicios, atualizar_exercicio, deletar_exercicio
from repository.treino_exercicio_repository import cadastrar_treino_exercicio, listar_treino_exercicio, listar_treino_exercicio, deletar_treino_exercicio, listar_treino_exercicio_aluno, listar_treino_exercicio_instrutor
from view.exercicios_view.menu_exercicio import registrar_exercicio, identificar_exercicio
from view.treinos_view.menu_treino import identificar_treino
# from treinos.painel_treino import visulizar_treinos
from repository.treinos_repository import listar_treino_aluno, listar_treino_instrutor
from service.exercicios_service import validar_quantidade_series, validar_peso, validar_numero_repeticoes, validar_tempo_descanso
from service.exercicios_service import validar_quantidade_exercicios
from util.validacoes_util import validar_nome
from model.exercicios_model import selecionar_exercicio, confirmar_deletar_exercicio
from view.treinos_view.painel_treino_aluno import visulizar_treinos_aluno
from model.treinos_model import selecionar_treino
from view.treinos_view.painel_treino_aluno import visulizar_treinos_aluno
from view.treinos_view.painel_treino_instrutor import visulizar_treinos_instrutor

def painel_exercicio(id: int, entidade: str):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel Exercício\n--------------------------------------------")
        menu = ["Adicionar Exercício", "Editar Exercício", "Excluir Exercício", "Voltar"]

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: adicionar_exercicio(id, entidade)
                case 2: editar_exercicio(id, entidade)
                case 3: excluir_exercicio(id, entidade)
                case 4:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def adicionar_exercicio(id: int, entidade: str):
    if entidade == "alunos":
        total_treinos = listar_treino_aluno(id)
    elif entidade == "instrutores":
        total_treinos = listar_treino_instrutor(id)

    if len(total_treinos) == 0:
        print("Nenhum treino cadastrado à você anteriormente.")
    else:
        if entidade == "alunos":
            visulizar_treinos_aluno(id)
        elif entidade == "instrutores":
            visulizar_treinos_instrutor(id)

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

def editar_exercicio(id: int, entidade: str):
    if entidade == "alunos":
        total_treinos = listar_treino_aluno(id)
    elif entidade == "instrutores":
        total_treinos = listar_treino_instrutor(id)

    if len(total_treinos) == 0:
        print("Nenhum treino cadastrado à você anteriormente.")
    else:
        if entidade == "alunos":
            total_exercicios = listar_treino_exercicio_aluno(id)
        elif entidade == "instrutores":
            total_exercicios = listar_treino_exercicio_instrutor(id)
        
        if len(total_exercicios) == 0:
            print("Nenhum exercício cadastrado à você anteriormente.")
        else:
            if entidade == "alunos":
                visulizar_treinos_aluno(id)
            elif entidade == "instrutores":
                visulizar_treinos_instrutor(id)
            
            id_exercicio = selecionar_exercicio()

            while True:
                limpar_tela()

                print("\n--------------------------------------------\n          Atualizar Exercício\n--------------------------------------------")
                menu = ["Nome", "Quantidade de Séries", "Número de Repetições", "Peso", "Tempo de Descanço", "Voltar"]

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
                                    nova_quantidade_series = int(input("Digite a nova quantidade de séries do exercício: "))
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
                                    novo_numero_repeticoes = int(input("Digite o novo número de repetições do exercício: "))
                                    novo_numero_repeticoes_valido = validar_numero_repeticoes(novo_numero_repeticoes)
                                    if novo_numero_repeticoes_valido:
                                        atualizar_exercicio(id_exercicio, novo_numero_repeticoes, "numero_repeticoes", "Número de Repetições")
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

def excluir_exercicio(id: int, entidade: str):
    if entidade == "alunos":
        total_treinos = listar_treino_aluno(id)
    elif entidade == "instrutores":
        total_treinos = listar_treino_instrutor(id)

    if len(total_treinos) == 0:
        print("Nenhum treino cadastrado à você anteriormente.")
    else:
        if entidade == "alunos":
            total_exercicios = listar_treino_exercicio_aluno(id)
        elif entidade == "instrutores":
            total_exercicios = listar_treino_exercicio_instrutor(id)
        
        if len(total_exercicios) == 0:
            print("Nenhum exercício cadastrado à você anteriormente.")
        else:
            if entidade == "alunos":
                visulizar_treinos_aluno(id)
            elif entidade == "instrutores":
                visulizar_treinos_instrutor(id)
                id_exercicio = selecionar_exercicio()

            id_exercicio = selecionar_exercicio()
            deletar_confirmado = confirmar_deletar_exercicio(id_exercicio)

            if deletar_confirmado:
                deletar_treino_exercicio(id_exercicio)