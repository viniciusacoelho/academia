from re import match

def validar_nome(nome: str) -> bool:
    # TODO: Fazer validação de se tiver número ou algum caractere especial no nome retornar false
    return len(nome) > 3

def validar_email(email: str) -> bool:
    return match(r"^[\w\d._%+-]{3,}\@{1}[\w\d]{2,}\.{1}[\w\d]{2,}$", email)

def validar_senha(senha: str) -> bool:
    # TODO: Colocar mais segurança -> a senha tem que ter número, letra maiúscula/minúscula, caractere especial etc 
    return len(senha) >= 8