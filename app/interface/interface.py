import tkinter as tk
from tkinter import messagebox
from .style import colors, themes

class Interface:
    """Interface gráfica com histórico de palpites e feedback colorido."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quente ou Frio")
        self.root.geometry("700x600")
        self.root.configure(**themes.THEME["window"])
        self.root.resizable(False, False)

        # --- Título ---
        self.label_title = tk.Label(self.root, text="Bem-vindo ao Quente ou Frio!", **themes.THEME["label_title"])
        self.label_title.pack(pady=15)

        # --- Entrada ---
        self.entry = tk.Entry(self.root, **themes.THEME["entry"])
        self.entry.pack(pady=5)

        # --- Botão ---
        self.button = tk.Button(self.root, text="OK", command=self._on_submit, **themes.THEME["button"])
        self.button.pack(pady=10)

        # --- Mensagem de feedback ---
        self.feedback_label = tk.Label(self.root, text="", **themes.THEME["label_text"])
        self.feedback_label.pack(pady=10)

        # --- Histórico ---
        self.history_frame = tk.Frame(self.root, bg=colors.BACKGROUND)
        self.history_frame.pack(pady=10, fill="both", expand=True)

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
        self.history_list.pack(padx=20, pady=10, fill="both", expand=True)

        # Controle interno
        self._input_value = None

    # ---------- Funções de interação ----------
    def _on_submit(self):
        self._input_value = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.root.quit()

    def ask_player_name(self) -> str:
        self.label_title.config(text="Qual é o seu nome?")
        self.root.mainloop()
        return self._input_value or "Jogador"

    def ask_number_of_digits(self) -> int:
        self.label_title.config(text="Quantos dígitos terá o número misterioso?")
        while True:
            self.root.mainloop()
            try:
                digits = int(self._input_value)
                if digits > 0:
                    return digits
                else:
                    messagebox.showwarning("Aviso", "Digite um número maior que zero.")
            except ValueError:
                messagebox.showwarning("Erro", "Digite um número inteiro válido.")

    def ask_guess(self) -> int:
        self.label_title.config(text="Chute um número:")
        while True:
            self.root.mainloop()
            try:
                return int(self._input_value)
            except ValueError:
                messagebox.showwarning("Erro", "Digite um número válido.")

    # ---------- Exibição visual ----------
    def show_feedback(self, text: str, color: str):
        """Mostra mensagem colorida."""
        self.feedback_label.config(text=text, fg=color)

    def add_history(self, attempt: int, guess: int, result: str):
        """Adiciona o palpite à lista."""
        self.history_list.insert(tk.END, f"Tentativa {attempt}: {guess} → {result}")

    def ask_restart(self) -> bool:
        return messagebox.askyesno("Reiniciar", "Quer jogar de novo?")

    def clear_history(self):
        self.history_list.delete(0, tk.END)

    def close(self):
        self.root.destroy()
