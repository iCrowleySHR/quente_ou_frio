from .model.player import Player
from .utils.mysterious_random_number import generate_mysterious_number

class HotOrColdGame:
    """Classe principal do jogo 'Quente ou Frio'."""

    def __init__(self):
        self.player = None
        self.mysterious_number = None
        self.attempts = 0

    def ask_player_name(self) -> Player:
        """Pede o nome do jogador via input, cria o Player e retorna."""
        while True:
            name = input("Olá! Qual é o seu nome? ").strip()
            if name:
                self.player = Player(name)
                print(f"👋 Bem-vindo, {self.player.name}!\n")
                return self.player
            else:
                print("Por favor, digite um nome válido.\n")

    def ask_number_of_digits(self) -> int:
        """Pergunta quantos dígitos terá o número misterioso."""
        while True:
            try:
                digits = int(input("Quantos dígitos terá o número misterioso? "))
                if digits <= 0:
                    print("Digite um número de dígitos válido (maior que zero).\n")
                    continue
                return digits
            except ValueError:
                print("Por favor, digite um número inteiro válido.\n")

    def start(self):
        """Inicia o jogo."""
        self.ask_player_name()
        digits = self.ask_number_of_digits()
        self.mysterious_number = generate_mysterious_number(digits)
        print("🔢 O número foi gerado! Tente adivinhar:\n")
        self.play()

    def play(self):
        """Loop principal de tentativas."""
        self.attempts = 0

        while True:
            try:
                guess = int(input("Chute um número: "))
            except ValueError:
                print("Por favor, digite um número válido.\n")
                continue

            self.attempts += 1
            self.player.register_guess(self.attempts, guess)

            if guess < self.mysterious_number:
                print("🔥 Está frio... o número é maior!\n")
            elif guess > self.mysterious_number:
                print("❄️ Está frio... o número é menor!\n")
            else:
                print(
                    f"🎉 Parabéns, {self.player.name}! "
                    f"Você acertou o número misterioso {self.mysterious_number} "
                    f"em {self.attempts} tentativas.\n"
                )
                break

        self.restart()

    def restart(self):
        """Pergunta se o jogador quer jogar novamente."""
        while True:
            response = input("Quer jogar de novo? (sim/não): ").strip().lower()
            if response in ("sim", "s"):
                print("\n🔄 Reiniciando o jogo...\n")
                self.start()
                break
            elif response in ("não", "nao", "n"):
                print("👋 Obrigado por jogar! Até a próxima!")
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.\n")
