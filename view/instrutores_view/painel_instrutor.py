from util.limpar_tela_util import limpar_tela
from repository.instrutores_repository import listar_aluno_instrutor, atualizar_instrutor
from repository.alunos_repository import listar_alunos
from view.treinos_view.menu_treino import registrar_treino
from view.treinos_view.painel_treino_aluno import editar_treino_aluno
from util.confirmar_excluir_conta_util import confirmar_excluir_conta
from model.alunos_model import identificar_aluno
from view.alunos_view.menu_aluno_administrador import imprimir_alunos
from service.instrutores_service import validar_cpf, formatar_cpf
from util.validacoes_util import validar_nome, validar_email, validar_senha
from service.banco_de_dados_service import validar_unique
from config.criptografia_config import criptografar
from view.treinos_view.painel_treino_instrutor import painel_treino_instrutor
from util.input_asterisco_util import input_asterisco
from model.instrutores_model import selecionar_instrutor
from view.exercicios_view.painel_exercicio import painel_exercicio

def painel_instrutor(instrutor_autenticado: list):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Instrutor\n--------------------------------------------")
        menu = ["Treinos", "Exercícios", "Visualizar Alunos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: painel_treino_instrutor(instrutor_autenticado[0])
                case 2: painel_exercicio(instrutor_autenticado[0], "instrutores")
                case 3: visualizar_alunos(instrutor_autenticado[0])
                case 4: editar_instrutor(instrutor_autenticado[0])
                case 5: confirmar_excluir_conta(instrutor_autenticado[0], "instrutores")
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def criar_treino(id_instrutor: int):
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        imprimir_alunos()

        try:
            id_aluno = int(input("Digite o ID do aluno para criar o treino: "))
            aluno_identificado = identificar_aluno(id_aluno, 0)

            if aluno_identificado:
                registrar_treino(id_instrutor, id_aluno)
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

def editar_instrutor():
    id_instrutor = selecionar_instrutor()
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
                        nova_senha = input_asterisco("Digite sua nova senha: ")
                        criptografar(nova_senha)
                        nova_senha_valida = validar_senha(nova_senha)
                        
                        if nova_senha_valida:
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