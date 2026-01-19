from limpar_tela.limpar_tela import limpar_tela
from treinos.registrar_treino import registrar_treino
from treinos.crud_treinos import listar_treinos, buscar_treino, atualizar_treino, deletar_treino

def menu_treino():
    limpar_tela()

    print("--------------------------------------------\n        Menu Treino\n--------------------------------------------")

    menu = ["Cadastrar Treino", "Listar Treinos", "Buscar Treino", "Atualizar Treino", "Deletar Treino", "Voltar"]
    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: registrar_treino()
                case 2:
                    treinos = listar_treinos()
                    print("Treinos listados com sucesso!")
                    for treino in treinos:
                        print(f"Treino {treino[0]}\nExercícios: {treino[1]}\nDescrição: {treino[2]}\nTipo: {treino[3]}\nPreço: {treino[4]}")
                case 3:
                    nome = input("Digite o nome do treino para buscar: ")
                    buscar_treino(nome)

                    treinos = listar_treinos()
                    for treino in treinos:
                        print(f"Treino {treino[0]}\nNome: {treino[1]}\nDescrição: {treino[2]}\nPreço: R$ {treino[3]}")
                case 4:
                    atualizar_treino()
                case 5:
                    listar_treinos()
                    id = int(input("Digite o ID do treino para deletar: "))
                    deletar_treino(id)
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida!")

        except ValueError:
            print("[ERRO]: Digite um número!")