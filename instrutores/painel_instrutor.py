from limpar_tela.limpar_tela import limpar_tela
from instrutores.crud_instrutores import listar_aluno_instrutor, atualizar_instrutor
from alunos.crud_alunos import listar_alunos
from treinos.menu_treino import registrar_treino
from treinos.painel_treino import editar_treino
from alunos.painel_aluno import excluir_conta
from alunos.menu_aluno_administrador import imprimir_alunos, identificar_aluno
from instrutores.validar_instrutor import validar_nome, validar_email, validar_cpf, formatar_cpf, validar_senha
from banco_de_dados.validar_banco_de_dados import validar_unique
from msvcrt import getch
from criptografia.criptografar import criptografar
from treinos.painel_treino import painel_treino

def painel_instrutor(instrutor_autenticado: list):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Treino\n--------------------------------------------")
        menu = ["Treinos", "Visualizar Alunos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                # case 1: criar_treino(instrutor_autenticado)
                case 1: painel_treino(instrutor_autenticado)
                case 2: visualizar_alunos(instrutor_autenticado)
                case 3: atualizar_cadastro(instrutor_autenticado)
                case 4: excluir_conta(instrutor_autenticado, "Instrutor")
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def criar_treino(instrutor_autenticado: int):
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        imprimir_alunos()

        try:
            id_aluno = int(input("Digite o ID do aluno para criar o treino: "))
            aluno_identificado = identificar_aluno(id_aluno, 0)

            if aluno_identificado:
                registrar_treino(instrutor_autenticado, id_aluno)
            else:
                print("ID do aluno inválido! Tente novamente.")        
        except ValueError:
            print("[ERRO]: Digite um número!")

def editar_treino_instrutor():
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        alunos = listar_alunos()

        for aluno in alunos:
            print(f"{aluno[0]} - {aluno[1]}")

        try:
            id_aluno = int(input("Digite o ID do aluno para editar o treino: "))
            aluno_identificado = identificar_aluno(id_aluno, 0)

            if aluno_identificado:
                editar_treino(id_aluno)
            else:
                print("ID do aluno inválido! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

def visualizar_alunos(id_instrutor: int):
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        # TODO: Validar se o instrutor está relacionado a algum aluno -> Nenhum aluno 'com seu treino cadastrado' anteriormente.
        alunos = listar_aluno_instrutor(id_instrutor)

        for aluno in alunos:
            print(f"{aluno[0]} - {aluno[1]}")

def atualizar_cadastro(id_instrutor: int):
    while True:
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
                        novo_nome_valido = validar_nome(novo_nome)

                        if novo_nome_valido:
                            atualizar_instrutor(id_instrutor, novo_nome, "nome", "Nome")
                        else:
                            print("Novo nome inválido. Tente novamente.")

                    case 2:
                        novo_email = input("Digite seu novo e-mail: ")
                        novo_email_valido = validar_email(novo_email)

                        if novo_email_valido:
                            email_unico = validar_unique(novo_email, "alunos", 2)

                            if email_unico:
                                atualizar_instrutor(id_instrutor, novo_email, "email", "E-mail")
                            else:
                                print("Novo e-mail já cadastrado anteriormente. Tente novamente.")

                        else:
                            print("E-mail inválido! Tente novamente.")

                    case 3:
                        novo_cpf = input("Digite seu novo CPF: ")

                        try:
                            int(novo_cpf)
                            novo_cpf_valido = validar_cpf(novo_cpf)

                            if novo_cpf_valido:
                                novo_cpf = formatar_cpf(novo_cpf)
                                atualizar_instrutor(id_instrutor, novo_cpf, "cpf", "CPF")
                            else:
                                print("CPF inválido. Tente novamente.")

                        except ValueError:
                            print("[ERRO]: Digite um número!")

                    case 4:
                        # TODO: Colocar o input com asterisco na importação
                        nova_senha = input_asterisco("Digite sua nova senha: ")
                        criptografar(nova_senha)
                        nova_senha_valida = validar_senha(nova_senha)
                        
                        if nova_senha_valida:
                            # TODO: Colocar o input com asterisco na importação
                            confirmar_nova_senha = input_asterisco("Confirme sua nova senha: ")

                            if confirmar_nova_senha == nova_senha:
                                atualizar_instrutor(id_instrutor, nova_senha, "senha", "Senha")
                            else:
                                print("Novas senhas diferentes! Tente novamente.")

                        else:
                            print("Nova_senha inválida! Tente novamente.")

                    case 5:
                        print("Voltando...")
                        break
                    case _:
                        print("Opção inválida! Tente novamente.")

            except ValueError:
                print("[ERRO]: Digite um número!")

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