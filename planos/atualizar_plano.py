from planos.crud_planos import listar_planos, atualizar_plano

def atualizar_plano():
    while True:
        listar_planos()

        print("\n--------------------------------------------\n          Atualizar Plano\n--------------------------------------------")
        try:
            id = int("Digite o ID do plano para atualizar: ")
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

    menu = ["Nome", "Descrição", "Tipo", "Preço"]
    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    nome = input("Digite o novo nome do plano: ")
                    
                case 3:
                    descricao = input("Digite a nova descrição do plano: ")
                case 1:
                    menu = ["Mensal", "Semestral", "Anual"]
                    while True:
                        print("\n--------------------------------------------\n")
                        for i in range(len(menu)):
                            print(f"{i + 1} - {menu[i]}")

                        try:
                            tipo = int(input("Digite o ID do novo tipo do plano: "))

                            match tipo:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    pass
                                case _:
                                    print("Opção inválida!")
                            break
                        except Exception as e:
                            print("[ERRO]: Digite um número!")

                    tipo = str(tipo)
                    if tipo == "1":
                        tipo = "Mensal"
                    elif tipo == "2":
                        tipo = "Semestral"
                    elif tipo == "3":
                        tipo = "Anual"
                    tipo = input("Digite o novo tipo do plano: ")
                case 1:
                    preco = float(input("Digite o novo preço do plano: "))

                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")

    # atualizar_plano(atributo)