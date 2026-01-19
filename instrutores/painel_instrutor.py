from limpar_tela.limpar_tela import limpar_tela

def painel_aluno(professor_autenticado: list):
    limpar_tela()

    print("\n--------------------------------------------\n            Painel Aluno\n--------------------------------------------")
    menu = ["Visualizar Alunos", "Criar Treino", "Editar Treino", "Atualizar Cadastro", "Excluir Conta", "Voltar"]
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
                case 4: pass
                case 5:
                    print("Voltando...")
                    break
                case _:
                    print("Opção inválida!")
        except ValueError:
            print("[ERRO]: Digite um número!")