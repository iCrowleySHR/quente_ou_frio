import random

def gerar_numero_misterioso(digitos: int) -> int:
    """Gera um número aleatório de acordo com a quantidade de dígitos."""
    if digitos <= 0:
        raise ValueError("O número de dígitos deve ser maior que zero.")
    
    minimo = 10 ** (digitos - 1)
    maximo = (10 ** digitos) - 1

    if digitos == 1:
        minimo = 0

    return random.randint(minimo, maximo)
