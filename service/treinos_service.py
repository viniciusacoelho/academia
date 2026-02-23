def validar_nome(nome: int) -> bool:
    return len(nome) >= 3

def validar_quantidade_exercicios(quantidade_exercicios: int) -> bool:
    return quantidade_exercicios >= 0 and quantidade_exercicios <= 50