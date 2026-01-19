from limpar_tela.limpar_tela import limpar_tela
from instrutores.criar_conta_instrutor import criar_conta
from instrutores.login_instrutor import login

def menu_instrutores():
    limpar_tela()

    print("--------------------------------------------\n        Menu Plano\n--------------------------------------------")

    menu = ["Criar Conta", "Login", "Voltar"]
    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: criar_conta()
                case 2: login()
                case 3:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida!")
        except ValueError:
            print("[ERRO]: Digite um número!")