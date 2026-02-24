from re import match

def validar_altura(altura: float) -> bool:
    return match(r"^\d{1}.{1}\d{,2}$", altura)

def validar_peso(peso: float) -> bool:
    # return match(r"^\d{1}.{1}\d{,2}$", peso)
    # return len(peso) >= 2
    return peso >= 10

def validar_data_nascimento(data_nascimento: float) -> bool:
    return len(data_nascimento) == 8

def formartar_data_nascimento(data_nascimento: float) -> bool:
    return f"{data_nascimento[4:8]}-{data_nascimento[2:4]}-{data_nascimento[:2]}"