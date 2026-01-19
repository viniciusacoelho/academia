def atualizar_treino():
    print("\n--------------------------------------------\n           Atualizar Treino\n--------------------------------------------")
    menu = ["Nome do Exercício", "Peso", "Repetições", "Séries", "Tempo de Descanço", "Voltar"]

    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1:
                    nome = input("Digite o novo nome do exercício: ")
                case 2:
                    peso = float(input(f"Digite o novo peso do exercício: "))
                case 3:
                    repeticoes = int(input(f"Digite o novo número de repetições do exercício: "))
                case 4:
                    series = int(input(f"Digite a nova quantidade de séries do exercício: "))
                case 5:
                    tempo_descanso = float(input(f"Digite o novo tempo de descanso do exercício: "))
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")