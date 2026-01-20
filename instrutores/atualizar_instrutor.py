from limpar_tela.limpar_tela import limpar_tela
from instrutores.crud_instrutores import atualizar_instrutor

def atualizar_instrutor(id_instrutor: int):
    limpar_tela()

    print("\n--------------------------------------------\n          Atualizar Instrutor\n--------------------------------------------")

    menu = ["Editar Nome", "Editar E-mail", "Editar CPF", "Editar Senha", "Voltar"]
    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1:
                    novo_nome = input("Digite seu novo nome: ")
                    atualizar_instrutor(id_instrutor, novo_nome, "nome")
                case 2:
                    novo_email = input("Digite seu novo e-mail: ")
                    atualizar_instrutor(id_instrutor, novo_email, "email")
                case 3:
                    novo_cpf = input("Digite sua novo CPF: ")
                    atualizar_instrutor(id_instrutor, novo_cpf, "cpf")
                case 4:
                    nova_senha = float(input("Digite sua nova senha: "))
                    atualizar_instrutor(id_instrutor, nova_senha, "senha")
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")