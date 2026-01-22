from limpar_tela.limpar_tela import limpar_tela
from instrutores.atualizar_instrutor import atualizar_instrutor
from instrutores.crud_instrutores import deletar_instrutor
from alunos.crud_alunos import listar_alunos
from treinos.registrar_treino import registrar_treino

def painel_instrutor(instrutor_autenticado: list):
    while True:
    
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")

        menu = ["Criar Treino", "Visualizar Alunos", "Editar Treino", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))
            
            match opcao:
                case 1: criar_treino(instrutor_autenticado)
                case 2: pass
                case 3:
                    alunos = listar_alunos()
                    for aluno in alunos:
                        print(f"{aluno[0]} - {aluno[1]}")
                    id_aluno = int(input("Digite o ID do aluno para editar o treino: "))
                    
                    input("Digite o ID do treino para editar: ")
                case 4: atualizar_instrutor(instrutor_autenticado[0])
                case 5:
                    # TODO: Criar um função disso
                    while True:
                        resposta = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
                        if resposta == "s" or resposta == "sim":
                            deletar_instrutor(instrutor_autenticado[0])
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

def criar_treino(instrutor_autenticado: int):
    alunos = listar_alunos()
    for aluno in alunos:
        print(f"{aluno[0]} - {aluno[1]}")
    id_aluno = int(input("Digite o ID do aluno para criar o treino: "))
    registrar_treino(instrutor_autenticado, id_aluno)