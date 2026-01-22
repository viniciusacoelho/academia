from limpar_tela.limpar_tela import limpar_tela
from alunos.atualizar_aluno import atualizar_aluno
from alunos.crud_alunos import deletar_aluno
from planos.crud_planos import listar_planos
from banco_de_dados.criar_conexao import criar_conexao
from datetime import datetime

def painel_aluno(id_aluno: int):
    while True:
        limpar_tela()

        print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")

        menu = ["Visualizar Treinos", "Editar Treino", "Assinar Plano", "Visualizar Plano", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1: visulizar_treinos(id_aluno)
                case 2: editando_treino(id_aluno)
                case 3: assinar_plano(id_aluno)
                case 4: vizualizar_plano(id_aluno)
                case 5: atualizar_aluno(id_aluno)
                case 6:
                     while True:
                        resposta = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
                        if resposta == "s" or resposta == "sim":
                            deletar_aluno(id_aluno)
                            break
                        elif resposta == "n" or resposta == "não" or resposta == "nao":
                            break
                        else:
                            print("Resposta inválida! Tente novamente.")
                case 7:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
        except ValueError:
            print("[ERRO]: Digite um número!")

def exibir_treino_aluno(id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM treinos WHERE id_aluno = %s ORDER BY id_treino;", [id_aluno])    
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao visualizar treino de aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def visulizar_treinos(id_aluno: int):
    treinos_alunos = exibir_treino_aluno(id_aluno)

    for treinos_aluno in treinos_alunos:
        print(f"Treino {treinos_aluno[0]}\nTipo: {treinos_aluno[1]}\nNome do Exercício: {treinos_aluno[2]}\nPeso: {treinos_aluno[3]}\nRepetições: {treinos_aluno[4]}\nSéries: {treinos_aluno[5]}\nTempo de Descanço: {treinos_aluno[6]}")

def editar_treino_aluno(id_aluno: int, id_treino: int, nome_exercicio: str, parametro_atributo: str | int, atributo: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"UPDATE treinos SET {atributo} = %s WHERE id_treino = %s AND id_aluno = %s AND nome_exercicio = %s;", [parametro_atributo, id_treino, id_aluno, nome_exercicio])    
        conexao.commit()
        print(f"{atributo} de treino atualizado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao atualizar treino: {e}")
    finally:
        cursor.close()
        conexao.close()

def editando_treino(id_aluno: int):
    while True:
        visulizar_treinos(id_aluno)
        try:
            print("--------------------------------------------")
            id_treino = int(input("Digite o ID do treino para editar: "))
            nome_exercicio = input("Digite o nome do exercício para editar: ")
            editar_treino(id_aluno, id_treino, nome_exercicio)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def editar_treino(id_aluno: int, id_treino: int, nome_exercicio: str):
    while True:
        limpar_tela()
    
        print("\n--------------------------------------------\n           Atualizar Treino\n--------------------------------------------")

        menu = ["Editar Nome do Exercício", "Editar Peso", "Editar Repetições", "Editar Séries", "Editar Tempo de Descanço", "Voltar"]
        for i in range(len(menu)):
            print(f"{i + 1} - {menu[i]}")

        try:
            print("--------------------------------------------")
            opcao = int(input("Digite uma opção: "))

            match opcao:
                case 1:
                    novo_nome = input("Digite o novo nome do exercício: ")
                    editar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_nome, "nome_exercicio")
                    break
                case 2:
                    novo_peso = float(input(f"Digite o novo peso do exercício: "))
                    editar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_peso, "peso")
                    break
                case 3:
                    novo_numero_repeticoes = int(input(f"Digite o novo número de repetições do exercício: "))
                    editar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_numero_repeticoes, "repeticoes")
                    break
                case 4:
                    novo_numero_series = int(input(f"Digite a nova quantidade de séries do exercício: "))
                    editar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_numero_series, "series")
                    break
                case 5:
                    novo_tempo_descanso = float(input(f"Digite o novo tempo de descanso do exercício: "))
                    editar_treino_aluno(id_aluno, id_treino, nome_exercicio, novo_tempo_descanso, "tempo_descanso")
                    break
                case 6:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida! Tente novamente.")

        except ValueError:
            print("[ERRO]: Digite um número!")

def plano_aluno(id_aluno: int, id_plano: int, data_hora: datetime, metodo_pagamento: str):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO plano_aluno (id_plano, id_aluno, metodo_pagamento, data_hora) VALUES (%s, %s, %s, %s);", [id_plano, id_aluno, metodo_pagamento, data_hora])    
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

def assinar_plano(id_aluno: int):
    planos = listar_planos()

    for plano in planos:
        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: {plano[4]}")

    while True:
        try:
            id_plano = int(input("Digite o ID do plano para assinar: "))
            metodo_pagamento(id_aluno, id_plano)
            break
        except ValueError:
            print("[ERRO]: Digite um número!")

def metodo_pagamento(id_aluno: int, id_plano: int):
    menu = ["Crédito", "Débito", "Pix", "Dinheiro", "Boleto"]
    for i in range(len(menu)):
        print(f"{i + 1} - {menu[i]}")

    try:
        print("--------------------------------------------")
        opcao = int(input("Digite uma opção: "))

        match opcao:
            case 1: metodo_pagamento = "Crédito"
            case 2: metodo_pagamento = "Débito"
            case 3: metodo_pagamento = "PIX" # TODO: 10% de desconto do PIX
            case 4: metodo_pagamento = "Dinheiro"
            case 5: metodo_pagamento = "Boleto"
            case _:
                print("Opção inválida! Tente novamente.")

    except ValueError:
        print("[ERRO]: Digite um número!")

    data_hora = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    plano_aluno(id_aluno, id_plano, data_hora, metodo_pagamento)

def exibir_plano_aluno(id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT p.id_plano, p.nome, p.descricao, p.tipo, p.preco FROM plano_aluno pa JOIN planos p ON p.id_plano = pa.id_plano WHERE id_aluno = %s;", [id_aluno])    
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()

"""def selecionar_plano_aluno(id_aluno: int):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * WHERE id_aluno = %s;", [id_aluno])    
        conexao.commit()
        print("Aluno cadastrado com sucesso!")
    except Exception as e:
        print(f"[ERRO]: Falha ao cadastrar aluno: {e}")
    finally:
        cursor.close()
        conexao.close()
"""
def vizualizar_plano(id_aluno: int):
    planos = exibir_plano_aluno(id_aluno)
    for plano in planos:
        print(f"Plano {plano[0]}\nNome: {plano[1]}\nDescrição: {plano[2]}\nTipo: {plano[3]}\nPreço: R$ {plano[4]}")
