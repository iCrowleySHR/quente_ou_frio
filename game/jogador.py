class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.palpites = []  

    def registrar_palpite(self, tentativa: int, valor: int):
        """Registra o palpite do jogador."""
        self.palpites.append((tentativa, valor))
