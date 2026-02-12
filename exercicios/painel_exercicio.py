from limpar_tela.limpar_tela import limpar_tela
from exercicios.crud_exercicio import listar_exercicios, cadastrar_exercicio_aluno, listar_exercicio_aluno, deletar_exercicio_aluno
from pagamento.pagamento import pagamento
from exercicios.menu_exercicio import imprimir_exercicios
from treinos.menu_treino import imprimir_treinos

def painel_exercicio(id_aluno: int):
    while True:
        limpar_tela()

        print("--------------------------------------------\n        Painel exercicio\n--------------------------------------------")

        menu = ["Adicionar Exercício", "Remover Exercício", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: visualizar_exercicio(id_aluno)
                case 2: adicionar_exercicio(id_aluno)
                case 3: remover_exercicio(id_aluno)
                case 4:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def visualizar_exercicio(id_aluno: int):
    exercicio_aluno = listar_exercicio_aluno(id_aluno)

    if len(exercicio_aluno) == 0:
        print("Nenhum exercicio escolhido anteriormente.")
    else:
        exercicios = listar_exercicio_aluno(id_aluno)

        for exercicio in exercicios:
            print(f"exercicio {exercicio[0]}\nNome: {exercicio[1]}\nDescrição: {exercicio[2]}\nTipo: {exercicio[3]}\nPreço: R$ {exercicio[4]}")

def adicionar_exercicio(id_aluno: int, id_treino: int):
    while True:
        exercicio_aluno = listar_exercicio_aluno(id_aluno)
        if len(exercicio_aluno) == 1:
            print("exercicio já assinado anteriormente.")
            break

        total_exercicios = listar_exercicios()

        if len(total_exercicios) > 0:
            while True:
                # imprimir_treinos(id_treino)

                try:
                    id_treino = int(input("Digite o ID do treino para adicionar exercício: "))
                    
                    break
                except ValueError:
                    print("[ERRO]: Digite um número!")
            break

        else:
            print("Nenhum exercicio cadastrado anteriormente.")
            break

def remover_exercicio(id_aluno: int):
    # TODO: Talvez transformar em função:
    while True:
        exercicio_aluno = listar_exercicio_aluno(id_aluno)
    
        if len(exercicio_aluno) == 0:
            print("Nenhum exercicio assinado anteriormente.")
            break

        visualizar_exercicio(id_aluno)

        try:
            id_exercicio = int(input("Digite o ID do exercicio para cancelar: "))
            confirmar_cancelar_exercicio(id_exercicio, id_aluno)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def confirmar_cancelar_exercicio(id_exercicio: int, id_aluno: int):
    while True:
        resposta = input("Tem certeza que deseja cancelar seu exercicio? (s/n): ").lower()

        if resposta == "s" or resposta == "sim":
            deletar_exercicio_aluno(id_exercicio, id_aluno)
            break
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            break
        else:
            print("Resposta inválida! Tente novamente.")