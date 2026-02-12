from limpar_tela.limpar_tela import limpar_tela
# from treinos.registrar_treino import registrar_treino
from treinos.crud_treinos import listar_treinos, buscar_treino, atualizar_treino, deletar_treino
from treinos.crud_treinos import cadastrar_treino
from treinos.validar_treino import validar_quantidade_exercicios

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
                case 2: imprimir_treinos()
                case 3: procurar_treino()
                case 4: atualizar_treino()
                case 5: remover_treino()
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")


def registrar_treino(id_instrutor: int, id_aluno: int):
    limpar_tela()

    print("--------------------------------------------\n              Cadastrar Treino\n--------------------------------------------")

    while True:
        menu = ["Empurrar", "Puxar", "Inferior", "Inferior Intermediário"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            id_treino = int(input("Digite o ID do tipo de treino: "))
            
            match id_treino:
                case 1:
                    tipo = "Empurrar"
                    break
                case 2:
                    tipo = "Puxar"
                    break
                case 3:
                    tipo = "Inferior"
                    break
                case 4:
                    tipo = "Inferior Intermediário"
                    break
                case 4:
                    print("ID de treino inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

    while True:
        quantidade_exercicios = int(input("Digite a quantidade de exercícios: "))
        quantidade_exercicios_validada = validar_quantidade_exercicios(quantidade_exercicios)
        if quantidade_exercicios_validada:
            break
        else:
            print("Quantidadde de exercícios inválida! Tente novamente.")

    for i in range(quantidade_exercicios):
        nome_exercicio = input(f"Digite o nome do exercício {i + 1}: ")
        peso = int(input(f"Digite o peso do exercício {i + 1}: "))
        repeticoes = int(input(f"Digite o número de repetições do exercício {i + 1}: "))
        series = int(input(f"Digite a quantidade de séries do exercício {i + 1}: "))
        # TODO: Colocar time no tempo de descanço
        # tempo_descanso = float(input(f"Digite o tempo de descanso do exercício {i + 1}: "))
        tempo_descanso = input(f"Digite o tempo de descanso do exercício {i + 1}: ")

        cadastrar_treino(tipo, nome_exercicio, peso, repeticoes, series, tempo_descanso, id_aluno, id_instrutor)

def imprimir_treinos():
    treinos = listar_treinos()

    for treino in treinos:
        print(f"Treino {treino[0]}\nTipo: {treino[1]}\nExercícios: {treino[2]}\nDescrição: {treino[3]}\nTipo: {treino[4]}\nPreço: {treino[5]}")
        print("--------------------------------------------")

    print("Treinos listados com sucesso!")

def procurar_treino():
    nome = input("Digite o nome do treino para buscar: ")
    treino_busca = buscar_treino(nome)

    # if not nome:
    #     print("Nome do treino inválido! Tente novamente.")

    for treino in treino_busca:
        print(f"Treino {treino[0]}\nTipo: {treino[1]}\nExercícios: {treino[2]}\nDescrição: {treino[3]}\nTipo: {treino[4]}\nPreço: {treino[5]}")

def remover_treino():
    while True:
        treino_aluno = listar_treinos()
    
        if len(treino_aluno) == 0:
            print("Nenhum treino cadastrado anteriormente.")
            break
    listar_treinos()
    id_treino = int(input("Digite o ID do treino para deletar: "))
    deletar_treino(id_treino)