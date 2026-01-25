from alunos.crud_alunos import listar_alunos
from instrutores.crud_instrutores import listar_instrutores

def validar_unique(parametro_atributo: str, entidade: str, posicao: int):
    if entidade == "alunos":
        itens = listar_alunos()
    elif entidade == "instrutores":
        itens = listar_instrutores()

    lista_intens = []
    for item in itens:
        lista_intens.append(item[posicao])

    return parametro_atributo in lista_intens