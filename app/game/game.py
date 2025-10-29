from .model.player import Player
from .engine import GameEngine
from ..interface.interface import Interface  

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

        self.io.show_message("🔢 O número foi gerado! Tente adivinhar!")
        self.play()

    def play(self):
        """Loop principal de palpites."""
        self.engine.attempts = 0

        while True:
            guess = self.io.ask_guess()
            result = self.engine.check_guess(guess)
            self.player.register_guess(self.engine.attempts, guess)

            if result == "low":
                self.io.show_message("🔥 Está frio... o número é MAIOR!")
            elif result == "high":
                self.io.show_message("❄️ Está frio... o número é MENOR!")
            else:
                self.io.show_message(
                    f"🎉 Parabéns, {self.player.name}!\n"
                    f"Você acertou o número {self.engine.mysterious_number} "
                    f"em {self.engine.attempts} tentativas!"
                )
                break

        self.restart()

    def restart(self):
        """Pergunta se o jogador quer reiniciar."""
        if self.io.ask_restart():
            self.start()
        else:
            self.io.show_message("👋 Obrigado por jogar! Até a próxima!")
            self.io.root.after(2000, self.io.close)
