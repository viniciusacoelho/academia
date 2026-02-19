from util.limpar_tela_util import limpar_tela
from repository.treinos_repository import listar_treinos, listar_treino_aluno, atualizar_treino_aluno, listar_treinos
from view.exercicios_view.painel_exercicio import painel_exercicio
from view.treinos_view.menu_treino import registrar_treino, identificar_treino
from view.exercicios_view.menu_exercicio import imprimir_exercicios
from repository.treino_exercicio_repository import listar_treino_exercicio, listar_treino_exercicio_join

def painel_treino(id_aluno: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel Treino\n--------------------------------------------")
        menu = ["Cadastrar Treino", "Visualizar Treinos", "Editar Treino", "Exercícios", "Voltar"]

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: registrar_treino()
                case 2:
                    if len(listar_treino_aluno(id_aluno)) != 0:
                        visulizar_treinos_aluno(id_aluno)
                        print("Treinos listados com sucesso!")
                case 3: editar_treino_aluno(id_aluno)
                case 4: painel_exercicio(id_aluno)
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def visulizar_treinos_aluno(id_aluno: int):
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        total_treinos_aluno = len(listar_treino_aluno(id_aluno))

        if total_treinos_aluno == 0:
            print("Nenhum treino cadastrado à você anteriormente.")
        else:
            treinos_aluno = listar_treino_aluno(id_aluno)
            
            for treino_aluno in treinos_aluno:
                print(f"Treino {treino_aluno[0]}\nNome: {treino_aluno[1]}\nTipo: {treino_aluno[2]}")
                print("Exercícios:")
                
                if len(listar_treino_exercicio(treino_aluno[0])) == 0:
                    print("Nenhum exercício cadastrado anteriormente.")
                else:
                    pass
                print(f"Instrutor: {treino_aluno[3]}")
                print("--------------------------------------------")

    for i in range(len(listar_treino_exercicio(treino_aluno[0]))):
        exercicios = listar_treino_exercicio_join(treino_aluno[0])
        for exercicio in exercicios:
            print(f"Exercício {exercicio[0]}\nNome: {exercicio[1]}\nQuantidade de séries: {exercicio[2]}\nNúmero de repetições: {exercicio[3]}\nPeso: {exercicio[4]}kg\nTempo de Descanço: {exercicio[5]}")
            print("--------------------------------------------")

def visulizar_treinos_instrutor(id_aluno: int):
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        total_treinos_aluno = len(listar_treino_aluno(id_aluno))

        if total_treinos_aluno == 0:
            print("Nenhum treino cadastrado à você anteriormente.")
        else:
            treinos_aluno = listar_treino_aluno(id_aluno)
            
            for treino_aluno in treinos_aluno:
                print(f"Treino {treino_aluno[0]}\nNome: {treino_aluno[1]}\nTipo: {treino_aluno[2]}")
                print("Exercícios:")
                
                if len(listar_treino_exercicio(treino_aluno[0])) == 0:
                    print("Nenhum exercício cadastrado anteriormente.")
                else:
                    for i in range(len(listar_treino_exercicio(treino_aluno[0]))):
                        exercicios = listar_treino_exercicio_join(treino_aluno[0])
                        for exercicio in exercicios:
                            print(f"Exercício {exercicio[0]}\nNome: {exercicio[1]}\nQuantidade de séries: {exercicio[2]}\nNúmero de repetições: {exercicio[3]}\nPeso: {exercicio[4]}kg\nTempo de Descanço: {exercicio[5]}")
                            print("--------------------------------------------")
                print(f"Instrutor: {treino_aluno[3]}")
                print("--------------------------------------------")

def editar_treino_aluno(id_aluno: int):
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        total_treinos_aluno = len(listar_treino_aluno(id_aluno))

        if total_treinos_aluno == 0:
            print("Nenhum treino cadastrado à você anteriormente.")
        else:
            id_treino = selecionar_treino(id_aluno)

            while True:
                limpar_tela()
            
                print("\n--------------------------------------------\n           Atualizar Treino\n--------------------------------------------")
                menu = ["Nome do Treino", "Tipo do Treino", "Voltar"]

                for i in range(len(menu)):
                    print(f"{i + 1} - {menu[i]}")

                try:
                    print("--------------------------------------------")
                    opcao = int(input("Digite uma opção: "))

                    match opcao:
                        case 1:
                            novo_nome = input("Digite o novo nome do treino: ")
                            atualizar_treino_aluno(id_aluno, id_treino, novo_nome, "nome", "Nome")
                            break
                        case 2:
                            menu = ["Empurrar", "Puxar", "Inferior"]
                            for i in range(len(menu)):
                                print(f"{i + 1} - {menu[i]}")

                            try:
                                print("--------------------------------------------")
                                id_tipo_treino = int(input("Digite o ID do novo tipo de treino: "))
                                
                                match id_tipo_treino:
                                    case 1:
                                        atualizar_treino_aluno(id_aluno, id_treino, "Empurrar", "nome", "Nome")
                                        break
                                    case 2:
                                        atualizar_treino_aluno(id_aluno, id_treino, "Puxar", "nome", "Nome")
                                        break
                                    case 3:
                                        atualizar_treino_aluno(id_aluno, id_treino, "Inferior", "nome", "Nome")
                                        break
                                    case _:
                                        print("ID do tipo de treino inválido! Tente novamente.")

                            except ValueError:
                                print("[ERRO]: Digite um número!")

                        case 3:
                            print("Voltando...")
                            break
                        case _:
                            print("Opção inválida! Tente novamente.")

                except ValueError:
                    print("[ERRO]: Digite um número!")

def selecionar_treino(id_aluno: int):
    visulizar_treinos_aluno(id_aluno)

    try:
        print("--------------------------------------------")
        id_treino = int(input("Digite o ID do treino para editar: "))
        treino_identificado = identificar_treino(id_treino, 0)

        if treino_identificado:
            return id_treino
        else:
            print("ID do treino inválido! Tente novamente.")

    except ValueError:
        print("[ERRO]: Digite um número!")