from re import match

def validar_nome(nome: str) -> bool:
    return len(nome) > 3

def validar_email(email: str) -> bool:
    return match(r"^[\w\d._%+-]{3,}\@{1}[\w\d]{2,}\.{1}[\w\d]{2,}$", email)

def validar_altura(altura: float) -> bool:
    return match(r"^\d{1}.{1}\d{,2}$", altura)

def validar_peso(peso: float) -> bool:
    # return match(r"^\d{1}.{1}\d{,2}$", peso)
    return len(peso) == 2

def validar_data_nascimento(data_nascimento: float) -> bool:
    # return match(r"^\d{1}.{1}\d{,2}$", data_nascimento)
    return len(data_nascimento) == 8

def formartar_data_nascimento(data_nascimento: float) -> bool:
    return f"{data_nascimento[4:8]}-{data_nascimento[2:4]}-{data_nascimento[:2]}"

def validar_senha(senha: str) -> bool:
    # TODO: Colocar mais segurança -> a senha tem que ter número, letra maiúscula/minúscula, caractere especial etc 
    return len(senha) >= 8