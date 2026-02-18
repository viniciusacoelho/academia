from limpar_tela.limpar_tela import limpar_tela
from exercicios.crud_exercicio import cadastrar_exercicio, listar_exercicios, buscar_exercicio, atualizar_exercicio, deletar_exercicio
from exercicios.validar_exercicio import validar_nome, validar_quantidade_series, validar_peso, validar_numero_repeticoes, validar_tempo_descanso

def menu_exercicio():
    while True:    
        limpar_tela()

        print("--------------------------------------------\n        Menu Exercício\n--------------------------------------------")

        menu = ["Cadastrar Exercício", "Listar Exercícios", "Buscar Exercício", "Atualizar Exercício", "Deletar Exercício", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: registrar_exercicio()
                case 2: 
                    imprimir_exercicios()
                    print("Exercícios listados com sucesso!")
                case 3: procurar_exercicio()
                case 4: editar_exercicio()
                case 5: excluir_exercicio()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

def registrar_exercicio():
    limpar_tela()

    print("--------------------------------------------\n        Cadastrar Exercício\n--------------------------------------------")

    while True:
        nome = input("Digite o nome no exercício: ")
        nome_valido = validar_nome(nome)

        if nome_valido:
            break
        else:
            print("Nome inválido! Tente novamente.")

    while True:
        try:
            quantidade_series = int(input("Digite a quantidade de séries do exercício: "))
            quantidade_series_validas = validar_quantidade_series(quantidade_series)

            if quantidade_series_validas:
                break
            else:
                print("Quantidade de séries inválidas! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        try:
            numero_repeticoes = int(input("Digite o número de repetições do exercício: "))
            numero_repeticoes_valido = validar_numero_repeticoes(numero_repeticoes)

            if numero_repeticoes_valido:
                break
            else:
                print("Número de repetições inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        try:
            peso = int(input("Digite o peso do exercício (em kg): "))
            peso_valido = validar_peso(peso)

            if peso_valido:
                break
            else:
                print("Peso inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        menu = ["Segundo (s)", "Minuto (min)", "Hora (h)"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        unidade_medida = input("Digite a unidade de medida do tempo de descanço: ").lower()

        if unidade_medida == "segundo" or unidade_medida == "s":
            unidade_medida = "s"
            break
        elif unidade_medida == "minuto" or unidade_medida == "min" or unidade_medida == "m":
            unidade_medida = "min"
            break
        elif unidade_medida == "hora" or unidade_medida == "h":
            unidade_medida = "h"
            break
        else:
            print("Unidade de medida inválida! Tente novamente.")

    while True:
        try:
            tempo_descanso = float(input(f"Digite o tempo de descanso do exercício: "))
            tempo_descanso_valido = validar_tempo_descanso(tempo_descanso)

            if tempo_descanso_valido:
                tempo_descanso_validado = str(tempo_descanso)
                # cadastrar_exercicio(nome, numero_repeticoes, quantidade_series, peso, tempo_descanso_validado + unidade_medida)
                break
            else:
                print("Tempo de descanço inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    return cadastrar_exercicio(nome, numero_repeticoes, quantidade_series, peso, tempo_descanso_validado + unidade_medida)

def imprimir_exercicios():
    total_exercicios = len(listar_exercicios())

    if total_exercicios == 0:
        print("Nenhum exercício cadastrado anteriormente.")
    else:
        exercicios = listar_exercicios()

        print("--------------------------------------------")
        for exercicio in exercicios:
            print(f"Exercício {exercicio[0]}\nNome: {exercicio[1]}\nQuantidade de séries: {exercicio[2]}\nNúmero de repetições: {exercicio[3]}\nPeso: {exercicio[4]}kg\nTempo de Descanço: {exercicio[5]}")
            print("--------------------------------------------")

def procurar_exercicio():
    total_exercicios = len(listar_exercicios())

    if total_exercicios == 0:
        print("Nenhum exercício cadastrado anteriormente.")
    else:
        nome = input("Digite o nome do exercício para buscar: ")
        exercicio_identificado = identificar_exercicio(nome, 1)

        if exercicio_identificado:
            exercicio_busca = buscar_exercicio(nome)
            print("--------------------------------------------")

            for exercicio in exercicio_busca:
                print(f"Exercício {exercicio[0]}\nNome: {exercicio[1]}\nQuantidade de séries: {exercicio[2]}\nNúmero de repetições: {exercicio[3]}\nPeso: {exercicio[4]}kg\nTempo de Descanço: {exercicio[5]}")

def editar_exercicio():
    total_exercicios = len(listar_exercicios())

    if total_exercicios == 0:
        print("Nenhum exercício cadastrado anteriormente.")
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

def selecionar_exercicio():
    while True:
        imprimir_exercicios()

        try:
            id_exercicio = int(input("Digite o ID do exercício para atualizar: "))

            exercicio_identificado = identificar_exercicio(id_exercicio)
            if exercicio_identificado:
                return id_exercicio
            else:
                print("ID do exercício não cadastrado anteriormente. Tente novamente.")

            # exercicios = listar_exercicios()
            # for exercicio in exercicios:
            #     if id_exercicio == exercicio[0]:
            #         return id_exercicio
            # else:
            #     print("ID do exercício não cadastrado anteriormente. Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def excluir_exercicio():
    total_exercicios = len(listar_exercicios())

    if total_exercicios == 0:
        print("Nenhum exercício cadastrado anteriormente.")
    else:
        while True:
            imprimir_exercicios()

            try:
                id_exercicio = int(input("Digite o ID do exercício para deletar: "))
                exercicio_identificado = identificar_exercicio(id_exercicio)

                if exercicio_identificado:
                    deletar_exercicio(id_exercicio)
                    break
                else:
                    print("ID do exercício não cadastrado anteriormente. Tente novamente.")

            except ValueError:
                print("[ERRO]: Digite um número!")  

def identificar_exercicio(id_exercicio: int):
    exercicios = listar_exercicios()
    for exercicio in exercicios:
        if id_exercicio == exercicio[0]:
            return True
    return False