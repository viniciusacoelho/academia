# TODO: Validar se há números no nome
def validar_nome(nome: str) -> bool:
    return len(nome) >= 3

def validar_descricao(descricao: str) -> bool:
    return len(descricao) <= 500

def validar_preco(preco: float) -> bool:
    return preco >= 0