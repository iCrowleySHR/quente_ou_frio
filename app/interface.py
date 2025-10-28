class Interface:
    """Entrada e saída do jogo (input e print)."""

    def ask_player_name(self) -> str:
        while True:
            name = input("Olá! Qual é o seu nome? ").strip()
            if name:
                print(f"👋 Bem-vindo, {name}!\n")
                return name
            print("Por favor, digite um nome válido.\n")

    def ask_number_of_digits(self) -> int:
        while True:
            try:
                digits = int(input("Quantos dígitos terá o número misterioso? "))
                if digits <= 0:
                    print("Digite um número de dígitos válido (maior que zero).\n")
                    continue
                return digits
            except ValueError:
                print("Por favor, digite um número inteiro válido.\n")

    def ask_guess(self) -> int:
        while True:
            try:
                return int(input("Chute um número: "))
            except ValueError:
                print("Por favor, digite um número válido.\n")

    def ask_restart(self) -> bool:
        while True:
            response = input("Quer jogar de novo? (sim/não): ").strip().lower()
            if response in ("sim", "s"):
                return True
            elif response in ("não", "nao", "n"):
                return False
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.\n")
