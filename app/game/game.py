from .model.player import Player
from .engine import GameEngine
from ..interface.interface import Interface
from ..interface.style import colors

class HotOrColdGame:
    """Orquestração do jogo."""

    def __init__(self):
        self.player = None
        self.engine = None
        self.io = Interface()

    def start(self):
        """Inicia o jogo."""
        if self.player is None:
            name = self.io.ask_player_name()
            self.player = Player(name)
        digits = self.io.ask_number_of_digits()
        self.engine = GameEngine(digits)
        self.io.clear_history()
        self.io.clear_graph()

        # Inicializa o gráfico (sem mostrar o número correto ainda)
        max_number = 10 ** digits - 1
        self.io.initialize_graph(max_number, self.engine.mysterious_number)

        self.io.show_feedback("O número foi gerado! Tente adivinhar!", colors.TEXT)
        self.play()

    def play(self):
        """Loop principal de palpites."""
        self.engine.attempts = 0

        while True:
            guess = self.io.ask_guess()
            result = self.engine.check_guess(guess)
            self.player.register_guess(self.engine.attempts, guess)

            # Atualiza o gráfico
            self.io.update_graph(guess)

            # Adiciona ao histórico
            if result == "low":
                self.io.show_feedback("Está frio... o número é MAIOR!", colors.INFO)
                self.io.add_history(self.engine.attempts, guess, "Frio ❄️ (baixo)")
            elif result == "high":
                self.io.show_feedback("Está frio... o número é MENOR!", colors.ERROR)
                self.io.add_history(self.engine.attempts, guess, "Frio ❄️ (alto)")
            else:
                # Quando acertar, revela o número correto no gráfico
                self.io.reveal_correct_number()
                self.io.show_feedback(
                    f"🎯 Parabéns, {self.player.name}!\n"
                    f"Você acertou o número {self.engine.mysterious_number} "
                    f"em {self.engine.attempts} tentativas!",
                    colors.SUCCESS
                )
                self.io.add_history(self.engine.attempts, guess, "✅ ACERTOU!")
                break

        self.restart()

    def restart(self):
        """Pergunta se o jogador quer reiniciar."""
        if self.io.ask_restart():
            self.start()
        else:
            self.io.show_feedback("👋 Obrigado por jogar! Até a próxima!", colors.TEXT)
            self.io.root.after(2000, self.io.close)