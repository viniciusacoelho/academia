from limpar_tela.limpar_tela import limpar_tela
from planos.menu_plano import menu_plano
from alunos.menu_aluno import menu_aluno
from treinos.menu_treino import menu_treino
from instrutores.menu_instrutor import menu_instrutor

def menu_administrador():
    while True:
        limpar_tela()

        print("--------------------------------------------\n              Academia\n--------------------------------------------")

        menu = ["Planos", "Alunos", "Treinos", "Instrutores", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: menu_plano()
                case 2: menu_aluno()
                case 3: menu_treino()
                case 4: menu_instrutor()
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")