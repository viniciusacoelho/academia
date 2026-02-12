from limpar_tela.limpar_tela import limpar_tela
# from planos.registrar_plano import registrar_plano
from planos.crud_planos import listar_planos, buscar_plano, atualizar_plano, deletar_plano
# from planos.atualizar_plano import atualizar_plano
from planos.crud_planos import cadastrar_plano
from planos.validar_plano import validar_nome, validar_descricao, validar_preco

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
    while True:
        limpar_tela()

        print("--------------------------------------------\n            Cadastrar Plano\n--------------------------------------------")

        # TODO: Talvez fazer que o usuário não pode cadastrar um plano com o mesmo nome que ele já cadastrou anteriormente
        while True:
            nome = input("Digite o nome do plano: ")
            nome_validado = validar_nome(nome)
            if nome_validado:
                break
            else:
                print("Nome muito pequeno! Tente novamente.")

        # TODO: Validar se a descrição for muito grande ou muito pequena
        while True:
            descricao = input("Digite a descrição do plano: ")
            descricao_validada = validar_descricao(descricao)
            if descricao_validada:
                break
            else:
                print("Descrição muito grande! Tente novamente.")

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
                    print("Opção inválida!")

        except Exception as e:
            print("[ERRO]: Digite um número!")

    while True:
        try:
            preco = float(input("Digite o preço do plano: R$ "))
            preco_validado = validar_preco(preco)
            if preco_validado:
                break
            else:
                print("Preco inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    cadastrar_plano(nome, descricao, tipo, preco)

def imprimir_planos():
    planos = listar_planos()

    for plano in planos:
        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")
        print("--------------------------------------------")

def procurar_plano():
    nome = input("Digite o nome do plano para buscar: ")
    plano_busca = buscar_plano(nome)

    for plano in plano_busca:
        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")

def atualizar_planos():
    id_plano = selecionar_plano()
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n          Atualizar Plano\n--------------------------------------------")

        menu = ["Nome", "Descrição", "Tipo", "Preço", "Voltar"]
        while True:
            for i in range(len(menu)):
                print(f"{i + 1} - {menu[i]}")

            try:
                print("--------------------------------------------")
                opcao = int(input("Digite uma opção: "))

                match opcao:
                    case 1:
                        nome = input("Digite o novo nome do plano: ")
                        atualizar_plano(id_plano, nome, "nome", "Nome")
                    case 2:
                        descricao = input("Digite a nova descrição do plano: ")
                        atualizar_plano(id_plano, descricao, "descricao", "Descrição")
                    case 3:
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
                        try:
                            preco = float(input("Digite o novo preço do plano: "))
                            atualizar_plano(id_plano, preco, "preco", "Preço")
                        except ValueError:
                            print("[ERRO]: Digite um número!")
                    case 5:
                        print("Voltando...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente.")

            except ValueError:
                print("[ERRO]: Digite um número!")

def selecionar_plano():
    while True:
        imprimir_planos()

        try:
            id_plano = int(input("Digite o ID do plano para atualizar: "))

            plano_identificado = identificar_plano(id_plano)
            if plano_identificado:
                atualizar_plano(id_plano)
                break
            else:
                print("ID do plano não cadastrado anteriormente. Tente novamente.")

            # planos = listar_planos()
            # for plano in planos:
            #     if id_plano == plano[0]:
            #         return id_plano
            # else:
            #     print("ID do plano não cadastrado anteriormente. Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def excluir_plano():
    while True:
        imprimir_planos()

        try:
            id_plano = int(input("Digite o ID do plano para deletar: "))
            plano_identificado = identificar_plano(id_plano)
            
            if plano_identificado:
                deletar_plano(id_plano)
                break
            else:
                print("ID do plano não cadastrado anteriormente. Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")  

def identificar_plano(id_plano: int):
    planos = listar_planos()
    for plano in planos:
        if id_plano == plano[0]:
            return True
    return False

"""
    Planos de academia variam por duração (mensal, semestral, anual), frequência 
    (dias por semana, horários), acesso (uma unidade ou rede) e inclusões (aulas, 
    personal, apps), com opções como planos recorrentes (pagamento automático), 
    pacotes corporativos (TotalPass, Wellhub/Gympass) e modalidades como 
    musculação, funcional, dança, yoga e artes marciais, oferecendo flexibilidade e 
    diferentes custos, sendo os mais longos geralmente mais econômicos. 
    
    Tipos Comuns de Planos:
        Mensal/Semestral/Anual: Contratos com durações definidas, sendo os mais 
        longos mais baratos por mês.
        Recorrente: Cobrança automática a cada 30 dias, sem fidelidade fixa.
        Por Frequência: Pacotes com limite de visitas por semana ou mês, comum em 
        academias premium.
        Corporativo (Wellhub/Gympass, TotalPass): Benefícios oferecidos por empresas, 
        dando acesso a diversas academias e estúdios com mensalidade reduzida. 
    
    O Que Verificar ao Escolher:
        Localização e Acesso: Verifique se a academia tem unidades perto de você ou em 
        locais que você frequenta.
        Infraestrutura e Modalidades: Veja se oferece musculação, aulas (yoga, dança, 
        fitdance, muay thai), crossfit, etc., e se o espaço atende suas necessidades.
        Horários: Confirme se os horários de funcionamento e das aulas batem com sua 
        rotina.
        Inclusões Extras: Alguns planos incluem acesso a apps de bem-estar, nutricionista, 
        personal trainer ou acompanhante.
        Custo-Benefício: Compare o preço com a liberdade de horários, número de 
        unidades e extras incluídos. 
    
    Exemplos em Maceió:
        Selfit: Plano Plus sem fidelidade/anuidade, com acesso a todas as unidades e app, 
        a partir de R$99,90.
        BG Fitness: Variações como BG Gold e Platinum, com preços diferentes por 
        unidade e adesão, em Maceió.
        Wellhub (Gympass): Permite acesso a várias academias como Korpus, DS Fitness, 
        Academia CAM, etc., via benefício corporativo. 
    
    Para escolher o melhor, visite a academia, converse sobre as opções e veja qual se 
    encaixa melhor nos seus objetivos e orçamento!. 
"""