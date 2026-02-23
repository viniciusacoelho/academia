from repository.alunos_repository import listar_alunos

def identificar_aluno(atributo: int, posicao: int) -> bool:
    alunos = listar_alunos()

    for aluno in alunos:
        if atributo == aluno[posicao]:
            return True

    return False

def selecionar_aluno():
    try:
        id_aluno = int(input("Digite o ID do aluno: "))
        aluno_identificado = identificar_aluno(id_aluno, 0)

        if aluno_identificado:
            return id_aluno
        else:
            return "ID do aluno inválido! Tente novamente."

    except ValueError:
        return "[ERRO]: Digite um número!"
