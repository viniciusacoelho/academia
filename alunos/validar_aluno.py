from re import match

def validar_nome(nome: str):
    return len(nome) > 3

def validar_email(email: str):
    return match(r"^[\w\d._%+-]{3,}\@{1}[\w\d]{2,}\.{1}[\w\d]{2,}$", email)

def validar_altura(altura: float):
    return match(r"^\d{1}.{1}\d{,2}$", altura)

def validar_peso(peso: float):
    # return match(r"^\d{1}.{1}\d{,2}$", peso)
    return len(peso) == 2

