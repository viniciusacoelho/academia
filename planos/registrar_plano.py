from limpar_tela.limpar_tela import limpar_tela
from planos.crud_planos import cadastrar_plano

def registrar_plano():
    while True:
        limpar_tela()

        print("--------------------------------------------\n            Cadastrar Plano\n--------------------------------------------")

        nome = input("Digite o nome do plano: ")
        descricao = input("Digite a descrição do plano: ")

        menu = ["Mensal", "Semestral", "Anual"]
        print("--------------------------------------------\n")
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("\n--------------------------------------------")
            id_tipo = int(input("Digite o ID do tipo de plano: "))

            match id_tipo:
                case 1:
                    tipo = "Mensal"
                    break
                case 2:
                    tipo = "Semestral"
                    break
                case 3:
                    tipo = "Anual"
                    break
                case _:
                    print("Opção inválida!")
            
        except Exception as e:
            print("[ERRO]: Digite um número!")

    while True:
        try:
            preco = float(input("Digite o preço do plano: R$ "))
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

    cadastrar_plano(nome, descricao, tipo, preco)