def validar_nome(nome: str) -> bool:
    return len(nome) >= 3

def validar_quantidade_series(quantidade_series: int) -> bool:
    return quantidade_series >= 0 and quantidade_series <= 100

def validar_peso(peso: int) -> bool:
    return peso >= 0 and peso <= 2000

def validar_numero_repeticoes(numero_repeticoes: int) -> bool:
    return numero_repeticoes >= 0 and numero_repeticoes <= 500

def validar_tempo_descanso(tempo_descanso: int) -> bool:
    return tempo_descanso >= 0 and tempo_descanso <= 60

