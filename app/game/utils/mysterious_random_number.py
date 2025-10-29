import random

def generate_mysterious_number(digits: int) -> int:
    """Gera um número aleatório com base na quantidade de dígitos informada."""
    if digits <= 0:
        raise ValueError("O número de dígitos deve ser maior que zero.")

    min_value = 10 ** (digits - 1)
    max_value = (10 ** digits) - 1

    # Caso especial: 1 dígito → de 0 a 9
    if digits == 1:
        min_value = 0

    return random.randint(min_value, max_value)
