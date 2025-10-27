from .jogador import Jogador
from .utils import gerar_numero_misterioso

class JogoQuenteFrio:
    def __init__(self):
        self.jogador = None
        self.numero_misterioso = None
        self.tentativas = 0

    def iniciar(self):
        """Inicia o jogo, pedindo nome e número de dígitos."""
        nome = input("Olá! Qual é o seu nome? ").strip()
        self.jogador = Jogador(nome)

        while True:
            try:
                digitos = int(input("Quantos dígitos terá o número misterioso? "))
                if digitos <= 0:
                    print("Digite um número de dígitos válido (maior que zero).")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

        self.numero_misterioso = gerar_numero_misterioso(digitos)
        print("\nO número foi gerado! Tente adivinhar:\n")

        self.jogar()

    def jogar(self):
        """Loop principal de tentativas."""
        self.tentativas = 0

        while True:
            try:
                chute = int(input("Chute um número: "))
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            self.tentativas += 1
            self.jogador.registrar_palpite(self.tentativas, chute)

            if chute < self.numero_misterioso:
                print("O número jogado é menor que o número misterioso.\n")
            elif chute > self.numero_misterioso:
                print("O número jogado é maior que o número misterioso.\n")
            else:
                print(
                    f"🎉 Parabéns, {self.jogador.nome}! "
                    f"Você acertou o número misterioso {self.numero_misterioso} "
                    f"em {self.tentativas} tentativas.\n"
                )
                break

        self.reiniciar()

    def reiniciar(self):
        """Pergunta se o jogador quer jogar novamente."""
        while True:
            resposta = input("Quer jogar de novo? (sim/não): ").strip().lower()
            if resposta in ("sim", "s"):
                print("\n🔄 Reiniciando o jogo...\n")
                self.iniciar()
                break
            elif resposta in ("não", "nao", "n"):
                print("👋 Obrigado por jogar! Até a próxima!")
                break
            else:
                print("Resposta inválida. Digite 'sim' ou 'não'.")
