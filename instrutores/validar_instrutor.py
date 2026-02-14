from re import match

def validar_nome(nome: str) -> bool:
    # TODO: Fazer validação de se tiver número ou algum caractere especial no nome retornar false
    return len(nome) > 3

def validar_email(email: str) -> bool:
    return match(r"^[\w\d._%+-]{3,}\@{1}[\w\d]{2,}\.{1}[\w\d]{2,}$", email)

def validar_cpf(cpf: str) -> bool:
    return len(cpf) == 11

def formatar_cpf(cpf: str) -> str:
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def validar_senha(senha: str) -> bool:
    return len(senha) >= 8