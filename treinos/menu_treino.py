from limpar_tela.limpar_tela import limpar_tela
from treinos.registrar_treino import registrar_treino
from treinos.crud_treinos import listar_treinos, buscar_treino, atualizar_treino, deletar_treino

def menu_treino():
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Menu Treino\n--------------------------------------------")

        menu = ["Cadastrar Treino", "Listar Treinos", "Buscar Treino", "Atualizar Treino", "Deletar Treino", "Voltar"]
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
                        print(f"Treino {treino[0]}\nTipo: {treino[1]}\nExercícios: {treino[2]}\nDescrição: {treino[3]}\nTipo: {treino[4]}\nPreço: {treino[5]}")
                case 3:
                    nome = input("Digite o nome do treino para buscar: ")
                    buscar_treino(nome)

                    treinos = listar_treinos()
                    for treino in treinos:
                        print(f"Treino {treino[0]}\nTipo: {treino[1]}\nExercícios: {treino[2]}\nDescrição: {treino[3]}\nTipo: {treino[4]}\nPreço: {treino[5]}")
                case 4: atualizar_treino()
                case 5:
                    listar_treinos()
                    id_treino = int(input("Digite o ID do treino para deletar: "))
                    deletar_treino(id_treino)
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")