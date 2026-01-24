from limpar_tela.limpar_tela import limpar_tela
from alunos.crud_alunos import atualizar_aluno

def atualizar_alunoo(id_aluno: list):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n          Atualizar Aluno\n--------------------------------------------")

        menu = ["Editar Nome", "Editar E-mail", "Editar Altura", "Editar Peso", "Editar Data de Nascimento", "Editar Senha", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1:
                    novo_nome = input("Digite seu novo nome: ")
                    atualizar_aluno(id_aluno, novo_nome, "nome")
                case 2:
                    novo_email = input("Digite seu novo e-mail: ")
                    atualizar_aluno(id_aluno, novo_email, "email")
                case 3:
                    nova_altura = float(input("Digite sua nova altura: "))
                    atualizar_aluno(id_aluno, nova_altura, "altura")
                case 4:
                    novo_peso = float(input("Digite seu novo peso: "))
                    atualizar_aluno(id_aluno, novo_peso, "peso")
                case 5:
                    nova_data_nascimento = input("Digite sua nova data de nascimento: ")
                    atualizar_aluno(id_aluno, nova_data_nascimento, "data_nascimento")
                case 6:
                    nova_senha = input("Digite sua nova senha: ")
                    atualizar_aluno(id_aluno, nova_senha, "senha")
                case 7:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")