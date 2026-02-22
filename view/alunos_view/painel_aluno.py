from util.limpar_tela_util import limpar_tela
from util.validacoes_util import validar_nome, validar_email, validar_senha
from service.banco_de_dados_service import validar_unique
from service.alunos_service import validar_altura, validar_peso, validar_data_nascimento, formartar_data_nascimento
from util.input_asterisco_util import input_asterisco
from repository.alunos_repository import listar_alunos, atualizar_aluno
from config.criptografia_config import criptografar
from util.confirmar_excluir_conta_util import confirmar_excluir_conta
from model.alunos_model import selecionar_aluno
from view.planos_view.painel_plano import painel_plano
from view.treinos_view.painel_treino_aluno import painel_treino_aluno
from view.exercicios_view.painel_exercicio import painel_exercicio

def painel_aluno(aluno_autenticado: int):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")
        menu = ["Planos", "Treinos", "Exercícios", "Atualizar Cadastro", "Excluir Conta", "Voltar"]

        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: painel_plano(aluno_autenticado[0])
                case 2: painel_treino_aluno(aluno_autenticado[0])
                case 3: painel_exercicio(aluno_autenticado[0], "alunos")
                case 4: editar_aluno(aluno_autenticado[0])
                case 5: confirmar_excluir_conta(aluno_autenticado[0], "alunos")
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def editar_aluno():
    total_alunos = len(listar_alunos())

    if total_alunos == 0:
        print("Nenhum plano cadastrado anteriormente.")
    else:
        id_aluno = selecionar_aluno(id_aluno)
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