from limpar_tela.limpar_tela import limpar_tela
from planos.registrar_plano import registrar_plano
from planos.crud_planos import listar_planos, buscar_plano, atualizar_plano, deletar_plano
from planos.atualizar_plano import atualizar_plano

def menu_planos():
    limpar_tela()

    print("--------------------------------------------\n        Menu Plano\n--------------------------------------------")

    menu = ["Cadastrar Plano", "Listar Planos", "Buscar Plano", "Atualizar Plano", "Deletar Plano", "Voltar"]

    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: registrar_plano()
                case 2:
                    planos = listar_planos()
                    print("Planos listados com sucesso!")
                    for plano in planos:
                        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: {plano[4]}")
                case 3:
                    nome = input("Digite o nome do plano para buscar: ")
                    buscar_plano(nome)

                    planos = listar_planos()
                    for plano in planos:
                        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nPreço: R$ {plano[3]}")
                case 4:
                    atualizar_plano()
                case 5:
                    listar_planos()
                    id = int(input("Digite o ID do plano para deletar: "))
                    deletar_plano(id)
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida!")
        except ValueError:
            print("[ERRO]: Digite um número!")

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