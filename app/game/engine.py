from .utils.mysterious_random_number import generate_mysterious_number

class GameEngine:
    """Lógica principal do jogo."""

    def __init__(self, digits: int):
        self.mysterious_number = generate_mysterious_number(digits)
        self.attempts = 0

    def check_guess(self, guess: int) -> str:
        """Verifica se o palpite está correto, maior ou menor."""
        self.attempts += 1
        if guess < self.mysterious_number:
            return "low"
        elif guess > self.mysterious_number:
            return "high"
        else:
            return "correct"
