from repository.alunos_repository import listar_alunos
from repository.instrutores_repository import listar_instrutores

from repository.planos_repository import listar_planos
from repository.alunos_repository import listar_alunos
from repository.treinos_repository import listar_treinos
from repository.instrutores_repository import listar_instrutores
from repository.exercicios_repository import listar_exercicios

def validar_unique(parametro_atributo: str, entidade: str, posicao: int):
    if entidade == "alunos":
        itens = listar_alunos()
    elif entidade == "instrutores":
        itens = listar_instrutores()

    lista_intens = []
    for item in itens:
        lista_intens.append(item[posicao])

    return parametro_atributo in lista_intens

# TODO: Verificar se é possível fazer isso
def validar_entidade_cadastrada(entidade: str, nome_entidade: str) -> bool:
    if entidade == "planos":
        quantidade = len(listar_planos())
    elif entidade == "alunos":
        quantidade = len(listar_alunos())
    elif entidade == "treinos":
        quantidade = len(listar_treinos())
    elif entidade == "instrutores":
        quantidade = len(listar_instrutores())
    elif entidade == "exercicios":
        quantidade = len(listar_exercicios())

    if quantidade == 0:
        print(f"Nenhum {nome_entidade} cadastrado anteriormente.")
        return False
    return True