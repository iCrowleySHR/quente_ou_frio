import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GameGraph:
    def __init__(self, parent, max_number):
        """
        parent: frame ou root do Tkinter onde o gráfico será exibido
        max_number: maior número possível
        """
        self.parent = parent
        self.max_number = max_number
        self.correct_number = None
        self.guesses = []
        self.canvas = None
        self.show_correct_number = False  
    def set_correct_number(self, number):
        self.correct_number = number

    def add_guess(self, guess):
        self.guesses.append(guess)

    def reveal_correct_number(self):
        """Mostra o número correto no gráfico"""
        self.show_correct_number = True

    def clear(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        self.guesses.clear()
        self.correct_number = None
        self.show_correct_number = False

    def show(self):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_title("Tentativas do jogador vs Número correto")
        ax.set_xlabel("Número")
        ax.set_ylabel("Tentativa")

        if self.show_correct_number and self.correct_number is not None:
            ax.axvline(self.correct_number, color='green', linestyle='--', label='Número correto')
            legend_needed = True
        else:
            legend_needed = False

        for i, guess in enumerate(self.guesses, start=1):
            ax.plot(guess, i, 'ro')
            ax.text(guess, i + 0.1, str(guess), fontsize=9, ha='center')

        ax.set_xlim(0, self.max_number)
        ax.set_ylim(0, len(self.guesses) + 2)
        
        if legend_needed:
            ax.legend()
        ax.grid(True)

        self.canvas = FigureCanvasTkAgg(fig, master=self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(padx=10, pady=10, fill="both", expand=True)
