from repository.alunos_repository import listar_alunos

def selecionar_aluno():
    from view.alunos_view.menu_aluno_administrador import imprimir_alunos
    quantidade_alunos = len(listar_alunos())

    if quantidade_alunos == 0:
        print("Nenhum aluno cadastrado anteriormente.")
    else:
        imprimir_alunos()

        try:
            id_aluno = int(input("Digite o ID do aluno para atualizar: "))
            aluno_identificado = identificar_aluno(id_aluno, 0)

            if aluno_identificado:
                return id_aluno
            else:
                return "ID do aluno inválido! Tente novamente."

        except ValueError:
            return "[ERRO]: Digite um número!"

def identificar_aluno(atributo: int, posicao: int) -> bool:
    # TODO: Fazer uma regra para ser de service
    alunos = listar_alunos()
    for aluno in alunos:
        if atributo == aluno[posicao]:
            return True
    return False