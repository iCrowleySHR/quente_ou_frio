import tkinter as tk
from tkinter import messagebox
from .style import colors, themes
from .graph import GameGraph

class Interface:
    """Interface gráfica com histórico de palpites, feedback colorido e gráfico."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quente ou Frio")
        self.root.attributes('-fullscreen', True)
        self.root.configure(**themes.THEME["window"])
        self.root.resizable(False, False)

        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=colors.BACKGROUND)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # --- Título ---
        self.label_title = tk.Label(self.main_frame, text="Bem-vindo ao Quente ou Frio!", **themes.THEME["label_title"])
        self.label_title.pack(pady=15)

        # --- Entrada ---
        self.entry = tk.Entry(self.main_frame, **themes.THEME["entry"])
        self.entry.pack(pady=5)
        self.entry.focus_set()  # Foco inicial no Entry

        # --- Botão ---
        self.button = tk.Button(self.main_frame, text="OK", command=self._on_submit, **themes.THEME["button"])
        self.button.pack(pady=10)

        # --- Mensagem de feedback ---
        self.feedback_label = tk.Label(self.main_frame, text="", **themes.THEME["label_text"])
        self.feedback_label.pack(pady=10)

        # --- Frame para conteúdo inferior (histórico e gráfico) ---
        self.bottom_frame = tk.Frame(self.main_frame, bg=colors.BACKGROUND)
        self.bottom_frame.pack(fill="both", expand=True, pady=10)

        # --- Frame do histórico (esquerda) ---
        self.history_frame = tk.Frame(self.bottom_frame, bg=colors.BACKGROUND)
        self.history_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.history_title = tk.Label(self.history_frame, text="📜 Histórico de Palpites:", **themes.THEME["label_text"])
        self.history_title.pack()

        self.history_list = tk.Listbox(
            self.history_frame,
            bg=colors.SECONDARY,
            fg=colors.TEXT,
            font=themes.fonts.TEXT_FONT,
            highlightthickness=0,
            selectbackground=colors.ACCENT,
        )
        self.history_list.pack(padx=10, pady=10, fill="both", expand=True)

        # --- Frame do gráfico (direita) ---
        self.graph_frame = tk.Frame(self.bottom_frame, bg=colors.BACKGROUND)
        self.graph_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.graph_title = tk.Label(self.graph_frame, text="📊 Progresso das Tentativas:", **themes.THEME["label_text"])
        self.graph_title.pack()

        # Inicializa o gráfico vazio
        self.game_graph = None

        # Controle interno
        self._input_value = None
        self._waiting_for_input = False

        self.root.bind("<Return>", lambda event: self._on_submit())

    # ---------- Funções de interação ----------
    def _on_submit(self, event=None):
        """Processa a submissão do usuário."""
        if not self._waiting_for_input:
            return
            
        self._input_value = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.entry.focus_set()  # Garante que o foco volte para o Entry
        self._waiting_for_input = False
        self.root.quit()  # Sai do loop principal para continuar o processamento

    def ask_player_name(self) -> str:
        """Solicita o nome do jogador."""
        self.label_title.config(text="Qual é o seu nome?")
        self._waiting_for_input = True
        self.entry.focus_set()
        self.root.mainloop()
        return self._input_value or "Jogador"

    def ask_number_of_digits(self) -> int:
        """Solicita o número de dígitos."""
        self.label_title.config(text="Quantos dígitos terá o número misterioso?")
        self._waiting_for_input = True
        self.entry.focus_set()
        
        while True:
            self.root.mainloop()
            try:
                digits = int(self._input_value)
                if digits > 0:
                    return digits
                else:
                    messagebox.showwarning("Aviso", "Digite um número maior que zero.")
                    self._waiting_for_input = True
                    self.entry.focus_set()
            except ValueError:
                messagebox.showwarning("Erro", "Digite um número inteiro válido.")
                self._waiting_for_input = True
                self.entry.focus_set()

    def ask_guess(self) -> int:
        """Solicita um palpite do jogador."""
        self.label_title.config(text="Chute um número:")
        self._waiting_for_input = True
        self.entry.focus_set()
        
        while True:
            self.root.mainloop()
            try:
                return int(self._input_value)
            except ValueError:
                messagebox.showwarning("Erro", "Digite um número válido.")
                self._waiting_for_input = True
                self.entry.focus_set()

    # ---------- Exibição visual ----------
    def show_feedback(self, text: str, color: str):
        """Mostra mensagem colorida."""
        self.feedback_label.config(text=text, fg=color)
        self.root.update()  # Atualiza a interface para mostrar o feedback

    def add_history(self, attempt: int, guess: int, result: str):
        """Adiciona o palpite à lista."""
        self.history_list.insert(tk.END, f"Tentativa {attempt}: {guess} → {result}")
        # Rola para o final da lista
        self.history_list.see(tk.END)

    def ask_restart(self) -> bool:
        """Pergunta se o jogador quer reiniciar."""
        return messagebox.askyesno("Reiniciar", "Quer jogar de novo?")

    def clear_history(self):
        """Limpa o histórico de palpites."""
        self.history_list.delete(0, tk.END)

    def close(self):
        """Fecha a janela."""
        self.root.destroy()

    # ---------- Funções do gráfico ----------
    def initialize_graph(self, max_number: int, correct_number: int):
        """Inicializa o gráfico do jogo."""
        if self.game_graph:
            self.game_graph.clear()
        
        self.game_graph = GameGraph(self.graph_frame, max_number)
        self.game_graph.set_correct_number(correct_number)

    def update_graph(self, guess: int):
        """Atualiza o gráfico com um novo palpite."""
        if self.game_graph:
            self.game_graph.add_guess(guess)
            # Limpa o frame do gráfico antes de mostrar o novo
            for widget in self.graph_frame.winfo_children():
                if isinstance(widget, tk.Frame) or hasattr(widget, '_name') and 'canvas' in str(widget._name).lower():
                    widget.destroy()
            self.game_graph.show()

    def reveal_correct_number(self):
        """Revela o número correto no gráfico"""
        if self.game_graph:
            self.game_graph.reveal_correct_number()
            # Atualiza o gráfico para mostrar o número correto
            for widget in self.graph_frame.winfo_children():
                if isinstance(widget, tk.Frame) or hasattr(widget, '_name') and 'canvas' in str(widget._name).lower():
                    widget.destroy()
            self.game_graph.show()

    def clear_graph(self):
        """Limpa o gráfico."""
        if self.game_graph:
            self.game_graph.clear()
            self.game_graph = None