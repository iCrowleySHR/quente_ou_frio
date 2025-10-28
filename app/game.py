from .model.player import Player
from .engine import GameEngine
from .interface import Interface

class HotOrColdGame:
    """Orquestração do jogo."""

    def __init__(self):
        self.player = None
        self.engine = None
        self.io = Interface()

    def start(self):
        """Inicia o jogo."""
        name = self.io.ask_player_name()
        self.player = Player(name)
        digits = self.io.ask_number_of_digits()
        self.engine = GameEngine(digits)

        print("🔢 O número foi gerado! Tente adivinhar:\n")
        self.play()

    def play(self):
        """Loop principal de palpites."""
        self.engine.attempts = 0

        while True:
            guess = self.io.ask_guess()
            result = self.engine.check_guess(guess)
            self.player.register_guess(self.engine.attempts, guess)

            if result == "low":
                print("🔥 Está frio... o número é maior!\n")
            elif result == "high":
                print("❄️ Está frio... o número é menor!\n")
            else:
                print(f"🎉 Parabéns, {self.player.name}! "
                      f"Você acertou o número {self.engine.mysterious_number} "
                      f"em {self.engine.attempts} tentativas.\n")
                break

        self.restart()

    def restart(self):
        """Pergunta se o jogador quer reiniciar."""
        if self.io.ask_restart():
            print("\n🔄 Reiniciando o jogo...\n")
            self.start()
        else:
            print("👋 Obrigado por jogar! Até a próxima!")
