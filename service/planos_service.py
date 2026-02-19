def validar_descricao(descricao: str) -> bool:
    return len(descricao) <= 500

def validar_preco(preco: float) -> bool:
    return preco >= 0