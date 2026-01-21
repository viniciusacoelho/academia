from limpar_tela.limpar_tela import limpar_tela
from alunos.atualizar_aluno import atualizar_aluno
from alunos.crud_alunos import deletar_aluno

from banco_de_dados.criar_conexao import criar_conexao

def painel_aluno(aluno_autenticado: list):
    limpar_tela()

    print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")

    menu = ["Visualizar Treinos", "Editar Treino", "Planos", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
    while True:
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: visulizar_treinos(aluno_autenticado)
                case 2: pass
                case 3: pass
                case 4: atualizar_aluno(aluno_autenticado)
                case 5:
                     while True:
                        resposta = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
                        if resposta == "s" or resposta == "sim":
                            deletar_aluno(aluno_autenticado)
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

def treino_aluno(id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treinos WHERE id_aluno = %s", [id_aluno])    
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao visualizar treino de aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def visulizar_treinos(id_aluno: int):
    treinos_alunos = treino_aluno(id_aluno)

    for treinos_aluno in treinos_alunos:
        print(f"Treino {treinos_aluno[0]}\nExercícios: {treinos_aluno[1]}\nDescrição: {treinos_aluno[2]}\nTipo: {treinos_aluno[3]}\nPreço: {treinos_aluno[4]}")