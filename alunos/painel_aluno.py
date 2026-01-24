from limpar_tela.limpar_tela import limpar_tela
from planos.painel_plano import painel_plano
from treinos.painel_treino import painel_treino
from alunos.atualizar_aluno import atualizar_aluno
from alunos.crud_alunos import deletar_aluno
from criptografia.criptografar import criptografar
from instrutores.crud_instrutores import deletar_instrutor

def painel_aluno(id_aluno: int):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")

        menu = ["Planos", "Treinos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: painel_plano(id_aluno)
                case 2: painel_treino(id_aluno)
                case 3: atualizar_cadastro(id_aluno)
                case 4: excluir_conta(id_aluno, "Aluno")
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def atualizar_cadastro(id_aluno: int):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n          Atualizar Cadastro\n--------------------------------------------")

        menu = ["Editar Nome", "Editar E-mail", "Editar Altura", "Editar Peso", "Editar Data de Nascimento", "Editar Senha", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1:
                    novo_nome = input("Digite seu novo nome: ")
                    atualizar_aluno(id_aluno, novo_nome, "nome", "Nome")
                case 2:
                    novo_email = input("Digite seu novo e-mail: ")
                    atualizar_aluno(id_aluno, novo_email, "email", "E-mail")
                case 3:
                    nova_altura = float(input("Digite sua nova altura: "))
                    atualizar_aluno(id_aluno, nova_altura, "altura", "Altura")
                case 4:
                    novo_peso = float(input("Digite seu novo peso: "))
                    atualizar_aluno(id_aluno, novo_peso, "peso", "Peso")
                case 5:
                    nova_data_nascimento = input("Digite sua nova data de nascimento: ")
                    atualizar_aluno(id_aluno, nova_data_nascimento, "data_nascimento", "Data de nascimento")
                case 6:
                    nova_senha = input("Digite sua nova senha: ")
                    criptografar(nova_senha)
                    atualizar_aluno(id_aluno, nova_senha, "senha", "Senha")
                case 7:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def excluir_conta(id: int, entidade: str):
    while True:
        resposta = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
        if resposta == "s" or resposta == "sim":
            if entidade == "Aluno":
                deletar_aluno(id)
            elif entidade == "Instrutor":
                deletar_instrutor(id)
            break
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            break
        else:
            print("Resposta inválida! Tente novamente.")