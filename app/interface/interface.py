import tkinter as tk
from tkinter import messagebox
from .style.themes import THEME

class Interface:
    """Interface gráfica estilizada para o jogo 'Quente ou Frio'."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quente ou Frio")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(**THEME["window"])

        self.label = tk.Label(self.root, text="Bem-vindo ao Quente ou Frio!", **THEME["label_title"])
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.root, **THEME["entry"])
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="OK", command=self._on_submit, **THEME["button"])
        self.button.pack(pady=10)

        self.output = tk.Label(self.root, text="", **THEME["label_text"])
        self.output.pack(pady=20)

        self._input_value = None

    def _on_submit(self):
        self._input_value = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        self.root.quit()

    def ask_player_name(self) -> str:
        self.label.config(text="Qual é o seu nome?")
        self.root.mainloop()
        return self._input_value or "Jogador"

    def ask_number_of_digits(self) -> int:
        self.label.config(text="Quantos dígitos terá o número misterioso?")
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
        self.label.config(text="Chute um número:")
        while True:
            self.root.mainloop()
            try:
                return int(self._input_value)
            except ValueError:
                messagebox.showwarning("Erro", "Digite um número válido.")

    def show_message(self, text: str):
        self.output.config(text=text)

    def ask_restart(self) -> bool:
        return messagebox.askyesno("Reiniciar", "Quer jogar de novo?")

    def close(self):
        self.root.destroy()
