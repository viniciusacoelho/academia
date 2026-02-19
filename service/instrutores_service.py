def validar_cpf(cpf: str) -> bool:
    return len(cpf) == 11

def formatar_cpf(cpf: str) -> str:
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"