from .model.player import Player
from .utils.mysterious_random_number import generate_mysterious_number

class HotOrColdGame:
    """Classe principal do jogo 'Quente ou Frio'."""

    def __init__(self):
        self.player = None
        self.mysterious_number = None
        self.attempts = 0

    def start(self):
        """Inicia o jogo, pedindo nome e número de dígitos."""
        name = input("Olá! Qual é o seu nome? ").strip()
        self.player = Player(name)

        while True:
            try:
                digits = int(input("Quantos dígitos terá o número misterioso? "))
                if digits <= 0:
                    print("Digite um número de dígitos válido (maior que zero).")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

        self.mysterious_number = generate_mysterious_number(digits)
        print("\nO número foi gerado! Tente adivinhar:\n")

        self.play()

    def play(self):
        """Loop principal de tentativas."""
        self.attempts = 0

        while True:
            try:
                guess = int(input("Chute um número: "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            self.attempts += 1
            self.player.register_guess(self.attempts, guess)

            if guess < self.mysterious_number:
                print("O número jogado é menor que o número misterioso.\n")
            elif guess > self.mysterious_number:
                print("O número jogado é maior que o número misterioso.\n")
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
                print("Resposta inválida. Digite 'sim' ou 'não'.")
