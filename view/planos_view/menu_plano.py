from util.limpar_tela_util import limpar_tela
from repository.planos_repository import cadastrar_plano, listar_planos, buscar_plano, atualizar_plano, deletar_plano
from service.planos_service import validar_descricao, validar_preco
from util.validacoes_util import validar_nome
from model.planos_model import identificar_plano, confirmar_cancelar_plano, selecionar_plano

def menu_plano():
    while True:    
        limpar_tela()

        print("--------------------------------------------\n        Menu Plano\n--------------------------------------------")
        menu = ["Cadastrar Plano", "Listar Planos", "Buscar Plano", "Atualizar Plano", "Deletar Plano", "Voltar"]

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: registrar_plano()
                case 2: 
                    imprimir_planos()
                    if len(listar_planos()) != 0:
                        print("Planos listados com sucesso!")
                case 3: procurar_plano()
                case 4: atualizar_planos()
                case 5: excluir_plano()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def registrar_plano():
    limpar_tela()

    print("--------------------------------------------\n            Cadastrar Plano\n--------------------------------------------")

    # TODO: Talvez fazer que o usuário não pode cadastrar um plano com o mesmo nome que ele já cadastrou anteriormente
    while True:
        nome = input("Digite o nome do plano: ")
        nome_valido = validar_nome(nome)
        if nome_valido:
            break
        else:
            print("Nome muito pequeno! Tente novamente.")

    # TODO: Validar se a descrição for muito grande ou muito pequena
    while True:
        descricao = input("Digite a descrição do plano: ")
        descricao_valida = validar_descricao(descricao)
        if descricao_valida:
            break
        else:
            print("Descrição muito grande! Tente novamente.")

    while True:
        menu = ["Mensal", "Semestral", "Anual"]
        print("--------------------------------------------")
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            id_tipo = int(input("Digite o ID do tipo de plano: "))

            match id_tipo:
                case 1:
                    tipo = "Mensal"
                    break
                case 2:
                    tipo = "Semestral"
                    break
                case 3:
                    tipo = "Anual"
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except Exception as e:
            print("[ERRO]: Digite um número!")

    while True:
        try:
            preco = float(input("Digite o preço do plano: R$ "))
            preco_valido = validar_preco(preco)
            if preco_valido:
                break
            else:
                print("Preço inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    cadastrar_plano(nome, descricao, tipo, preco)

def imprimir_planos():
    quantidade_planos = len(listar_planos())

    if quantidade_planos == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        planos = listar_planos()

        for plano in planos:
            print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")
            print("--------------------------------------------")

def procurar_plano():
    planos = listar_planos()

    if len(planos) == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        # while True:
            nome = input("Digite o nome do plano para buscar: ")
            plano_identificado = identificar_plano(nome, 1)

            if plano_identificado:
                plano_busca = buscar_plano(nome)
                print("--------------------------------------------")
                
                for plano in plano_busca:
                    print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")
                # break
            else:
                print("Nome do plano inválido! Tente novamente.")

def atualizar_planos():
    planos = listar_planos()

    if len(planos) == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        id_plano = selecionar_plano()
        while True:
            limpar_tela()

            print("\n--------------------------------------------\n          Atualizar Plano\n--------------------------------------------")

            menu = ["Nome", "Descrição", "Tipo", "Preço", "Voltar"]
            for i in range(len(menu)):
                print(f"{i + 1} - {menu[i]}")

            try:
                print("--------------------------------------------")
                opcao = int(input("Digite uma opção: "))

                match opcao:
                    case 1:
                        while True:
                            novo_nome = input("Digite o novo nome do plano: ")
                            novo_nome_valido = validar_nome(novo_nome)

                            if novo_nome_valido:
                                atualizar_plano(id_plano, novo_nome, "nome", "Nome")
                                break
                            else:
                                print("Novo nome muito pequeno! Tente novamente.")

                    case 2:
                        while True:
                            nova_descricao = input("Digite a nova descrição do plano: ")
                            nova_descricao_valida = validar_descricao(nova_descricao)

                            if nova_descricao_valida:
                                atualizar_plano(id_plano, nova_descricao, "descricao", "Descrição")
                                break
                            else:
                                print("Nova descrição muito grande! Tente novamente.")

                    case 3:
                        while True:
                            print("--------------------------------------------")
                            menu = ["Mensal", "Semestral", "Anual"]
                            for i in range(len(menu)):
                                print(f"{i + 1} - {menu[i]}")

                            try:
                                print("--------------------------------------------")
                                id_novo_tipo = int(input("Digite o ID do novo tipo de plano: "))

                                match id_novo_tipo:
                                    case 1:
                                        atualizar_plano(id_plano, "Mensal", "tipo", "Tipo")
                                        break
                                    case 2:
                                        atualizar_plano(id_plano, "Semestral", "tipo", "Tipo")
                                        break
                                    case 3:
                                        atualizar_plano(id_plano, "Anual", "tipo", "Tipo")
                                        break
                                    case _:
                                        print("Opção inválida! Tente novamente.")

                            except ValueError:
                                print("[ERRO]: Digite um número!")

                    case 4:
                        while True:
                            try:
                                preco = float(input("Digite o novo preço do plano: "))
                                preco_valido = validar_preco(preco)

                                if preco_valido:
                                    atualizar_plano(id_plano, preco, "preco", "Preço")
                                    break
                                else:
                                    print("Preco inválido! Tente novamente.")

                            except ValueError:
                                print("[ERRO]: Digite um número!")

                    case 5:
                        print("Voltando...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente.")

            except ValueError:
                print("[ERRO]: Digite um número!")

def excluir_plano():
    planos = listar_planos()

    if len(planos) == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        while True:
            print("--------------------------------------------")
            imprimir_planos()

            try:
                id_plano = int(input("Digite o ID do plano para deletar: "))
                plano_identificado = identificar_plano(id_plano, 0)

                if plano_identificado:
                    plano_deletado = confirmar_cancelar_plano(id_plano)

                    if plano_deletado:
                        deletar_plano(id_plano)
                    break

                else:
                    print("ID do plano não cadastrado anteriormente. Tente novamente.")

            except ValueError:
                print("[ERRO]: Digite um número!")