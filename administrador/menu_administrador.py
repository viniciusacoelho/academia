from limpar_tela.limpar_tela import limpar_tela
from planos.menu_plano import menu_plano
from alunos.menu_aluno_administrador import menu_aluno_administrador
from treinos.menu_treino import menu_treino
from instrutores.menu_instrutor_administrador import menu_instrutor_administrador
from exercicios.menu_exercicio import menu_exercicio

def menu_administrador():
    while True:
        limpar_tela()

        print("--------------------------------------------\n              Academia\n--------------------------------------------")

        menu = ["Planos", "Treinos", "Exercícios", "Instrutores", "Alunos", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: menu_plano()
                case 2: menu_treino()
                case 3: menu_exercicio()
                case 4: menu_instrutor_administrador()
                case 5: menu_aluno_administrador()
                case 6: 
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")