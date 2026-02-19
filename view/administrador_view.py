from util.limpar_tela_util import limpar_tela
from view.planos_view.menu_plano import menu_plano
from view.treinos_view.menu_treino import menu_treino
from view.exercicios_view.menu_exercicio import menu_exercicio
from view.instrutores_view.menu_instrutor_administrador import menu_instrutor_administrador
from view.alunos_view.menu_aluno_administrador import menu_aluno_administrador
from util.input_asterisco_util import input_asterisco

def menu_administrador():
    while True:
        limpar_tela()

        print("--------------------------------------------\n              Academia\n--------------------------------------------")
        print("Dashboard\n")
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

def login_administrador():
    SENHA_ACESSO = "1234"

    while True:
        limpar_tela()

        print("--------------------------------------------\n                   Login\n--------------------------------------------")
        senha = input_asterisco("Digite a senha de acesso: ")

        if senha == SENHA_ACESSO:
            print("Login realizado com sucesso! Seja bem-vindo(a)!")
            menu_administrador()
            break
        else:
            print("Senha de acesso inválida! Tente novamente.")