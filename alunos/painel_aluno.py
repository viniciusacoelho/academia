from limpar_tela.limpar_tela import limpar_tela
from alunos.atualizar_aluno import atualizar_aluno
from alunos.crud_alunos import deletar_aluno

def painel_aluno(aluno_autenticado: list):
    limpar_tela()

    print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")
    menu = ["Visualizar Treino", "Editar Treino", "Planos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: pass
                case 2: pass
                case 3: pass
                case 4: atualizar_aluno(aluno_autenticado[0])
                case 5:
                     while True:
                        resposta = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
                        if resposta == "s" or resposta == "sim":
                            deletar_aluno(aluno_autenticado[0])
                            break
                        elif resposta == "n" or resposta == "não" or resposta == "nao":
                            break
                        else:
                            print("Resposta inválida! Tente novamente.")
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

