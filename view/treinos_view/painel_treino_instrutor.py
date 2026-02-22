from util.limpar_tela_util import limpar_tela
from view.treinos_view.menu_treino import registrar_treino
from repository.treinos_repository import listar_treinos, listar_treino_instrutor, atualizar_treino_instrutor, listar_treinos
# from view.exercicios_view.painel_exercicio import painel_exercicio
from repository.treino_exercicio_repository import listar_treino_exercicio, listar_treino_exercicio_join
from model.treinos_model import selecionar_treino

def painel_treino_instrutor(id_instrutor: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel Treino\n--------------------------------------------")
        menu = ["Cadastrar Treino", "Visualizar Treinos", "Editar Treino", "Voltar"]

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: registrar_treino(id_instrutor)
                case 2: visulizar_treinos_instrutor(id_instrutor)
                case 3: editar_treino_instrutor(id_instrutor)
                case 4:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def visulizar_treinos_instrutor(id_instrutor: int):
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        print("--------------------------------------------")
        total_treinos_instrutor = len(listar_treino_instrutor(id_instrutor))

        if total_treinos_instrutor == 0:
            print("Nenhum treino cadastrado à você anteriormente.")
        else:
            treinos_instrutor = listar_treino_instrutor(id_instrutor)

            for treino_instrutor in treinos_instrutor:
                print(f"Treino {treino_instrutor[0]}\nNome: {treino_instrutor[1]}\nTipo: {treino_instrutor[2]}\nAluno: {treino_instrutor[3]}")
                print("Exercícios:")

                if len(listar_treino_exercicio(treino_instrutor[0])) == 0:
                    print("Nenhum exercício cadastrado anteriormente.")
                else:
                    print("--------------------------------------------")
                    exercicios = listar_treino_exercicio_join(treino_instrutor[0])

                    for exercicio in exercicios:
                        print(f"Exercício {exercicio[0]}\nNome: {exercicio[1]}\nQuantidade de séries: {exercicio[2]}\nNúmero de repetições: {exercicio[3]}\nPeso: {exercicio[4]}kg\nTempo de Descanço: {exercicio[5]}")
                        print("--------------------------------------------")
                        
                print("--------------------------------------------")

def editar_treino_instrutor(id_instrutor: int):
    total_treinos = len(listar_treinos())

    if total_treinos == 0:
        print("Nenhum treino cadastrado anteriormente.")
    else:
        total_treinos_instrutor = len(listar_treino_instrutor(id_instrutor))

        if total_treinos_instrutor == 0:
            print("Nenhum treino cadastrado à você anteriormente.")
        else:
            visulizar_treinos_instrutor(id_instrutor)
            id_treino = selecionar_treino()

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
                            atualizar_treino_instrutor(id_instrutor, id_treino, novo_nome, "nome", "Nome")
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
                                        atualizar_treino_instrutor(id_instrutor, id_treino, "Empurrar", "nome", "Nome")
                                        break
                                    case 2:
                                        atualizar_treino_instrutor(id_instrutor, id_treino, "Puxar", "nome", "Nome")
                                        break
                                    case 3:
                                        atualizar_treino_instrutor(id_instrutor, id_treino, "Inferior", "nome", "Nome")
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