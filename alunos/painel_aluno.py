from limpar_tela.limpar_tela import limpar_tela
from planos.painel_plano import painel_plano
from treinos.painel_treino import painel_treino
from alunos.crud_alunos import atualizar_aluno, deletar_aluno
from criptografia.criptografar import criptografar
from instrutores.crud_instrutores import deletar_instrutor
from alunos.validar_aluno import validar_nome, validar_email, validar_altura, validar_peso, validar_data_nascimento, formartar_data_nascimento, validar_senha
from banco_de_dados.validar_banco_de_dados import validar_unique
# TODO: Colocar o input com asterisco
# from alunos.menu_aluno import input_asterisco
from msvcrt import getch

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
                    nome_valido = validar_nome(novo_nome)
                    
                    if nome_valido:
                        atualizar_aluno(id_aluno, novo_nome, "nome", "Nome")
                    else:
                        print("Novo nome inválido! Tente novamente.")

                case 2:
                    novo_email = input("Digite seu novo e-mail: ")
                    novo_email_valido = validar_email(novo_email)

                    if novo_email_valido:
                        email_unico = validar_unique(novo_email, "alunos", 2)

                        if email_unico:
                            atualizar_aluno(id_aluno, novo_email, "email", "E-mail")
                        else:
                            print("Novo e-mail já cadastrado anteriormente. Tente novamente.")

                    else:
                        print("E-mail inválido! Tente novamente.")

                case 3:
                    try:
                        nova_altura = float(input("Digite sua nova altura: "))
                        nova_altura_valida = validar_altura(str(nova_altura))
                        
                        if nova_altura_valida:
                            atualizar_aluno(id_aluno, nova_altura, "altura", "Altura")
                        else:
                            print("Nova altura inválida! Tente novamente.")
                    except ValueError:
                        print("[ERRO]: Digite um número!")

                case 4:
                    try:
                        novo_peso = float(input("Digite seu novo peso: "))
                        novo_peso_valido = validar_peso(novo_peso)
                        
                        if novo_peso_valido:
                            atualizar_aluno(id_aluno, novo_peso, "peso", "Peso")
                        else:
                            print("Novo peso inválido! Tente novamente.")
                    except ValueError:
                        print("[ERRO]: Digite um número!")

                case 5:
                    nova_data_nascimento = input("Digite sua nova data de nascimento: ")

                    try:
                        int(nova_data_nascimento)
                        data_nascimento_valida = validar_data_nascimento(nova_data_nascimento)

                        if data_nascimento_valida:
                            nova_data_nascimento = formartar_data_nascimento(nova_data_nascimento)
                            atualizar_aluno(id_aluno, nova_data_nascimento, "data_nascimento", "Data de nascimento")
                        else:
                            print("Nova data de nascimento inválida! Tente novamente.")
                    except ValueError:
                        print("[ERRO]: Digite um número!")

                case 6:
                    # TODO: Colocar o input com asterisco na importação
                    nova_senha = input_asterisco("Digite sua nova senha: ")
                    criptografar(nova_senha)
                    nova_senha_valida = validar_senha(nova_senha)
                    
                    if nova_senha_valida:
                        # TODO: Colocar o input com asterisco na importação
                        confirmar_nova_senha = input_asterisco("Confirme sua nova senha: ")

                        if confirmar_nova_senha == nova_senha:
                            atualizar_aluno(id_aluno, nova_senha, "senha", "Senha")
                        else:
                            print("Novas senhas diferentes! Tente novamente.")

                    else:
                        print("Nova_senha inválida! Tente novamente.")

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

def input_asterisco(mensagem=""):
    print(mensagem, end="", flush=True)
    senha = ""

    while True:
        char = getch()

        if char in {b'\r', b'\n'}:  # Enter
            print()
            break
        elif char == b'\x08':  # Backspace
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        else:
            senha += char.decode("UTF-8")
            print("*", end="", flush=True)

    return senha