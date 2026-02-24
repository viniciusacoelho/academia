from util.limpar_tela_util import limpar_tela
from view.administrador_view import login_administrador
from view.alunos_view.menu_aluno import menu_aluno
from view.instrutores_view.menu_instrutor import menu_instrutor

while True:
    limpar_tela()

    print("--------------------------------------------\n                  Academia\n--------------------------------------------")
    print("Identifique-se\n")
    menu = ["Administrador", "Aluno", "Instrutor", "Sair"]

    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    try:
        print("--------------------------------------------")
        opcao = int(input("Digite uma opção: "))

        match opcao:
            case 1: login_administrador()
            case 2: menu_aluno()
            case 3: menu_instrutor()
            case 4:
                print("Saindo...")
                limpar_tela()
                print("--------------------------------------------\n                Desenvolvedor\n--------------------------------------------")
                print("LinkedIn: https://www.linkedin.com/in/viniciusacoelho/")
                print("GitHub: https://github.com/viniciusacoelho")
                print("--------------------------------------------")
                break
            case _:
                print("Opção inválida! Tente novamente.")

    except ValueError:
        print("[ERRO]: Digite um número!")