class Player:
    """Representa o jogador no jogo 'Quente ou Frio'."""

    def __init__(self, name: str):
        self.name = name
        self.guesses = [] 

    def register_guess(self, attempt: int, value: int):
        """Registra um palpite feito pelo jogador."""
        self.guesses.append((attempt, value))
